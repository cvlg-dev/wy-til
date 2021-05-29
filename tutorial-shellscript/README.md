# Shell script 101

## 1. basic syntax

### 1.1. 셸스크립트 작성

**1.1.1. 셸스크립트 작성 전**

셸스크립트를 만들 때는, 해당 파일이 셸스크립트라는 것을 알려주기 위해 파일 상단에 이를 명시한다.

- `myshell-01.sh`

```bash
#!/bin/bash

echo "hello world"
```

**1.1.2. 셸스크립트 실행**

해당파일을 실행할 때는 `sh` 명령어를 사용한다.

```shell
$ sh myshell-01.sh
```

### 1.2.  변수

#### 1.2.1. 변수 선언 후 `$`를 통한 변수 입력 

- `myshell-02.sh`

```bash
#!/bin/bash

language="Spanish"

echo "I can speak $language"
```

예제) 변수를 사용한 디렉토리 생성

- `make_directory.sh`

```bash
#!/bin/bash

language="korean english japanese"

mkdir $language
```

#### 1.2.2. 함수에서의 변수 사용

1. 함수에 전달되는 파라미터로서 변수를 선언할 수 있다.

- `myshell-03-1.sh`

```bash
#!/bin/bash

function print() {
    echo $1
}

print "I can speak Korean"
````

2. 전역 변수로서의 사용

- `myshell-03-2.sh`

```bash
#!/bin/bash

language="English"

function print() {
    echo "I can speak $language"
}

print
```

3. 지역 변수로서의 사용

- `myshell-03-3.sh`

```bash
#!/bin/bash

language="German"

function learn() {
    local learn_language="French"
    echo "I am learning $learn_language"
}

function print() {
    echo "I can speak $1"
}

learn
print $language
print $learn_language
```

#### 1.2.3. 예약 변수 / 환경 변수 (env variables)

이미 시스템에서 사용되고 있는 변수들이 있는데, 이를 예약변수 또는 환경 변수라고 함. 시스템의 환경정보를 확인할 경우 매우 유용함.

#### 1.2.4. 위치 매개변수 (positional parameters)

스크립트를 수행할 때 함께 딸려오는 파라미터를 위치 매개변수라고 함.

- `$0`
- `$1`
- `$*`
- `$@`
- `$#`

#### 1.2.5. 특수매개변수 (special parameters)

명령, 함수 또는 스크립트 실행이 정상적으로 수행되었는지 여부를 확인할 수 있는 변수의 모음

- `$$`
- `$?`
- `$!`
- `$-`


#### 1.2.6. `$*` 와  `$@`

- `$*` 
	- 스페이스를 기준으로 문자열을 파라미터로 인식. 큰 따옴표와 상관 없이 동작.
- `"$*"`
	- 매개변수 전체를 하나의 문자열로 인식
- `$@` : 
	- `$*`와 동일
- `"$@"` : 
	- 큰 따옴표 내의 매개변수를 하나의 문자열로 인식