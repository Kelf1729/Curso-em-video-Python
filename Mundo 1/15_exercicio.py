days = int(input('Digite quantos dias o carro foi usado:  '))
km = float(input('Digite quantos km foram rodados:  '))
print('O total a pagar é de R$ {:.2f}'.format(days*60 + km*0.15))
