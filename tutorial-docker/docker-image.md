# Docker Image


## 도커 이미지
- 도커는 레이어드 파일 시스템 기반
- 도커 이미지는 프로세스가 실행되는 파일들의 집합 또는 환경이라고 할 수 있음
- 프로세스가 실행되면 발생하는 파일들에 대한 변경을 이미지에 쌓는 것


## 이미지

- 이미지는 두가지로 나뉠 수 있음
	- 읽기전용 Only Read
	- 쓰기가능 Writable
- Base Image
	- 읽기 전용
	- 수정할 수 없음
	- 대신 해당 이미지 위에 또 다른 층을 추가할 수 있음


### 예시 1) docker commit을 통해 이미지 만들기
**우분투 베이스 이미지에 Git을 설치하여 새로운 이미지로 저장하기**

1. 우분투 베이스 이미지에 Git 설치

	```
	docker pull ubuntu:latest
	docker run -it --name git ubuntu:latest bash
	apt-get update
	apt-get install -y git
	git --version
	# git version 2.25.1
	```

2. 변경이 생긴 베이스 이미지를 커밋하기
	
	- `docker commit`으로 이미지 만들기
		- `:git`이라는 태그를 붙여 새로운 이미지를 만듬
	
		```
		docker commit git ubuntu:git
		docker run -it --name git2 ubuntu:git bash
		```
## Dockerfile	

- Dockerfile 핵심 명령어
	- FROM : 베이스 이미지 지정
	- RUN : 쉘 명령어 실행 (도커 이미지를 만들기 위해 사용하는 명령여)
	- CMD : 컨테이너 기본 실행 명령어 (도커 컨테이너를 만들때, 실행할 때 사용하는 명령어)
	- EXPOSE : 컨테이너에서 사용하는 포트 정보
	- ENV : 환경변수 설정
	- ADD : 파일 도는 디렉토리 추가. (URL / ZIP 사용 가능)
	- COPY : 로컬에 있는 파일 또는 디렉토리를 복사하여 이미지 내에 추가
	- ENTRYPOINT : 컨테이너 기본 실행 명령어
	- VOLUMN : 외부 마운트포인트 생성
	- USER : RUN, CMD, ENTRYPOINT를 실행하는 사용자
	- WORKDIR : 작업 디렉토리 변경/설정
	- ARGS : 빌드타임 환경변수 설정
	- LABEL : key - value 데이터
	- ONBUILD : 다른 빌드의 베이스로 사용될 때 사용하는 명령어
	
	
- `docker build`로 이미지 만들기
	- 전체 명령어 규칙
		- `docker build -t {유저네임스페이스/이미지이름:태그} {빌드컨텍스트}`
		- `-t` : 이미지의 이름 지정
		- `-f` : Dockerfile의 위치가 다른 디렉토리라면 해당 옵션을 활용할 수 있음
	- 빌드컨텍스트
		- 현재 디렉토리일 경우 점(`.`)을 사용
		- 필용한 경우 다른 디렉토리를 지정할 수 있음

		
- `.dockerignore` 지정
	- `.gitignore`와 비슷한 역할을 함
	- 도커 빌드 컨텍스트에서 지정된 패턴의 파일을 무시함
	- 민감한 정보를 제외하는 용도로 사용됨
	- 빌드속도를 개선하기 위해 불필요한 파일을 제외하는 역할로도 사용됨
	- 빌드할 때 사용되는 파일을 `.dockerignore`에 포함시켜서는 안 됨

	
### 예시 2) Dockerfile과 docker build를 통해 이미지 만들기

- Dockerfile

	```dockerfile
	FROM ubuntu:latest
	RUN apt-get update
	RUN apt-get install -y git
	```	
- Dockerfile을 빌드

	```
	docker build -t ubuntu:git-dockerfile .
	```	
	
	
## 도커 이미지 만들기 실습

- Dockerfile

	```
	# 1. base image 정의
	FROM ubuntu:20.04
	RUN apt-get update
	
	
	# 2. node 설치
	## DEBIAN_FRONTEND=noninteractive
	## 
	RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs npm
	
	
	# 3. 현재 로컬 디렉토리에 있는 소스를 이미지 내 디렉토리에 복사
	COPY . /usr/src/app
	
	
	# 4. Nodejs 패키지 설치
	WORKDIR /usr/src/app    # 이동
	RUN npm install			# npm install 실행
	
	
	# 5. WEB 서버 실행 (Listen 포트 정의)
	EXPOSE 3000				# 포트 정보
	CMD node app.js			# 컨테이너에서 실행
	```
	
- .dockerignore

	```
	node_modules/*
	```	

- 빌드 시작

	```
	docker build -t webapp .
	```
	
	
- 빌드 된 도커 이미지 실행

	```
	docker run -p 3000:3000 webapp
	```
	
	
## Dockerfile 최적화 

### 예시 3) Dockerfile 최적화 하기

- Dockerfile

	```
	# 최적화 포인트1: 이미 node가 설치되어 있는 base image 정의
	FROM node:12
	
	# 최적화 포인트2: 패키지를 우선적으로 복사
	COPY .package* /usr/src/app/
	WORKDIR /usr/src/app
	RUN npm install
	
	
	COPY . /usr/src/app
	WORKDIR /usr/src/app
	
	EXPOSE 3000
	CMD node app.js
	```