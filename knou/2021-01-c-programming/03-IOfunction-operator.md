

# 1. 표준 입출력 함수

C언어에서의 함수

- 종류
  - 표준함수: C언어 자체에서 제공하는 함수
  - 사용자 정의 함수: 사용자가 정의하여 사용하는 함수
- 특이점
  - C언어에서는 괄호를 열고 닫음으로서 함수를 정의. 괄호 안에 변수 등을 위치



## 1.1. 표준 출력함수

- 표준 출력함수의 종류
  - `printf()` : 화면에 여러 종류의 자료를 출력
  - `putchar()` : 화면에 1개의 문자를 출력
  - `puts()` : 화면에 문자열을 출력

### 1.1.1. `printf()`

- 형식
  - `printf("출력양식", 변수1, 변수2, ...);`
- 기능
  - 주어진 출력양식으로 자료를 출력

사용 예

```c
#include <stdio.h>

void main() {
  char c='A';
  int i=10, j=10, k=30;
  printf("간단한 출력 프로그램\n");
  printf("c=%c, c의 아스키 코드값은 %d\n", c, c);
  printf("i=%d, j=%d, k=%d\n", i, j, k);
}
```

### 1.1.2. `putchar()`

- 형식
  - `puthcar(문자);`
- 기능
  - 한 문자를 화면에 출력한다.

사용 예

```c
#include <stdio.h>

void main() {
  char var='A';
	putchar(var);
  putchar(var+1);
  putchar('\n');
  putchar('K');
  putchar('K'+2);
  putchar('\007');
}
```

```c
AB
KM
```



### 1.1.3. `puts()`

- 형식
  - `puts(변수)`
- 기능
  - 문자열을 화면에 출력한다
  - 메모리가 미리 확보되어 있어야 함
  - `\n` 을 사용하지 않아도 자동으로 줄이 바뀌어 출력됨

사용 예

```c
#include <stdio.h>

void main() {
  char s1[]="Computer";
  char s2[]="Science";
  puts(s1);
  puts(s2);
  printf("%s", s1);
  printf("%s", s2);
}
```

```
    Computer
    Science
    ComputerScience
```







## 1.2. 출력 양식

### 1.2.1. 변환기호

![](https://github.com/cvlg-dev/wy-til/blob/main/anything-python/xlsxwriter/resource/03-01.png)

```c
void main() {
    // 출력 양식 변환기호
    printf("%c\n", 'a');
    printf("%d\n", -123);
    printf("%o\n", 123);
    printf("%x\n", 123);
    printf("%X\n", 123);
    printf("%f\n", 123.456789);
    printf("%e\n", 123.456789);
    printf("%s\n", "abcdefg");
}
```

```
    a
    -123
    173
    7b
    7B
    123.456789
    1.234568e+02
    abcdefg
```

### 1.2.2. 출력양식 편집

```c
void main() {
    // 출력 양식 편집
    printf("|%d|\n", 123); // 숫자 길이만큼 출력 폭이 자동지정됨
    printf("|%5d|\n", 123); // 총 5자리로 오른쪽부터 채워짐
    printf("|%-5d|\n", 123); // 총 5자리로 왼쪽부터 채워짐
    printf("|%05d|\n", 123); // 총 5자리로 오른쪽부터 채워지고, 공백은 0으로 채워짐
    printf("|%6.1f|\n", 123.45); // 소수점 포함 총 6자리로 소수점 이하 1자리 까지만 출력함 
    printf("|%07.2f|\n", 123.45); // 소수점 포함 총 7자리로 소수점 이하 2자리 출력, 공백은 0으로 채움
}
```

```
    |123|
    |  123|
    |123  |
    |00123|
    | 123.5|
    |0123.45|
```



## 1.3. 표준 입력함수

### 1.3.1. 표준 입력함수의 종류

- scanf() : 키보들르 통해 여러 종류의 자료를 입력 받음 (모든 자료를 받아들일 수 있음)
- getchar() : 키보드를 통해 1개의 문자를 입력 받음
- gets() : 키보드를 통해 문자열을 입력받음

### 1.3.2. `scanf()`

- 형식
  - `scanf("입력양식", &변수1, &변수2, ...);`
- 기능
  - 주어진 양식으로 자료를 입력 받아 지정된 기억공간(변수)에 저장함

사용 예

```c
#include <stdio.h>
#pragma warning(disable:4996) // 권장하지 않는 함수 사용에 다한 경고 메세지 무시

void main() {
  inf jsu1, jsu2;
  float ssu1, ssu2;
  printf("\n정수를 입력하시오");
  scanf("%d %d", &jsu1, &jsu2);
  printf("\n실수를 입력하시오");
  scanf("%f %f", &ssu1, &ssu2);
  printf("\n정수는 %d %d\n", &jsu1, &jsu2);
  printf("\n실수는 %f %f\n", &ssu1, &ssu2);
}
```

```
    정수를 입력하시오12345 978
    실수를 입력하시오0.3890475 9999.47865

    정수는 12345 978
    실수는 0.389048 9999.478516
```



### 1.3.3. `getchar()`

- 형식
  - getchar();
- 기능
  - 한 문자를 키보드를 통해 입력 받는다.

사용 예

```c
#include <stdio.h>

void main() {
  char a;
  printf("문자 하나를 입력하세요\n");
  a=getchar();
  printf("a=%c\n", a);
}
```

```
    문자 하나를 입력하세요
    S
    a=S
```



### 1.3.4. `gets()`

- 형식
  - `gets(변수);`
- 기능
  - 문자열을 키보드로부터 입력 받는다.
  - 메모리에 공간을 미리 확보가 필요함

사용 예

```c
#include <stdio.h>

void main() {
  char s[50]; //문자열 저장을 위해 배열명 s인 배열 선언
  printf("문자열 입력?");
  gets(s);  // gets로 키보드에서 문자열을 받아들임
  printf("gets()로 문자열 입력= %s\n", s);
  printf("\n문자열 입력?");
  scanf("%s", s);  // scanf로 받아들임
  printf("scanf()로 문자열 입력= %s\n", s);
}
```

```
    문자열 입력?컴퓨터 과학과
    gets()로 문자열 입력= 컴퓨터 과학과

    문자열 입력?컴퓨터 과학과
    scanf()로 문자열 입력= 컴퓨터
```



## 1.4. 입력 양식

### 1.4.1. 입력양식 변환기호

![](https://github.com/cvlg-dev/wy-til/blob/main/anything-python/xlsxwriter/resource/03-02.png)



# 2. 연산자

- 임의의 자료에 대해 각종 연산을 수행하도록 하는 기호
- 종류
  - 산술 연산자
  - 관계 연산자
  - 논리 연산자
  - 대입 연산자
  - 조건 연산자
  - 조건 연산자
  - 비트 연산자
  - 기타 연산자

## 2.1. 산술 연산자

- 피 연산자에 대해 사칙연산을 포함한 각종 산술연산을 수행하는 연산자

### 2.1.1. 이항연산자

- `+ `
- `- `
- `/ `
- `* `
- `%` - modulo

```c
#include <stdio.h>

void main() {
    int x, y;
    x = 10;
    y = 3;

    printf("x + y = %d\n", x+y);
    printf("x / y = %d\n", x / y);
    printf("x % % x = %d\n", x % y);   // % modulo 연산을 출력하기 위해 문자를 2개 연속 사용
    printf("y % % y = %d\n", x % y);
}
```



### 2.1.2. 단항연산자

- `++`
- `--`

```c
#include <stdio.h>

void main() {
    int x=5, a, b;
    a = ++x;
    b = --x;
    b = x * 10;
    printf("a=%d b=%d x=%d", a, b, x);
}
```

```
		a=6 b=50 x=5
```





## 2.2. 관계 연산자

- `==`
- `!=`
- `>, >=, <, <=`

```c
#include <stdio.h>

void main() {
    int a = 4, b, c, d;
    b = a > 2;
    printf("b=%d\n", b);
    c = a<2;
    printf("c=%d\n", c);
    d = a==4;
    printf("d=%d\n", d);
}
```

```
		b=1
		c=0
		d=1
```



## 2.3. 논리 연산자

- `&&` : 논리곱 AND
- `||` : 논리합 OR
- `!` : 논리부정 NOT

```c
#include <stdio.h>

void main() {
    int a=4, b=7, c, d, e;
    c= a>2 && b<=7;
    printf("c=%d\n", c);
    d=a<2 || b<=7;
    printf("d=%d\n", d);
    e= !a;
    printf("e=%d\n", e);
}
```

```
    c=1
    d=1
    e=0
```



## 2.4. 대입 연산자

- 연산자의 오른쪽을 왼쪽에 대입하는데 사용
- 단축효과를 볼 수 있음

>- `=`
>- `+=, -=, *=, /=`
>- `%=`
>- `&=` : AND연산
>- `|=` : OR연산
>- `^=` : XOR연산
>- `<<=` : 왼쪽으로 이동 후 결과 대입
>- `>>=` : 오른쪽으로 이동 후 결과 대입

```c
#include <stdio.h>

void main() {
    int a=10, b=3, c=1;
    a *= (b-1);
    b /= 2+3;
    c += 2;
    printf("c=%d b=%d c=%d\n", a, b, c);
}
```

```c
		c=20 b=0 c=3
```



## 2.5. 조건 연산자

- 주어진 조건의 만족 여부에 따라 지정된 수식을 수행하는 연산자
- 형식
  - `(조건)? 수식1: 수식2;`
- 기능
  - 조건이 성립하면(참이면) - 수식1 수행
  - 조건이 성립하지 않으면(거짓이면) - 수식2 수행

```c
#include <stdio.h>

void main() {
    int a=10, b;
    b = (a>15)? (a+1):(a-1);
    printf("b=-%d\n", b);
}
```

```
		b=9
```



## 2.6. 비트 연산자

- 수치에 대해 bit단위의 연산을 수행하는 연산자

![](https://github.com/cvlg-dev/wy-til/blob/main/anything-python/xlsxwriter/resource/03-03.png)

|        |      |      |      |      |      |      |      |      |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| x      | 1    | 0    | 1    | 1    | 0    | 0    | 1    | 1    |
| y      | 0    | 1    | 0    | 0    | 1    | 0    | 0    | 1    |
| x & y  | 0    | 0    | 0    | 0    | 0    | 0    | 0    | 1    |
| x \| y | 1    | 1    | 1    | 1    | 1    | 0    | 1    | 1    |
| x ^ y  | 1    | 1    | 1    | 1    | 1    | 0    | 1    | 0    |
| ~x     | 0    | 1    | 0    | 0    | 1    | 1    | 0    | 0    |
| x<<2   | 1    | 1    | 0    | 0    | 1    | 1    | 0    | 0    |
| x>>2   | 0    | 0    | 1    | 0    | 1    | 1    | 0    | 0    |



## 2.7. 기타 연산자

- `sizeof()` : 변수가 차지하는 메모리의 크기
  - `sizeof(a)`
- `cast(형변환)` : 지정한 자료형을 다른 자료형으로 강제적으로 바꿈
  - `(float) a / b`
  - `(double) c`
- `&` : 주소 연산자로서 피 연산자의 주소를 나타냄
- `*` : 내용 연산자로서 피 연산자의 내용을 가져옴





## 2.8. 연산자 우선순위

![](https://github.com/cvlg-dev/wy-til/blob/main/anything-python/xlsxwriter/resource/03-04.png)

