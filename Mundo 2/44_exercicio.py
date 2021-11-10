"""Criar um programa que calcula o valor a ser pago pelo consumidor
Considerando os seguintes fatores
* À vista dinheiro/cheque: 10% de desconto
* À vista no cartão: 5% de desconto
* Em até 2x no cartão: preço normal
* 3x ou mais no cartão: 20% de juros"""

price = float(input("Digite o valor do produto:  "))
pay = str(input('A forma de pagamento será\n'
                '1 - À vista dinheiro/cheque\n'
                '2 - À vista no cartão\n'
                '3 - Em até 2x no cartão\n'
                '4 - 3x ou mais no cartão\n'))

if pay == '1':
    print('O produto que custa R$ {:.2f}\n'
          'Fica por R$ {:.2f} com desconto de 10%'.format(price, price*0.9))
elif pay == '2':
    print('O produto que custa R$ {:.2f}\n'
          'Fica por R$ {:.2f} com desconto de 5%'.format(price, price*0.95))
elif pay == '3':
    print('O produto que custa R$ {:.2f}\n'
          'Fica por R$ {:.2f} sem desconto'.format(price, price))
elif pay =='4':
    print('O produto que custa R$ {:.2f}\n'
          'Fica por R$ {:.2f} com juros de 20%'.format(price, price*1.2))