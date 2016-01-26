#include <stdio.h>
#include <math.h>
#include "test.h"

double test1(double arg1)
{
	double result = sqrt(arg1);
	printf("test1: %g\n", result);
	return result;
}
