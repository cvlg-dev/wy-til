// 사용자로부터 입력 받은 숫자에 해당하는 구구단을 출력하되
// 역순으로 출력하는 프로그램을 작성하시오
// while문을 사용하여 구구단을 출력합니다.


#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996)


int main(void){
    int num;
    int i = 9;

    do {
        printf("구구단(역순)을 실행할 단 : ");
        scanf("%d", &num);
        if (num > 9 || num < 1)
            printf("1~9 사이의 정수를 입력하시오\n");
    } while(num > 9 || num < 1);

    while (i > 0){
        printf("%d * %d = %d\n", num, i, num * i);
        i--;
    }
}