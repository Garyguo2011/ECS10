/* This is my first c program */

#include <stdio.h>
#include "genlib.h"
#include "simpio.h"

int main()
{
    int no1, no2, sum;
   
    printf("Input 1st number: ");
    no1 = GetInteger();

    printf("Input 2nd number: ");
    no2 = GetInteger();

    sum = no1 + no2;
    printf("The sum of %d and %d is %d\n",no1, no2, sum);

    return 0;
}
