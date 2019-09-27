# -*- coding: utf-8 -*
#codigo da peça, número de peças, valor unitário
c1, n1, v1 = input().split(' ', 3)
c2, n2, v2 = input().split(' ', 3)
print('VALOR A PAGAR: R$ ' + '{0:.2f}'.format(int(n1) * float(v1) + int(n2) * float(v2)))
