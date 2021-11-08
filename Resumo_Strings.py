'String analisado'
frase = 'Curso em Vídeo Python'

'Selecionar elementos da string'
print(frase[2])

'Fatiamento da string, de um elemento x até o elemento y'
print(frase[2:12])

'Fatiamento inicial até o elemento selecionado ou elemento selecionado até o final'
print(frase[:10])
print(frase[10:])

'Fatiamento com um intervalo de captura, intervalo de 2'
print(frase[1:10:2])

'Escrita de um texto longo, aplicar 3*" '
print("""Text.app is a simple text editor for Chrome OS and Chrome.
It's fast,lets you open multiple files at once, has syntax highlighting,""")

'Contar quantos elementos existem dentro da string'
print(frase.count('o'))
print(frase.count('Curso'))

'Obtendo o tamanho da frase'
print(len(frase))

'Remoção de espaços, para retirada de espaços á direita, rstrip'
frase1 = "  curso"
print(len(frase1))
print(len(frase1.strip()))

'Trocando elementos da string'
print(frase.replace("Curso", "Aula"))

'Analisar se um elemento está dentro da string'
print('Curso' in frase) #True está contido na string, False não está

'Analisar a posição de um elemento na string'
print(frase.find("em"))

'Dividindo os elementos da string'
print(frase.split())

'Guardando os elementos de divisão da string'
divisao = frase.split()
print(divisao[0], divisao[1])

'Selecionando elementos dentro da divisão após o split'
print(divisao[1][1]) #primeiro elemento do split, primeiro elemento da divisão

'Como aumentar as letras ou diminuir'
print(frase.upper())
print(frase.lower())

'Como ajustar para deixar as inicias do string em minusculas'
print(frase.capitalize())
print(frase)

'Processo invertido do capitalize'
print(frase.title())
print(frase)

'Juntando os elementos de split com um novo elemento'
print('-'.join(frase.split()))