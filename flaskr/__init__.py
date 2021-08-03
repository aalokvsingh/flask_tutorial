import os

from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:monu1988@localhost/flask_tutorial'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.init_app(app)

    # shell context for flask cli
    # @app.shell_context_processor
    # def ctx():
    #     return {"app": app, "db": db}

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flaskr.auth import bp
    app.register_blueprint(bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/',endpoint='index')

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from flaskr import user
    app.register_blueprint(user.user_blueprint)

    @app.route('/hellojson', methods=('GET', 'POST'))
    def hellojson():
        userData = {'username':'alok5n','firstname':'Alok SIngh'}
        return jsonify(userData)

    return app