/* This is my first c program */

#include <stdio.h>
#include "genlib.h"
#include "simpio.h"

int main()
{
    double no1, no2, sum;
   
    printf("Input 1st number: ");
    no1 = GetReal();

    printf("Input 2nd number: ");
    no2 = GetReal();

    sum = no1 + no2;
    printf("The sum of %f and %f is %f\n",no1, no2, sum);

    return 0;
}
