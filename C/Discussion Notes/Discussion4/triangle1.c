// Chapter 4. 12
#include <stdio.h>
#include "genlib.h"
#include "simpio.h"

void printTriangle(int n);

int main()
{
	int n = 0;
	printf("Please input the number of Diamond lines: ");
	n = GetInteger();
	
	// Start print the full Triangle
	printTriangle(n);
}		

void printTriangle(int n)
{
	int i, j;
	for(i=0; i<n; i++)
	{
		for(j=0; j<n-i-1; j++)
		{
			printf(" ");
		}
		for(j=0; j<2*i+1; j++)
		{
			printf("*");
		}
		printf("\n");
	}
}
