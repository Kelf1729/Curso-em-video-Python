'Calcular a quantidade de Tinta'
height = float(input(("Digite a altura:  ")))
lenght = float(input("Digite a largura:  "))
print('A sua parede de {} x {} tem área de {:.2f}'.format(height, lenght, height*lenght))
print('Para pintar sua parede você vai precisar de {:.2f}L de tinta'.format((height*lenght)/2))