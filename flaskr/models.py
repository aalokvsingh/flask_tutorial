 from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))

    def __repr__(self):
        if self.name:
            return "{} <{}>".format(
                self.username)
        return self.firstname