"""Refazer a tabuada"""

number = int(input('Digite o valor para a tabuada:  '))
print('-'*12)

for i in range(1,11):
    print('{} x {} = {}'.format(i, number, i*number))

print('-'*12)