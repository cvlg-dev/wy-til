

## Create database

- User

```sql
CREATE TABLE users
(
    id                  INT             NOT NULL    PRIMARY KEY     IDENTITY,
    name                VARCHAR(255)    NOT NULL,
    email               VARCHAR(255)    NOT NULL    UNIQUE ,
    hashed_password     VARCHAR(255)    NOT NULL,
    profile             VARCHAR(2000)   NOT NULL,
    created_at          DATETIME        NOT NULL    DEFAULT GETDATE()
) go
```

- user follow list

```sql
create table user_follow_list
(
	user_id int not null
		constraint users_follow_list_user_id_fkey
			references users,
	follow_user_id int not null
		constraint users_follow_list_follow_user_id_fkey
			references users,
	create_at datetime default GETDATE() not null,
	constraint user_follow_list_pk
		primary key nonclustered (user_id, follow_user_id)
) go
```

- tweet

```sql
CREATE TABLE tweets
(
    id                  INT             NOT NULL    IDENTITY    PRIMARY KEY ,
    user_id             INT             NOT NULL,
    tweet               VARCHAR(300)    NOT NULL,
    created_at          DATETIME        NOT NULL    DEFAULT GETDATE(),
    CONSTRAINT tweets_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(id)
);
```


## SQLAlchemy

- SQLAlchemy는 ORM(Object Relational Mapper)
    - RDBMS의 테이블들을 파이썬언어의 클래스로 표현할 수 있게 해주는 매퍼
    

