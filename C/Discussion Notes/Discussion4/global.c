#include <stdio.h>

#define PI 3.14

double num_global; // this variable is global

void set_NumGlobal(double val);
void increase_NumGlobal(double increment);
void print_Num();

int main()
{
	set_NumGlobal(PI);
	print_Num();
	increase_NumGlobal(3.14);
	print_Num();
	set_NumGlobal(0.5);
	print_Num();
	return;
}

void set_NumGlobal(double val)
{
	num_global = val;
}

void increase_NumGlobal(double increment)
{
	num_global += increment;
}

void print_Num()
{
	printf("num_global is now: %g\n", num_global);
}
