from flask import Flask,Blueprint,jsonify,json,request
# from flaskr import current_app as app
# from flask import current_app as app
from werkzeug.security import generate_password_hash,check_password_hash
# from app import db
from .models import User

user_blueprint = Blueprint('user_blueprint','__name__',url_prefix='/user')

@user_blueprint.route('/<int:id>', methods=['POST']) 
@user_blueprint.route('/', methods=['POST'])
def get_user(id=None):
    if id is None:
        users = User.query.all()
    else:
        users = User.query.filter_by(id=id).first()
        return jsonify(users)
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
    # users = User.query.filter_by(id=id).first()
    # users = User.query.all()

    # if not users:
    #    return jsonify({'message': 'User does not exist'})
    # # print(users)
    # for user in users:
    #     print(user)
    #     return list(user)
    # return dict(users)

    # output = []

    # for post in posts:
    #     post_data = {}
    #     post_data['post_title']=post.post_title
    #     post_data['post_content']=post.post_content
    #     post_data['filename']=post.filename

    #     output.append(post_data)

    # return jsonify({"list of posts":output})

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


