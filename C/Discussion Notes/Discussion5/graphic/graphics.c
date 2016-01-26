#include <stdio.h>
#include <math.h>
#include "graphics.h"

void DrawBox(double x, double y, double w, double h);
// for drawheart(x, y)indicate the start of the bottom point
// w represent the length of square side
void DrawHeart(double x, double y, double w);

int main()
{
	double w = 5;
	double h = 5;
	double offX = 1;
	double offY = 1;
	InitGraphics();

	DrawBox(offX, offY, w, h);

	DrawHeart(offX+w/2.0, offY+h/4.0, (w/4.0)*sqrt(2));

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

void DrawHeart(double x, double y, double w)
{
	MovePen(x, y);
	DrawLine(-w/sqrt(2), w/sqrt(2));
	MovePen(x, y);
	DrawLine(w/sqrt(2), w/sqrt(2));

	// Draw Arcs
	double w1 = w/sqrt(2.0);
	MovePen(x, y+2*w1);
	DrawArc(w/2.0, 45.0, 180.0);
	MovePen(x+w1, y+w1);
	DrawArc(w/2.0, -45.0, 180.0);
}


