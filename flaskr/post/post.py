from flask import Blueprint,jsonify,json,request,make_response
from flaskr.post.postModel import Post
from flaskr.user import token_required
from flaskr import db,logging
import datetime

post_blueprint = Blueprint('post_blueprint','__name__',url_prefix='/post')

@post_blueprint.route('/',methods=['GET','POST'])
@post_blueprint.route('/<int:id>',methods=['GET','POST'])
# @token_required
def post_list(id=None):
    if id is None:
        posts = Post.query.all()
    else:
        posts= Post.query.filter_by(id=id).all()
    result = []
    
    for post in posts:
        post_data = {}
        post_data['id'] = post.id
        post_data['ptitle'] = post.ptitle
        post_data['pcontent'] = post.pcontent
        post_data['create_at'] = post.create_at

        result.append(post_data)
    return jsonify(result)
    
@post_blueprint.route('/create-post',methods=['POST'])
@token_required
def create_post(self):
    try:
        getpayload = request.get_data()
        jsonData = json.loads(getpayload)
        ptitle   =  jsonData.get('ptitle')
        pcontent   =  jsonData.get('pcontent')
        create_at   =  datetime.datetime.now()
        # now = datetime.datetime.utcnow()
        # create_at = now.strftime('%Y-%m-%d %H:%M:%S')
        if not ptitle or not pcontent:
            return make_response(jsonify({'status':False,'data':[],'message':"ptitle and pcontent is required"}),300)
        
        postData = Post(ptitle=ptitle,pcontent=pcontent,create_at=create_at)
        logging.info(postData)
        db.session.add(postData)
        db.session.commit()
        if postData.id:
            id = postData.id
            msg ='Post created Successfull'
        else:
            msg ='Post not created'

        logging.info(msg)
        return make_response(jsonify({'status':True,"data":[id],'message':msg}),200)
    except Exception as e:
        logging.error(e)
        return make_response(jsonify({'status':False,'data':[],'message':str(e)}),500)
        
@post_blueprint.route('/delete/<int:id>',methods=['DELETE'])
@token_required
def post_delete(self,id):
    try:
        if id:
            post = Post.query.filter_by(id=id).first()
            if not post:
                msg = 'Post not found!'
                return make_response(jsonify({'status':True,"data":[id],'message':msg}),200)
            
            db.session.delete(post)
            db.session.commit()

            msg ='Post deleted'
            logging.info(msg)
            return make_response(jsonify({'status':True,"data":[id],'message':msg}),200)
    except Exception as e:
        logging.error(e)
        return make_response(jsonify({'status':False,'data':[],'message':str(e)}),500)

@post_blueprint.route('/update/<int:id>',methods=['PATCH'])
@token_required
def post_update(self,id):
    try:
        if id:
            getpayload = request.get_data()
            jsonData = json.loads(getpayload)
            ptitle   =  jsonData.get('ptitle')
            pcontent   =  jsonData.get('pcontent')

            post = Post.query.get(id)
            if not post:
                msg = 'Post not found!'
                return make_response(jsonify({'status':True,"data":[id],'message':msg}),200)
            post.ptitle = ptitle
            post.pcontent = pcontent
            db.session.commit()
            msg ='Post Updated !'
            logging.info(msg)
            return make_response(jsonify({'status':True,"data":[id],'message':msg}),200)
    except Exception as e:
        logging.error(e)
        return make_response(jsonify({'status':False,'data':[],'message':str(e)}),500)
