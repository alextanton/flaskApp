from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(20), index=True, unique=False)
    messages = db.relationship('Message', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)