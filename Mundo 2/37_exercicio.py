"""Criar um programa para receber um valor
e uma tabela para escolha da conversão desse número"""

number = int(input("Digite um valor inteiro:  "))
bases = str(input("Qual a base de conversão\n"
                  "-1 para binário\n"
                  "-2 para octal\n"
                  "-3 para hexadecimal\n"))

if bases == "1":
    print('O número {} em base binária é {}'.format(number, bin(number)))
elif bases == "2":
    print('O número {} em base octal é {}'.format(number, oct(number)))
else:
    print('O número {} em base octal é {}'.format(number, hex(number)))
