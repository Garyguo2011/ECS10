/* Program simulating rolling a die using seed */

#include<stdio.h>
#include "genlib.h"
#include "random.h"

int RollDie(void);

main()
{

int i,NumberOfTrials;

printf("Enter the number of tries:\n");

NumberOfTrials = GetInteger();

        for(i=0;i<NumberOfTrials;i++)
        {
        printf("%d\n",RollDie());
        }
}

int RollDie(void)
{
	Randomize();        
	return(RandomInteger(1,6));
}

