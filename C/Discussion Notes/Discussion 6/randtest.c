#include<stdio.h>
#include "genlib.h"
#include "random.h"

#define NTrials 10

main()
{

int i,r;

printf(" On this computer RAND_MAX is : %d \n",RAND_MAX);
printf("Here are the results to %d calls of rand:\n",NTrials);

//Randomize();
for(i=0;i<NTrials;i++)
{
	
	r = rand();
	printf("%10d\n",r);
}
}
