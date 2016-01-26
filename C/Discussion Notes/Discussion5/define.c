#include <stdio.h>

#define TRUE 1
#define getMax(a, b) (a>b?a:b)
#define absdif(a,b) (a>b?(a-b):(b-a))

void func();

int main()
{
	int x = 1;
	if(x == TRUE)
		printf("true.\n");

	int notuse = 50;	
	int m_a = 10;
	int m_b = 15;
	int max = getMax(m_a, m_b);
	//int max = absdif(m_a, m_b);
	printf("max: %d\n", max);
	func();
	return 0;
}

//#undef TRUE
//#undef getMax

void func()
{
	int func_x = 1;
	if(func_x == TRUE)
		printf("true in the func.\n");
	int f_a = 10;
	int f_b = 15;
	int fmax = getMax(f_a,f_b);
	printf("fmax: %d\n", fmax);
}
