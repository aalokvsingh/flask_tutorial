from flask import Flask,Blueprint,jsonify,json,request,make_response
from werkzeug.security import generate_password_hash,check_password_hash
from flaskr.models import User
import jwt
from datetime import datetime,timedelta
from flask import current_app as app
from functools import wraps
from . import db,logging
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
            return make_response(jsonify({'status':False,"data":[],'message':'a valid token is missing'}),200)
        # return token
        try:
            # return token
            data = jwt.decode(token, app.config['SECRET_KEY'])
            # return data['username']
            current_user = User.query.filter_by(username=data['username']).first()
            # return current_user.username
        except:
           return make_response(jsonify({'status':False,"data":[],'message':'token is invalid!'}),200)

        return f(current_user, *args, **kwargs)

    return decorator

@user_blueprint.route('/', methods=['POST'])
@user_blueprint.route('/<int:id>', methods=['POST'])
@token_required
def get_user1(self,id=None):
    # return make_response(jsonify(111))
    users = {}
    if id is None:
        users = User.query.all()
    else:
        users = User.query.filter_by(id=id).all()
        # return jsonify(users)
    
    result = []
    logging.info(users)
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['password'] = user.password
        user_data['firstname'] = user.firstname
        user_data['lastname'] = user.lastname

        result.append(user_data)
    return make_response(jsonify({'status':True,"data":result,'message':'Data Found'}),200)
    

    # userData = {'id':id,'username':'alok5n','firstname':'Alok SIngh'}
    # return jsonify(userData)

@user_blueprint.route('/register',methods=['POST'])
def register():
    # data = request.get_json(force=True)
    data  = request.get_data()
    msg = ""
    id =""
    try:
        jsonData = json.loads(data)
        logging.info(jsonData)
        # return jsonData

        firstname   =  jsonData.get('firstname')
        lastname    =  jsonData.get('lastname')
        username    =  jsonData.get('username')
        password    =  jsonData.get('password')
        if not firstname or not lastname or not username or not password:
            column = ''
            if not firstname:
                column ='firstname'
            if not lastname:
                column ='lastname'
            if not username:
                column ='username'
            if not password:
                column ='password'
            msg = column+' is requird required'
            return make_response(jsonify({'status':False,'data':[],'message':msg}),3000)
        hashed_pwd = generate_password_hash(password,method='sha256') if 'password' in jsonData else ''
        jsonData['password'] = hashed_pwd
        userData = User(firstname=jsonData['firstname'],lastname=jsonData['lastname'],username=jsonData['username'],password=jsonData['password'])
        logging.info(userData)
        db.session.add(userData)
        db.session.commit()
        if userData.id:
            id =userData.id
            msg ='User Registration Successfull'
        else:
            msg ='User Registration UnSuccessfull'
        logging.info(msg)
        return make_response(jsonify({'status':True,"data":[id],'message':msg}),200)
    except Exception as e:
        logging.error(e)
        return make_response(jsonify({'status':False,"data":[],'message':str(e)+' Invalid Input'}),200)
       

    

    

@user_blueprint.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        data  = request.get_data()
        # print(type(data))
        if data:
            JsonData = json.loads(data)
            password = JsonData['password']
            username=JsonData['username']
            UserData = User.query.filter_by(username=username).first()
            if UserData:
                verify_password = check_password_hash(UserData.password,password)
            if UserData and verify_password:
                # return(jsonify([UserData.lastname,UserData.firstname,UserData.id]))
                # generates the JWT Token
                token = jwt.encode({
                    'username': UserData.username,
                    'exp' : datetime.utcnow() + timedelta(minutes = 30)
                },app.config['SECRET_KEY'])

                return make_response(
                    jsonify({'status':True,'data':[token.decode('UTF-8')],'message':'authentication successfull'}),
                    201
                )
    
            else:
                #return jsonify({'status':'Invalid Usernaem or password'}),401
                return make_response(
                    jsonify({'status':False,'data':[],'message':'Could not verify'}),
                    403,
                    {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
                )
        else:
            # return jsonify({'status':'Request payload is empty'})
            return make_response(
                jsonify({'status':False,'data':[],'message':'username and Password required'}),
            401,
            {'WWW-Authenticate' : 'Basic realm ="Username and Password required !!"'}
        )
    else:

        return make_response(jsonify({'status':False,"data":[],'message':'Invalid requst method'}),200)
        


