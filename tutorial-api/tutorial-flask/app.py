from flask import Flask

app = Flask(__name__)

@app.route("/ping", methods=['GET']) # 엔드포인트를 @app.route 데코레이터를 통해 구현
def ping():
    return "pong"