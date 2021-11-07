'Calcular seno e cosseno de ângulos'
import math
angle = float(input('Digite o ângulo:  '))
degree = math.radians(angle)
print('Seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(math.cos(degree), math.sin(degree), math.tan(degree)))