from database import db


class students(db.Model):
    name = db.Column(db.String(10))
    ID = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)




