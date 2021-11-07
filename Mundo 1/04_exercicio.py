"Criar um algoritmo que leia a entrada e de informações de tipo dessa variável"
var = input('Digite uma variável qualquer:  ')

print('O tipo de variável diigta é, {}'.format(type(var)))
print('Alguma coisa foi digitada na variável, {}'.format(bool(var)))
print('É um número: {}'.format(var.isnumeric()))
print('É alfabético: {}'.format(var.isalpha()))
print('É alfanumérico: {}'.format(var.isalnum()))
print('É maiusculo: {}'.format(var.isupper()))
print('É miniscula: {}'.format(var.islower()))

