from flaskr import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ptitle = db.Column(db.String(255))
    pcontent = db.Column(db.String(255))
    create_at = db.Column(db.String(255))
    image_path = db.Column(db.String(255))
