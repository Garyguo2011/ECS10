/* Program testing the probability of a defect assuming 1 in every 1000 pieces is defective*/

#include<stdio.h>
#include "genlib.h"
#include "random.h"

main()
{

printf("Testing a random sample\n");
Randomize();
if(RandomChance(0.001))
{
printf("Defect found\n");
}
else
{
printf("Not a defective piece\n");
}
}

