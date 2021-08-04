from flask import Flask,Blueprint,jsonify,json,request
# from flaskr import current_app as app
# from flask import current_app as app
from werkzeug.security import generate_password_hash,check_password_hash
# from app import db
from flaskr.models import user

user_blueprint = Blueprint('user_blueprint','__name__',url_prefix='/user')


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(200))
#     password = db.Column(db.String(200))
#     firstname = db.Column(db.String(200))
#     lastname = db.Column(db.String(200))

#     def __repr__(self):
#         if self.name:
#             return "{} <{}>".format(
#                 self.username)
#         return self.firstname

@user_blueprint.route('/<int:id>', methods=['POST']) 
@user_blueprint.route('/', methods=['POST'])
def get_user(id=None):
    #user = User.query.filter_by(username='alok5n').first()
    # users = User.query.filter_by(id=id).all()

    # if not users:
    #    return jsonify({'message': 'User does not exist'})
    
    # return user

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


