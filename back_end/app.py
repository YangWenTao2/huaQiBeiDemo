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
    raw_data = list(request.form.to_dict().keys())[0]
    data = json.loads(raw_data)
    name = data['name']
    email = data['email']
    password = data['password']
    # test:
    # name = "ywt"
    # email = "303597673@qq.com"
    # password = "ygwt010825"
    if (models.user.query.filter_by(name=name).first() is not None or
            models.user.query.filter_by(email=email).first() is not None):
        return jsonify({"state": 1})
    else:
        new = user(name=name, isvip="false", email=email, Pass=password)
        db.session.add(new)
        db.session.commit()
        return jsonify({"state": 2})


@app.route('/login', methods=['POST'])
def login():
    raw_data = list(request.form.to_dict().keys())[0]
    data = json.loads(raw_data)
    email = data['email']
    password = data['password']
    if models.user.query.filter_by(email=email).first() is not None:
        this_user = models.user.query.filter_by(email=email).first()
        if password == this_user.Pass:
            return jsonify({"state": 0})
        else:
            return jsonify({"state": 1})
    else:
        return jsonify({"state": 2})


@app.route('/updateVIPState', methods=['POST'])
def update_vip_state():
    raw_data = list(request.form.to_dict().keys())[0]
    data = json.loads(raw_data)
    email = data['email']
    is_vip = data['isVIP']
    this_user = models.user.query.get(email)
    this_user.isvip = is_vip
    db.set_trace().commit()


@app.route('/search', methods=['POST'])
def return_search_result():
    raw_data = list(request.form.to_dict().keys())[0]
    data = json.loads(raw_data)
    search_input = data['searchInput']
    # todo
    # 访问数据库查询、数据处理与返回
    return jsonify(
        {'companyName': ''},
        {'companyStockNumber': ''},
        {'betaValues': [
            {'date': '', 'value': ''},
            {'date': '', 'value': ''},
            {'date': '', 'value': ''}
        ]},
        {'exchangeRateRisk': [
            {'date': '', 'value': ''},
            {'date': '', 'value': ''},
            {'date': '', 'value': ''}
        ]},
        {'financialLeverage': [
            {'date': '', 'value': ''},
            {'date': '', 'value': ''},
            {'date': '', 'value': ''}
        ]}
    )


@app.route('/get-macro', methods=['GET'])
def return_search_result():
    # todo
    # 访问数据库查询、数据处理与返回
    return jsonify(
        # GDP变动率
        {'GDPChangeRate': [
            {'date': '', 'value': ''},
            {'date': '', 'value': ''},
            {'date': '', 'value': ''}
        ]},
        # 外汇汇率波动率
        {'ForeignExchangeRateFluctuation': [
            {'date': '', 'value': ''},
            {'date': '', 'value': ''},
            {'date': '', 'value': ''}
        ]},
        # 结售汇变动率
        {'ExchangeSettlementChangeRate': [
            {'date': '', 'value': ''},
            {'date': '', 'value': ''},
            {'date': '', 'value': ''}
        ]},
        # 进出口变动率
        {'ImportAndExportChangeRate': [
            {'date': '', 'value': ''},
            {'date': '', 'value': ''},
            {'date': '', 'value': ''}
        ]},
        # 社会销售品零售总额变动率
        {'TotalSalesChangeRate': [
            {'date': '', 'value': ''},
            {'date': '', 'value': ''},
            {'date': '', 'value': ''}
        ]}
    )


@app.route("/get", methods=["GET"])
def get_():
    return "1"


if __name__ == '__main__':
    app.run()
