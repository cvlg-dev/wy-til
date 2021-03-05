#include <stdio.h>

int main() {
    
    // 이항 연산
    int x, y;
    x = 10;
    y = 3;
    printf("x + y = %d\n", x+y);
    printf("x / y = %d\n", x / y);
    printf("x % % x = %d\n", x % y);   // % modulo 연산을 출력하기 위해 문자를 2개 연속 사용
    printf("y % % y = %d\n", x % y);


    // 단항 연산
    int x=5, a, b;
    a = ++x;
    b = --x;
    b = x * 10;
    printf("a=%d b=%d x=%d\n", a, b, x);

    // 관계연산자
    int a = 4, b, c, d;
    b = a > 2;
    printf("b=%d\n", b);
    c = a<2;
    printf("c=%d\n", c);
    d = a==4;
    printf("d=%d\n", d);

    // 논리연산자
    int a=4, b=7, c, d, e;
    c= a>2 && b<=7;
    printf("c=%d\n", c);
    d=a<2 || b<=7;
    printf("d=%d\n", d);
    e= !a;
    printf("e=%d\n", e);

    // 대입연산자
    int a=10, b=3, c=1;
    a *= (b-1);
    b /= 2+3;
    c += 2;
    printf("c=%d b=%d c=%d\n", a, b, c);

    // 조건 연산자
    int a=10, b;
    b = (a>15)? (a+1):(a-1);
    printf("b=%d\n", b);
    return 0;
}