#include <stdio.h>
int main(void){
    int a=10;
    static int b=20;
    {
        int a=5;
        b=a+10;
    }
    printf("a=%d b=%d\n", a, b);
}