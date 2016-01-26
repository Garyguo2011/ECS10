#include <stdio.h>
#include "genlib.h"
#include "simpio.h"

#include "test.h"

int main()
{
	double num;
	printf("Please input a number to calculate the square root: ");
	num = GetReal();
	printf("The input is %g. \n", num);
	double output = test1(num);
	printf("The square root is: %g. \n", output);
	return 0;
}
