#include <stdio.h>
 
int main() 
{
	int i = 0;
	int j = 0; 
   	int k = 0;
	for(i = 0; i < 10; i++) {
        	if (i != 5) {
			break;
		}
        	printf("%d \n", i);       //what will happen? will it print something?
    	}
 
    	printf("\n");
 

	// What should we do if we want to 
	// break the outside loop when k == 3?
    	for(j = 0; j < 2; j++) {
        for (k = 0; k < 5; k++) {   //only this loop is affected by break
            if (k == 3) {
				break;
			}
			printf("%d %d \n", j, k); //break once k==3
        }
    }
}
