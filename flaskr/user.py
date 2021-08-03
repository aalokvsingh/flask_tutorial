from flask import Blueprint,jsonify,json,request
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy

user_blueprint = Blueprint('user_blueprint','__name__',url_prefix='/user')

@user_blueprint.route('/<int:id>', methods=['POST'])
@user_blueprint.route('/', methods=['POST'])
def get_user(id=None):
    userData = {'id':id,'username':'alok5n','firstname':'Alok SIngh'}
    return jsonify(userData)

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
    return jsonify({'status':'user login function'})


