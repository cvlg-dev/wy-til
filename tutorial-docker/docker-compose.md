# Docker Compose


- 도커 명령어를 통한 작업은 실수가 발생할 수 있는데, 도커 컴포즈는 이 문제를 해결할 수 있는 간결한 방법을 제시함
- 도커 컴포즈는 기본적으로 docker for mac을 설치할 때 함께 설치됨 (리눅스의 경우 그러하지 않기 때문에 따로 설치가 필요함)

	- 리눅스의 설치

		```
		$ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
		$ sudo chmod +x /usr/local/bin/docker-compose
		```
- 설치 버전 확인하기
	
	```
	$ docker-compose version
	
	docker-compose version 1.28.5, build c4eb3a1f
	docker-py version: 4.4.4
	CPython version: 3.9.0
	OpenSSL version: OpenSSL 1.1.1h  22 Sep 2020
	```


## Yaml(.yml) 개념

- XML, JSON과 같이 시스템 사이에 데이터를 주고 받을 때 사용하는 포맷
	- XML 의 구조: 
		- key-value : `<key>value</key>`
		- array : 

			```
			<parent>
				<child1></child1>
				<child2></child2>
				<child3></child3>
			</parent>
			```
	- JSON 의 구조
		- key-value : `{key: value}`
		- array 

			```
			{key: 
				[array1], 
				[array2],
				[array3],
			}
			```
	- Yaml의 구조
		- key-value : `key: value`
		- array :  하이픈을 통해 array임을 구별

			```
			key : 
			- array1
			
			- array2
			...
			```

## 예제

### docker-compose.yml 파일 예제

```yml
# docker-compose.yml

version: '2'
services:
  db:
    image: mysql/mysql-server:8.0.15
    volumes: 
      - ./mysql:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: wordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
  wordpress:
    image: wordpress:latest
    volumes:
      - ./wp:/var/www/html
    ports:
      - "8000:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_USER: wordpress
```

### 실행

```
$ cd wp
$ docker compose up
```

## Reference

https://docs.docker.com/compose/reference/up/



