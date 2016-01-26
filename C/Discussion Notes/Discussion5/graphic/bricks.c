#include <stdio.h>
#include <math.h>
#include "graphics.h"

void DrawBox(double x, double y, double w, double h);

int main()
{
	double w = 5;
	double h = 5;
	double offX = 1;
	double offY = 1;
	InitGraphics();

	DrawBox(offX, offY, w, h);
	offX += 1;
	offY += 1;

	int i = 0;
	int j = 0;
	double sizew = 0.5;
	double sizeh = 0.25;
	for(i=0; i<6; i++)
	{
		for(j=0; j<6-i; j++)
		{
			DrawBox(offX+(double)j*sizew, offY+(double)i*sizeh, sizew, sizeh);
		}
		offX += sizew/2.0;
	}

	return 0;
}

void DrawBox(double x, double y, double w, double h)
{
	MovePen(x, y);
	DrawLine(0, h);
	DrawLine(w, 0);
	DrawLine(0, -h);
	DrawLine(-w, 0);
}

