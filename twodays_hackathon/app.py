from flask import Flask, render_template, jsonify, request
import config
import models
from models import *

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/1')
def homepage():  # put application's code here
    result = models.students.query.all()
    print("ywt1")
    return render_template('homepage.html', list=result)


if __name__ == '__main__':
    app.config.from_object(config)
    db.init_app(app)
    app.run()
