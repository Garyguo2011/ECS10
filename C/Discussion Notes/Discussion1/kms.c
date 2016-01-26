//ECS30  Week 1 Discussion section DEMO

#include <stdio.h>
#include "genlib.h"
#include "simpio.h"

#define KMS_PER_MILE 1.609

int main()
{
    double miles;
    double kms;

    printf("Enter the distance in miles> ");
    miles = GetReal();

    kms = KMS_PER_MILE * miles;
    printf("That equals %g kilometers.\n", kms);

    return 0;
}
