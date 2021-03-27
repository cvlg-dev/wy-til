from flask import Flask, jsonify, request

app = Flask(__name__)
app.id_count = 1
app.users = {}



@app.route("/ping", methods=['GET']) # 엔드포인트를 @app.route 데코레이터를 통해 구현
def ping():
    return "pong"



@app.route("/sign-up", methods=['POST'])
def sign_up():
    new_user = request.json
    new_user["id"] = app.id_count
    app.users[app.id_count] = new_user
    app.id_count = app.id_count + 1

    return jsonify(new_user)