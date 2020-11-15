# -*- coding: utf-8 -*
a, b, c = [float(i) for i in input().split(' ', 3)]

triangulo = (a * c) / 2
circulo = 3.14159 * c**2
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

print ('TRIANGULO: ' + '{0:.3f}'.format(triangulo))
print ('CIRCULO: ' + '{0:.3f}'.format(circulo))
print ('TRAPEZIO: ' + '{0:.3f}'.format(trapezio))
print ('QUADRADO: ' + '{0:.3f}'.format(quadrado))
print ('RETANGULO: ' + '{0:.3f}'.format(retangulo))