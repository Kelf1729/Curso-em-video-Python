"Calculo de lados de um triângulo"
import math
cateto1 = float(input('Digite o cateto 1 :  '))
cateto2 = float(input('Digite o cateto 2 :  '))
print('O cateto1 {} o cateto2 {} e a hipotenusa é {}'.format(cateto1, cateto2, math.sqrt(cateto1**2 + cateto2**2)))