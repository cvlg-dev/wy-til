// 사용자로부터 두개의 정수를 입력 받아서
// 두 정수를 포함하여 그 사이에 존재하는 정수들의 합을 계산해서
// 출력하는 프로그램을 작성하시오.
// 만약 첫 번째 입력되는 정수보다 두 번째 입력되는 정수가 작은 경우
// "두 번째 정수가 첫 번째 정수보다 커야 함"이라고 출력하고 다시 입력 받는다
// 두 개의 정수는 같은 값을 입력하지 ㅇ낳고 5이상 차이가 발생하도록 입력받고 출력합니다.


#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996)

int start;
int end;
int result = 0;


int main(void){

do {
    printf("첫 번째 정수 입력:");
    scanf("%d", &start);

    printf("두 번째 정수 입력:");
    scanf("%d", &end);

    if (start > end)
        printf("두 번째 정수가 첫 번째 정수보다 커야 함\n");
} while(start > end );

    for (; start <= end; start++)
        result += start;

    printf("입력된 두 정수를 포함한 사이의 합 : %d \n", result);
}