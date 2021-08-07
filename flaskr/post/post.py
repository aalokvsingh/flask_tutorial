from flask import Blueprint,jsonify,json,request,make_response
from flaskr.post.postModel import Post
from flaskr.user import token_required

post_blueprint = Blueprint('post_blueprint','__name__',url_prefix='/post')

@post_blueprint.route('/')
@token_required
def post_list(self):
    posts = Post.query.all()
    result = []
    
    for post in posts:
        post_data = {}
        post_data['id'] = post.id
        post_data['ptitle'] = post.ptitle
        post_data['pcontent'] = post.pcontent

        result.append(post_data)
    return jsonify(result)
    
# @post_blueprint.route('/create')
# def create_post():
