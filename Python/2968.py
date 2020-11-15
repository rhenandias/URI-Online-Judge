# -*- coding: utf-8 -* 
import math

v, n = [int(i) for i in input().split(' ', 2)]

total_placas = v * n
resultado = []
for i in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
	value = math.ceil((total_placas * i)/100)
	resultado.append(str(value))

print(' '.join(resultado))