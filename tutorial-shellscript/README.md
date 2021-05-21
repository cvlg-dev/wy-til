# Shell script 101

## 1. basic syntax

### 1.1. 셸스크립트 작성

**1.1.1. 셸스크립트 작성 전**

셸스크립트를 만들 때는, 해당 파일이 셸스크립트라는 것을 알려주기 위해 파일 상단에 이를 명시한다.

```bash
#!/bin/bash

echo "hello world"
```

**1.1.2. 셸스크립트 실행**

해당파일을 실행할 때는 `sh` 명령어를 사용한다.

```bash
sh myshell-01.sh
```

### 1.2.  변수의 사용

**1.2.1. 변수 선언 후 `$`를 통한 변수 입력** 

```bash
#!/bin/bash

language="Spanish"

echo "I can speak $language"
```



