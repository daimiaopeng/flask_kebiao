from flask import Flask, make_response, redirect, url_for, session,Response,render_template
from flask import jsonify
from flask import request

from kbtable import *

app = Flask(__name__)
app.secret_key = 'nwenroiu2384u1'


@app.route('/', methods=['GET', 'POST'])
def index():
    return "OK"

@app.route('/api', methods=['GET'])
def api():
    name = request.args.get('name')
    password = request.args.get('password')
    print(name)
    print(password)
    return '你输入的name：%s ,password：%s' % (name, password)


@app.route('/api/kb', methods=['GET'])
def kb():
    name = request.args.get('name')
    password = request.args.get('password')
    print(name)
    # print(password)
    try:
        # a = str(get_kb(name, password))
        return jsonify(get_kb(name, password))
    except:
        return '用户名或者密码错误'


@app.route('/test', methods=['GET', 'POST'])
def test():
    response = make_response()
    return jsonify(name='123')




if __name__ == '__main__':
    app.run(port=80)
