# Tutorial: Flask based API

_All code and resources are based on the tutorial_

## 1. 



## 2. 회원가입

- 실행하기
    - `FLASK_ENV=development FLASK_APP=app.py flask run`


## 2.1. `sign-up()`

### 2.1.1. `sign-up()` 함수

### 2.1.2. POST 요청 보내기

- cURL 로 POST 요청 보내기
  - `sign-up()` 함수에서 json의 형태로 request를 받는 것을 가정하기 때문에, cURL에서는 헤더(`--header` 또는 `-H`)에 `"Content-Type: application/json"`을 패스해야 함. 
  
  ```bash
  curl -v -X POST -d '{"name":"lucas", "email":"test@hello.co.kr", "password":"test1234"}' --header "Content-Type: application/json" http://127.0.0.1:5000/sign-up
  ```
  
  단, `-d`를 통해 데이터를 보낼 때는 `-X POST`가 이미 포함되어 있음을 가정하여, 생략이 가능함.
  
  ```bash
  curl -v -d '{"name":"lucas", "email":"test@hello.co.kr", "password":"test1234"}' --header "Content-Type: application/json" http://127.0.0.1:5000/sign-up
  ```

- httpie 로 POST 요청 보내기

  ```bash
  http -v POST localhost:5000/sign-up name=lucas email=test@hello.co.kr password=test1234
  ```

