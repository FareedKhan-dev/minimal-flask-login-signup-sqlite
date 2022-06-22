from __main__ import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # filename = db.Column(db.String(300))
    # data = db.Column(db.LargeBinary)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"