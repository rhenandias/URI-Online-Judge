#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(){

	int time, vel, km;
	float liters;

	scanf("%d", &time);
	scanf("%d", &vel);

	km = time * vel;
	liters = km / 12.0;	
	
	printf("%.3f\n", liters);

	return 0;
}
