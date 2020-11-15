#include <stdlib.h>
#include <stdio.h>

int main(){

	unsigned int seg, hor, min;

	scanf("%d", &seg);

	hor = seg / 3600;
	min = (seg - hor * 3600) / 60;
	seg = (seg - (min * 60 + hor * 3600));

	printf("%d:%d:%d\n", hor, min, seg);

	return 0;
}
