#include <stdio.h>

// global variables are visible and accessible by all functions
int var_global = 10;

void func1(int arg1, int arg2)
{
	// a function can access any variable it declares
	int result = 0;
	// access all of its arguments
	result = arg1 + arg2;
	// access the global variable
	result = result * var_global;
	printf("func1's result = %d\n", result);
}

void func2()
{
	// different functions can declare variables with same name
	// unique scope
	int result = 15;
	printf("func2's result = %d\n", result);
}

void hiding()
{
	// if a function declares a variable that has the same name
	// as a global variable
	// that global variable becomes inaccessible inside this function
	// Variable Hiding
	int var_global = 99;
	printf("hiding func's var_global = %d\n", var_global);
}

/*void wrong()
{
	// a function cannot access another function's variables or arguments
	func1(arg1, arg2);
}*/

int main()
{
	func1(15, 27);
	func2();
	hiding();
	//wrong();
	return 0;
}
