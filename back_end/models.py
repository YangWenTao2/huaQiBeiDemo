from database import db

"""class students(db.Model):
    name = db.Column(db.String(10))
    ID = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)"""


class numBeta(db.Model):
    CompanyNo = db.Column(db.String(6), primary_key=True)
    endDate = db.Column(db.String)
    beta = db.Column(db.Float)


class user(db.Model):
    name = db.Column(db.String(100))
    email = db.Column(db.String(30), primary_key=True)
    isvip = db.Column(db.String(5))
    Pass = db.Column(db.String(19))


class num_leverage(db.Model):
    CompanyNo = db.Column(db.String(6), primary_key=True)
    EndDate = db.Column(db.TEXT)
    leverage = db.Column(db.Float)


class numName(db.Model):
    CompanyNo = db.Column(db.String(6))
    CompanyName = db.Column(db.String(8))


class export_importWithData(db.Model):
    EndDate = db.Column(db.String(11))
    Export = db.Column(db.Float)
    Import = db.Column(db.Float)
    Retail = db.Column(db.Float)
    GDP = db.Column(db.Float)
    FCap = db.Column(db.String(4))
    Infla = db.Column(db.Float)
    RtoUSD = db.Column(db.Float)
    RtoEU = db.Column(db.Float)
    RtoYEN = db.Column(db.Float)
    Income = db.Column(db.String(4))
    M2 = db.Column(db.Float)
    SHIBOR = db.Column(db.Float)
    Spend = db.Column(db.String(5))
    Settle = db.Column(db.Float)
    Sale = db.Column(db.Float)

class comnumYield(db.Model):
    CompanyNo = db.Column(db.String(6))
    EndDate = db.Column(db.String(11))
    Yield = db.Column(db.Float)
