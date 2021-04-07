# Docker 기본 명령어

## 1.기초 명령어

### ls (또는 ps)

- `docker container ls (= docker ps)`
	- 실행 중인 컨테이넝
- `docker container ls -a`
	- 실행이 중지된 컨테이너까지 출력


### stop
```bash
docker stop [OPTIONS] CONTAINER [CONTAINER ... ]
```

- 실행 중인 컨테이너를 중지하는 명령어
- 실행 중인 컨테이너를 복수로 중지시킬 수도 있음


### rm
```bash
docker rm [OPTIONS] CONTAINER [CONTAINER ... ]
```

- 종료된 컨테이너를 삭제하는 명령어


### logs
```
docker logs [OPTIONS] CONTAINER
```
- 기본 옵션
	- `-f` : fetch. 새로고침 할 때마다 로그 발생 시 실시간으로 업데이트 됨
	- `--detail`: 가장 마지막 부분을 보여줌
- 컨테이너가 정상적으로 동작하는지 확인하는 좋은 방법 중 하나


### pull 

	```
	docker pull [OPTIONS] NAME[:TAG|@DIGEST]
	```
	- 도커 이미지 다운로드

### rmi

	```
	docker rmi [OPTIONS] IMAGE [IMAGE...]
	```
	- 도커 이미지 삭제
	- 단, 컨테이너가 실행중인 이미지는 삭제되지 않음.

## 2. run

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


## 3. exec

- 이미 실행중인 도커 컨테이너에 접속할 때 사용
- 컨테이너 안에 ssh server 등을 설치하지 않고 접속함.


## 4. network

```
docker network create [OPTIONS] NETWORK
```

- 도커 컨테이너끼리 이름으로 통신할 수 있는 가상 네트워크를 만듬


```
docker network connect [OPTIONS] NETWORK CONTAINER
```

- 기존에 생성된 컨테이너에 네트워크를 추가

## 5. volumn (-v)

- 호스트의 드라이브를 마운트 시키는 명령어
- 마운트된 드라이브 없이 컨테이너를 중지/삭제시키면 데이터가 날라가게 됨
- 따라서 데이터를 저장하고 싶다면, 드라이브를 볼륨으로 마운트시켜야 함.

```
-v [my own dir]:[container dir]
```



## 6. 예제

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
	mysql/mysql-server:8.0.15
	```	
	- mysql 패스워드를 입력하지 않겠다는 환경변수를 `-e`로 패스
	- `--name` : 컨테이너에 이름 설정
	- `-d` : 백그라운드로 실행

	- 실제로 실행을 해서 워드프레스용 DB를 생성함.
		- `docker exec -it mysql mysql`
			- mysql 이라는 컨테이너에서 mysql이라는 명령어를 실행
		```
		create database wp CHARACTER SET utf8;
		CREATE USER wp@'%' IDENTIFIED BY 'wp';
		GRANT ALL PRIVILEGES ON wp.* TO wp@'%' WITH GRANT OPTION;
		flush privileges;
		quit
		```
	
	
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
		
6. 네트워크

	```
	docker network create app-network
	```
	- app-network라는 이름으로 네트워크를 만듬 (wordpress - mysql을 연결)

	
	```
	docker network connect app-network mysql
	```
	- mysql 컨테이너에 네트워크를 추가

	
	```
	docker run -d -p 8080:80 \
	--network=app-network \
	 -e WORDPRESS_DB_HOST=mysql \
	 -e WORDPRESS_DB_NAME=wp \
	 -e WORDPRESS_DB_USER=wp \
	 -e WORDPRESS_DB_PASSWORD=wp \
	 wordpress
	```
	- 워드프레스는 이미지를 실행할 때 네트워크를 지정해볼 수 있음
	- network는 위에서 생성한 app-network를 지정하고, host는 mysql의 이름으로 접근함.

	```
	docker stop mysql
	docker rm mysql
	docker run -d -p 3306:3306 \
	-e MYSQL_ALLOW_EMPTY_PASSWORD=true \
	--network=app-network \
	--name mysql \
	-v /Users/wg/dvlp/Lucas/learn_container/volumn:/var/lib/mysql \
	mysql/mysql-server:8.0.15
	
	docker exec -it mysql mysql
	create database wp CHARACTER SET utf8;
	CREATE USER wp@'%' IDENTIFIED BY 'wp';
	GRANT ALL PRIVILEGES ON wp.* TO wp@'%' WITH GRANT OPTION;
	flush privileges;
	quit	
	```
	- 기존의 mysql 컨테이너를 삭제하고 volumn을 마운트 시켜 다시 띄움
	- 이 경우 mysql의 데이터베이스는 마운트된 디렉토리에 데이터가 남게 되므로, 나중에 다시 동일한 연결하더라도 데이터를 유지할 수 있음.		

## Reference

- [인프런 초보를 위한 도커 안내서](https://www.inflearn.com/course/%EB%8F%84%EC%BB%A4-%EC%9E%85%EB%AC%B8#)