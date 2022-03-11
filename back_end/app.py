import json

from flask import Flask, render_template, jsonify, request
import config
import models
from flask_cors import CORS
from models import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(config)
db.init_app(app)



@app.route('/register')
def register():
    #data = json.loads(request.form.get('data'))
    """  name = data['name']
    email = data['email']
    password = data['password']"""
    #test:
    name="ywt"
    email="303597673@qq.com"
    password="ygwt010825"
    if( models.user.query.filter_by(name=name).first()!=None or models.user.query.filter_by(email=email).first()!=None):
        return 1
    else:
        new = user(name, 0, email, password)
        db.session.add(new)
        db.session.commtit()
        return 0
   #todo:服务器错误则RETURN 2;

@app.route('/login')
def login():
    data = json.loads(request.form.get('data'))
    email = data['email']
    password = data['password']
    if(models.user.query.filter_by(email=email).first()!=None):
        ThisUser=models.user.query.filter_by(email=email).first()
        if password == ThisUser.Pass :
            return 0
        else:
            return 2
    else:
        return 2

@app.route('/updateVIPState')
def updateVIPState():
    data = json.loads(request.form.get('data'))
    email = data['email']
    isVIP = data['isVIP']



if __name__ == '__main__':

    app.run()
