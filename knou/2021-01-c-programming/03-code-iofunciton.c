#include <stdio.h>
#pragma warning(disable:4996) // 권장하지 않는 함수 사용에 다한 경고 메세지 무시

int main() {

    // 출력 양식 변환기호
    printf("%c\n", 'a');
    printf("%d\n", -123);
    printf("%o\n", 123);
    printf("%x\n", 123);
    printf("%X\n", 123);
    printf("%f\n", 123.456789);
    printf("%e\n", 123.456789);
    printf("%s\n", "abcdefg");

    // 출력 양식 편집
    printf("|%d|\n", 123); // 숫자 길이만큼 출력 폭이 자동지정됨
    printf("|%5d|\n", 123); // 총 5자리로 오른쪽부터 채워짐
    printf("|%-5d|\n", 123); // 총 5자리로 왼쪽부터 채워짐
    printf("|%05d|\n", 123); // 총 5자리로 오른쪽부터 채워지고, 공백은 0으로 채워짐
    printf("|%6.1f|\n", 123.45); // 소수점 포함 총 6자리로 소수점 이하 1자리 까지만 출력함 
    printf("|%07.2f|\n", 123.45); // 소수점 포함 총 7자리로 소수점 이하 2자리 출력, 공백은 0으로 채움
    
    // printf
    char c='A';
    int i=10, j=10, k=30;    
    printf("간단한 출력 프로그램\n");
    printf("c=%c, c의 아스키 코드값은 %d\n", c, c);
    printf("i=%d, j=%d, k=%d\n", i, j, k);

    // putchar
    char var='A';
    putchar(var);  // 변수 사용 가능
    putchar(var+1); // 변수를 사용한 수식 사용 가능
    putchar('\n');
    putchar('K');  // 문자 사용 가능
    putchar('K'+2); // 문자를 사용한 수식 사용 가능
    putchar('\007'); // 예외문자 사용 가능

    // puts
    char s1[]="Computer";
    char s2[]="Science";
    puts(s1);
    puts(s2);
    printf("%s", s1);
    printf("%s\n", s2);

    // scanf
    int jsu1, jsu2;
    float ssu1, ssu2;
    printf("\n정수를 입력하시오");
    scanf("%d %d", &jsu1, &jsu2);  // 스페이스 공백으로 두 입력 자료를 구별함
    printf("\n실수를 입력하시오");
    scanf("%f %f", &ssu1, &ssu2);
    printf("\n정수는 %d %d\n", jsu1, jsu2);
    printf("실수는 %f %f\n", ssu1, ssu2);

    // getchar
    char a;
    printf("문자 하나를 입력하세요\n");
    a=getchar();
    printf("a=%c\n", a);

    // gets
    char s[50]; //문자열 저장을 위해 배열명 s인 배열 선언
    printf("문자열 입력?");
    gets(s);  // gets로 키보드에서 문자열을 받아들임
    printf("gets()로 문자열 입력= %s\n", s);
    printf("\n문자열 입력?");
    scanf("%s", s);  // scanf로 받아들임
    printf("scanf()로 문자열 입력= %s\n", s);

    return 0;
}