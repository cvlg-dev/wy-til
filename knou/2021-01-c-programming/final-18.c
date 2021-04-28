#include <stdio.h>
int main(void) {
    static int a[ ]={10, 20, 30, 40, 50};
    int *pt, b, c;
    pt = a;
    b = *pt + *(pt+2);
    pt = pt+2;
    c = *pt + *(pt+2);
    printf("b=%d\n", b);
    printf("c=%d\n", c);
}