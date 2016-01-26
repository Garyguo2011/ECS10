#include <stdio.h>

int GCD(int m, int n);
int LCM(int m, int n);

int main()
{
	int num0 = 0;
	int num1 = 0;
	printf("Please enter number 0: ");
	num0 = GetInteger();
	printf("Please enter number 1: ");
	num1 = GetInteger();
	int lcm = LCM(num0, num1);
	printf("The lease common multiple is: %d \n", lcm);
	
	return 0;
}

int GCD(int m, int n)
{
	int a = m;
	int b = n;
	int temp = 0;
	if(a < b)
	{
		temp = a;
		a = b;
		b = temp;
	}
	// make sure that a > b
	while (b != 0)
	{
		temp = b;
		b = a%b;
		a = temp; 
	}
	return a;
}

int LCM(int m, int n)
{
	return m*n/GCD(m, n);
}
