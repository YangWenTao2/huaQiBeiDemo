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


@app.route('/register', methods=['POST'])
def register():
    for key in request.form.to_dict().keys():
        data = json.loads(key)
        name = data['name']
        email = data['email']
        password = data['password']
    # test:
    # name = "ywt"
    # email = "303597673@qq.com"
    # password = "ygwt010825"
        if (models.user.query.filter_by(name=name).first() is not None or
                models.user.query.filter_by(email=email).first() is not None):
            return jsonify({"response": 1})
        else:
            new = user(name=name, isvip="false", email=email, Pass=password)
            db.session.add(new)
            db.session.commit()
            return jsonify({"response": 2})


@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.form.get('data'))
    email = data['email']
    password = data['password']
    if models.user.query.filter_by(email=email).first() is not None:
        this_user = models.user.query.filter_by(email=email).first()
        if password == this_user.Pass:
            return jsonify({"response": 0})
        else:
            return jsonify({"response": 2})
    else:
        return jsonify({"response": 2})


@app.route('/updateVIPState', methods=['POST'])
def update_vip_state():
    data = json.loads(request.form.get('data'))
    email = data['email']
    is_vip = data['isVIP']
    this_user = models.user.query.get(email)
    this_user.isvip = is_vip
    db.set_trace().commit()


if __name__ == '__main__':
    app.run()
