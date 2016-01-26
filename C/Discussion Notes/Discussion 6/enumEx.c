#include<stdio.h>
#include "genlib.h"
#include "strlib.h"

typedef enum 
        { 
          black_ops, 
          top_secret, 
          secret, 
          non_secret 
        }Security_levels;

int main() 
  { 
     Security_levels my_security_level = GetInteger(); 
 
     if ( my_security_level == black_ops ) 
       { 
          printf("Welcome\n"); 
          printf("open_safe\n");  
          printf("open_door\n"); 
       } 
    else if ( my_security_level == top_secret ) 
       { 
          printf("Welcome\n"); 
          printf("open_door\n");  
       } 
    else if ( my_security_level == secret ) 
       { 
          printf("Please leave Now\n"); 
       } 
    else if ( my_security_level == non_secret ) 
       { 
          printf("Warning, The Police have been Called\n"); 
          printf("Surrender yourself to them immediately!\n"); 
          //call_police(); 
       } 
 
    return 0; 
  } 
