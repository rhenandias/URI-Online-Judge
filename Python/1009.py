# -*- coding: utf-8 -*
nome = input()
salario = float(input())
vendas = float(input())
total = salario + ((vendas * 15)/100)
print('TOTAL = R$ ' + '{0:.2f}'.format(total))