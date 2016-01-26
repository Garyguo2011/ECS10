#include <stdio.h>

void main()
{
    int a[5] = {1,2,3,4,5};
    int * p1;
    
    p1 = &a[1];

    printf("*p1: %d\n", *p1);
    p1++;
    printf("*p1: %d\n", *p1);
    p1--;
    printf("*p1: %d\n", *p1);

    *p1 = 0;
    printf("*p1: %d\n", *p1);
    printf("a[1]:%d\n", a[1]);
    a[1] = 2; // reset value back to original


    p1 = a; //same as p1 = &a[0]
    printf("*p1: %d\n", *p1);
    printf("a[0]:%d\n", a[0]);

   


}
