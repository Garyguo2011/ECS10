#include <stdio.h>

void main()
{
    float x;
    double y;
    x = 4.5;
    y = 5.5;

    printf("x:  %f\n",x);
    printf("&x: %d\n", &x);

    printf("&y: %d\n", &y);

    float z = x;
    printf("z:  %f\n", z);
    printf("&z: %d\n", &z);

    float *w = &x;
    printf("w:  %d\n", w);
    printf("&w: %d\n", &w);
    printf("*w: %f\n", *w);

    *w = 10.89;
    printf("x:  %f\n",x);
    printf("*w: %f\n",*w);
    printf("z:  %f\n",z);

    float *t = w;
    printf("t:  %d\n", t);
    printf("&t: %d\n", &t);
    printf("*t: %f\n", *t);

}
