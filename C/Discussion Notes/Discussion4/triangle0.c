// Chapter 4.11
#include <stdio.h>
#include "genlib.h"
#include "simpio.h"

void printTriangle(int n);

int main()
{
	int n = 0;
	printf("Please input the number of Diamond lines: ");
	n = GetInteger();
	
	// Start print the half Triangle
	printTriangle(n);
}		

void printTriangle(int n)
{
	int i, j;
	for(i=0; i<n; i++)
	{
		for(j=0; j<=i; j++)
		{
			printf("*");
		}
		printf("\n");
	}
}
