from flask import Flask, jsonify, request, current_app
from flask.json import JSONEncoder
from sqlalchemy import create_engine, text


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return JSONEncoder.default(self, obj)


def insert_user(user):
    # 새로운 사용자 정보를 users테이블에 저장
    return current_app.database.execute(text("""
        INSERT INTO users (
            name,
            email,
            profile,
            hashed_password
        ) VALUES (
            :name,
            :email,
            :profile,
            :password
        )
    """), user).lastrowid # 새로 사용자가 생성되면, 새로 생성된 사용자의 id를 lastrowid를 통해 읽어들임

def get_user(user_id):
    user = current_app.database.execute(text("""
    SELECT
        id,
        name,
        email,
        profile
    FROM users
    WHERE
        id = :user_id
    """), {
        'user_id' : user_id
    }).fetchone()

    return {
        'id'        : user['id'],
        'name'      : user['name'],
        'email'     : user['email'],
        'profile'   : user['profile']
    } if user else None

def insert_tweet(user_tweet):
    return current_app.database.execute(text("""
    INSERT INTO tweets (
        user_id, 
        tweet
    ) VALUES (
        :id,
        :tweet
        ) 
    """), user_tweet).rowcount

def get_timeline(user_id):
    timeline = current_app.database.execute(text("""
        SELECT
            t.user_id,
            t.tweet
        FROM tweets as t
        LEFT JOIN user_follow_list as u
        ON u.user_id = :user_id
        WHERE t.user_id = :user_id OR 
              t.user_id = u.follow_user_id
    """), {
        'user_id': user_id
    }).fetchall()

    return [{
        'user_id' : tweet['user_id'],
        'tweet'   : tweet['tweet']
    } for tweet in timeline]


# create_app 함수: 플라스크가 해당 이름의 함수를 자동으로 팩토맇마수로 인식하여, 해당 함수를 통해 플라스크를 실행함.
def create_app(test_config = None):
    # test_config: unit test를 실행시킬 때 테스트용 데이터베이스 등의 테스트 설정 정보

    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    # 데이터베이스 객체 생성 및 플라스크 객체에 DB객체를 저장함
    database = create_engine(app.config["DB_URL"], encoding='utf-8', max_overflow=0)
    app.database = database

    @app.route("/ping", methods=["GET"])
    def ping():
        return "pong"

    # 회원가입 엔드포인트
    @app.route("/sign_up", methods=['POST'])
    def sign_up():
        new_user = request.json

        # 새로운 사용자 정보를 users테이블에 저장
        new_user_id = insert_user(new_user)
        new_user = get_user(new_user_id)
        return jsonify(new_user)


    @app.route("/tweet", methods=['POST'])
    def tweet():
        user_tweet = request.json
        tweet = user_tweet['tweet']

        if len(tweet) > 300:
            return '300자를 초과했습니다', 400

        insert_tweet(user_tweet)
        return '', 200


    @app.route("/timeline/<int:user_id>", methods=['GET'])
    def timeline(user_id):
        return jsonify({
            'user_id' : user_id,
            'timeline' : get_timeline(user_id)
        })



    return app



