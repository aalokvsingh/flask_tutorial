import os
from flask import Flask
# from instance.config import *
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.orm import validates
from flask import Flask,Blueprint,jsonify,json,request,make_response
db = SQLAlchemy()
logging.basicConfig(filename = 'flask_tutorial.log' , level = logging.DEBUG, format = f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
#factory pattern
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_ECHO"] = True
    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    db.init_app(app)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr import user
    app.register_blueprint(user.user_blueprint)

    from flaskr.post import post
    app.register_blueprint(post.post_blueprint)

    @app.route('/hellojson', methods=('GET', 'POST'))
    def hellojson():
        userData = {'username':'alok5n','firstname':'Alok Singh'}
        return userData

    
    return app