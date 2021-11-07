'Conversor de unidades'
var = float(input('Digite uma distância em metros:  '))
print('A medida de {} corresponde a'.format(var))
print('{:.3f}km'.format(var/1000))
print('{:.2f}hm'.format(var/100))
print('{:.1f}dam'.format(var/10))
print('{:.0f}dm'.format(var*10))
print('{:.0f}cm'.format(var*100))
print('{:.0f}mm'.format(var*1000))
