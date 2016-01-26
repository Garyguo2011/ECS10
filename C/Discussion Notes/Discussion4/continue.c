#include <stdio.h>
 
int main() 
{
	int i = 0;
	int j = 0;
	int k = 0;
    	for(i = 0; i < 10; i++) {
        	if (i == 5) {
			continue;
		}
        	printf("%d \n", i);       
		//this statement is skipped each time i == 5
    	}
 
    	printf("\n");
 
    	for(j = 0; j < 2; j++) {
        	for(k = 0; k < 5; k++) {
			//only this loop is affected by continue
            		if (k == 3)
			{
				continue;
			}
			printf("%d %d \n", j, k); 
			//this statement is skipped each time k==3
        }
    }
}
