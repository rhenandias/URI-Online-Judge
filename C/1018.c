#include <stdlib.h>
#include <stdio.h>

int main(){

	unsigned int value, hold_value;
	int bills[] = {100, 50, 20, 10, 5, 2, 1};
	int amount[7];

	scanf("%d", &value);
	hold_value = value;

	for(int i = 0; i < 7; i++){
		amount[i] = value / bills[i];
		value -= amount[i] * bills[i];
	}

	printf("%d\n", hold_value);
	for(int i = 0; i < 7; i++){
		printf("%d nota(s) de R$ %d,00\n", amount[i], bills[i]);
	}

	return 0;
}
