#include <stdio.h>

int main()
{
	int a = 10;
	while(a < 20)
	{
		if(a == 15)
		{
			// skip the iteration
			a++;
			continue;
		}
		printf("value of a: %d \n", a);
		a++;
	}
	return 0;
}
