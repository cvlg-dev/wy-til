#include <stdio.h>

int main(void){
    int a, b, sum = 0;
    for (a=0; a<10; a++)
        for (b=5; b>1; b--)
            sum+=1;
            printf("%d", sum);
}