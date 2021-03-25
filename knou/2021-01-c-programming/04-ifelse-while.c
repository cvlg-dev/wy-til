#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)

int main(void) {
    // // 단순 if
    // int a=10, b=20;
    // if(a>b) {
    //     a = a+20;
    //     printf("a=%d\n", a);
    // }
    // b = b+20;
    // printf("b=%d\n", b);

    // // if-else
    // int a, b, max;
    // scanf("%d %d", &a, &b);
    // if(a >= b)
    //     max = a;
    // else
    //     max = b;
    // printf("max = %d\n", max);

    // // 다중 if-else
    // int a;
    // scanf("%d", &a);
    // if(a>=0)
    //     if(a==0)
    //         printf("입력된 값은 0\n");
    //     else
    //         printf("입력된 값은 양수\n");
    // else
    //     printf("입력된 값은 음수\n");

    // // 다중 if-else if-else
    // int score=0;
    // printf("성적 입력:");
    // scanf("%d", &score);
    // if(score >= 90)
    //     printf("학점은 A\n");
    // else if(score >= 80)
    //     printf("학점은 B\n");
    // else if(score >= 70)
    //     printf("학점은 C\n");
    // else if(score >= 60)
    //     printf("학점은 D\n");
    // else 
    //     printf("학점은 F\n");

    // // switch-case
    // int n;
    // printf("n=?");
    // scanf("%d", &n);
    // printf("\n n %% 5 = %d\n", n%5);
    // switch(n%5){
    //     case 0: printf("나머지는 0\n");
    //     break;
    //     case 1: printf("나머지는 1\n");
    //     break;
    //     case 2: printf("나머지는 2\n");
    //     break;
    //     default: printf("나머지는 3이나 4\n");
    //     break;
    // }

    // // goto
    // int i, n, c = 'A';
    // while(1){
    //     printf("\n 횟수는?");
    //     scanf("%d", &n);
    //     for(i=1; i<=n; i++) {
    //         printf("%c", c);
    //         if(c=='Q')
    //             goto end;
    //         c++;
    //     }
    // }
    // end:
    // printf("\n\n 끝");

    // // for
    // int i, sum=0;
    // for(i=0; i<=10; ++i)
    //     sum=sum+i;
    // printf("1부터 %d까지의 합=%d\n", i-1, sum);

    //  // 다중 for
    //  int a, b;
    //  for(a=1; a<=3; ++a){
    //      printf("a=%d\n", a);
    //      for(b=0; b<=4; b++)
    //          printf("b=%d ", b);
    //     putchar('\n');
    //  }

    // // while
    // int i=0;
    // int sum=0;
    // while(i<=100){
    //     sum=sum+i;
    //     i++;
    // }
    // printf("1부터 100까지의 합=%d\n", sum);

    // // 다중 while
    // int i=2, j=0;
    // while(i<10){
    //     j=1;
    //     while(j<10){
    //         printf("%d x %d = %d\n", i, j, i*j);
    //         j++;
    //     }
    //     printf("\n");
    //     i++;
    // }

    // // do ~ while
    // int i=0, n;
    // int sum=0;
    // printf("n=?");
    // scanf("%d", &n);
    // do{
    //     sum = sum+i;
    //     i++;
    // } while(i<=n);
    // printf("i%d\n", i);
    // printf("i ~ %d까지 합 = %d\n", n, sum);

    // // break
    // int num, sum=0;
    // while(1){
    //     printf("num(끝:0)...?");
    //     scanf("%d", &num);
    //     if(num==0)
    //         break;
    //     sum=sum+num;
    // }
    // printf("\n sum=%d", sum);

    // // continue
    // int num=1;
    // while(num!=0){
    //     printf("\n num=?");
    //     scanf("%d", &num);
    //     if(num<0){
    //         printf("0: Negative number !\n");
    //         continue;
    //     }
    //     printf("Square root of %d = %f\n", num, sqrt(num));
    // }
    // printf("\n\n The end\n");
}