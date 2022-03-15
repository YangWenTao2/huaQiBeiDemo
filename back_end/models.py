from database import db


class students(db.Model):
    name = db.Column(db.String(10))
    ID = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)


class numBeta(db.Model):
    CompanyNo = db.Column(db.String(6),primary_key=True)
    endDate = db.Column(db.String)
    beta=db.Column(db.Float)


class user(db.Model):
    name=db.Column(db.String(100))
    email =db.Column(db.String(30),primary_key=True)
    isVip = db.Column(db.String(5))
    Pass = db.Column(db.String(19))

