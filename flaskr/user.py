from flask import Flask,Blueprint,jsonify,json,request,make_response
from werkzeug.security import generate_password_hash,check_password_hash
from flaskr.models import User
import jwt
from datetime import datetime,timedelta
from flask import current_app as app
from functools import wraps

user_blueprint = Blueprint('user_blueprint','__name__',url_prefix='/user')

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None
        # current_user =''
        if 'x-api-key' in request.headers:
            token = request.headers['x-api-key']
            # return token
        # return token
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        # return token
        try:
            # return token
            data = jwt.decode(token, app.config['SECRET_KEY'])
            # return data['username']
            current_user = User.query.filter_by(username=data['username']).first()
            # return current_user.username
        except:
           return jsonify({'message': 'token is invalid!'})
          
        return f(current_user, *args, **kwargs)

    return decorator

@user_blueprint.route('/', methods=['POST'])
@user_blueprint.route('/<int:id>', methods=['POST'])
@token_required
def get_user1(self,id=None):
    # return make_response(jsonify(111))
    if id is None:
        users = User.query.all()
    else:
        users = User.query.filter_by(id=id).all()
        # return jsonify(users)
    result = []
    
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['password'] = user.password
        user_data['firstname'] = user.firstname
        user_data['lastname'] = user.lastname

        result.append(user_data)
    return jsonify(result)
    

    # userData = {'id':id,'username':'alok5n','firstname':'Alok SIngh'}
    # return jsonify(userData)

@user_blueprint.route('/register',methods=['POST'])
def register():
    # data = request.get_json(force=True)
    data  = request.get_data()
    try:
        jsonData = json.loads(data)
        # return jsonData

        firstname   =  request.json.get('firstname')
        lastname    =  request.json.get('lastname')
        username    =  request.json.get('username')
        password    =  request.json.get('password')
        hashed_pwd = generate_password_hash(password,method='sha256')

        return jsonify({'firstname':firstname})
    except:
        return jsonify({'status':"Invalid Input!"})

    

    

@user_blueprint.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        data  = request.get_data()
        # print(type(data))
        if data:
            JsonData = json.loads(data)
            # return(JsonData['username'])
            # password = check_password_hash(JsonData['password'])
            password = JsonData['password']
            username=JsonData['username']
            UserData = User.query.filter_by(username=username,password=password).first()
            if UserData:
                # return(jsonify([UserData.lastname,UserData.firstname,UserData.id]))
                # generates the JWT Token
                token = jwt.encode({
                    'username': UserData.username,
                    'exp' : datetime.utcnow() + timedelta(minutes = 30)
                },app.config['SECRET_KEY'])

                return make_response(
                    jsonify({'token' : token.decode('UTF-8')}),
                    201
                )
    
            else:
                #return jsonify({'status':'Invalid Usernaem or password'}),401
                return make_response(
                    'Could not verify',
                    403,
                    {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
                )
        else:
            # return jsonify({'status':'Request payload is empty'})
            return make_response(
            'username and Password required',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Username and Password required !!"'}
        )
    else:

        return jsonify({'status':'Invali requst method'})
        


