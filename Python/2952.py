# -*- coding: utf-8 -*-
import itertools as it
n_horas = int(input())
atividades = input().split(' ', n_horas)

beneficio = {
	'A' : -50,
	'C' : -13500,
	'S' : 200,
	'M' : 550,
	'P' : 13000,
	'K' : -20,
	'B' : 40,
	'N' : 0
}

impactos = [beneficio[i] for i in atividades]

acc = []
for i in range(n_horas):
	new_list = impactos[i:]
	for n in list(it.accumulate(new_list)):
		if n != 0: acc.append(n)

print(str(max(acc)) + ' ' + str(min(acc)))