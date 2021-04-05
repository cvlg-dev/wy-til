# Docker 기본 명령어

## 1. run

```bash
docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
```
- 기능
	- 컨테이너 실행
- 명령어
	- `-d` : detached mode (백그라운드 모드)
	- `-p` : 호스트와 컨테이너의 포트를 연결
	- `-v` : 호스트와 컨테이너의 디렉토리 연결
	- `-e` : 컨테이너 내에서 사용할 환경변수 설정
	- `--name` : 컨테이너 이름 설정
	- `--rm` : 프로세스 종료시 컨테이너 자동 제거
		- 이 옵션이 없다면, 컨테이너가 종료되더라도 삭제되지 않고 남아있어 수동으로 삭제해야 함.
	- `-it` : 사용자가 사용할 수 있는 터미널을 위한 옵션
		- `-i` : 입력을 가능하게 하기
		- `-t` : 터미널 띄우기
	- `--network` : 네트워크 연결
- 설명
	- run 명령어를 사용하면, 사용할 이미지가 이미 저장되어 있는지 확인 후, 없다면 pull한 뒤, 컨테이너를 create하고 start함 
		- 각각의 동작들은 각각의 명령어로도 따로 실행 가능함.
	- 컨테이너가 실행되지만, 별 다른 명령어를 전달하지 않으면, 생성되자마자 종료됨.
		- 컨테이너는 기본적으로 **프로세스**이기 때문에, 실행 중인 프로세스가 없으면 컨테이너는 종료됨.
		- 예시: `docker run ubuntu:20.04`


## 2. exec

- 이미 실행중인 도커 컨테이너에 접속할 때 사용
- 컨테이너 안에 ssh server 등을 설치하지 않고 접속함.



## 9. 예제

1. 우분투 이미지 컨테이너로 띄우기
	
	```
	 docker run --rm -it ubuntu:20.04 /bin/sh
	```
	- `/bin/sh` : sh를 실행함
	- `-it` : 키보드 입력
	- `--rm` : 프로세스 종료 후 컨테이너 자동 삭제

2. 웹 어플리케이션 실행
	
	```
	docker run --rm -p 5678:5678 hashicorp/http-echo -text="helllo world" 
	```
	- `-p` : 포트 연결 [호스트 포트]:[도커 내 포트]
	- `-text` : 웹 어플리케이션에 들어가는 변수 전달
	
3. Redis 실행하기 (메모리기반 데이터베이스)
	
	```
	docker run --rm -p 1234:6379 redis
	```	
	- 레디스 테스트 해보기

	```
	set hello world
	get hello
	quit
	```
4. MySQL 실행하기
	
	```
	docker run -d -p 3306:3306 \
	-e MYSQL_ALLOW_EMPTY_PASSWORD=true \
	--name mysql \
	mysql:5.7
	```	
	- mysql 패스워드를 입력하지 않겠다는 환경변수를 `-e`로 패스
	- `--name` : 컨테이너에 이름 설정
	- `-d` : 백그라운드로 실행

	- 실제로 실행을 하고자 한다면
		- `docker exec -it mysql mysql`
		- mysql 이라는 컨테이너에서 mysql이라는 명령어를 실행
	
5. 워드프레스 블로그 실행하기 (앞서 MySQL이 실행 중인 상태에서)
	
	```
	docker run -d -p 8080:80 \
	 -e WORDPRESS_DB_HOST=host.docker.internal \
	 -e WORDPRESS_DB_NAME=wp \
	 -e WORDPRESS_DB_USER=wp \
	 -e WORDPRESS_DB_PASSWORD=wp \
	 wordpress
	 ```
	 - 기존에 띄워져 있던 mysql 컨테이너의 데이터베이스를 이용해서 워드프레스 블로그를 띄움.
	