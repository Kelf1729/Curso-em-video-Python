"""Criar um programa que calcula a aprovação
de um aluno, sendo as condições
* Média abaixo de 5, reprovado
* Média entre 5 e 6.9 recuperação
* Média maior que 7 aprovado"""

note1 = float(input("Digite a primeira nota: "))
note2 = float(input("Digite a segunda nota:  "))

media = (note2 + note1)/2

if media < 5:
    print('O aluno com notas {:.2F} e {:.2F}\n'
          'Com média {:.2F}, está REPROVADO'.format(note1, note2, media))
elif 5 <= media <= 6.9:
    print('O aluno com notas {:.2F} e {:.2F}\n'
          'Com média {:.2F}, está EM RECUPERAÇÃO'.format(note1, note2, media))
elif media > 7:
    print('O aluno com notas {:.2F} e {:.2F}\n'
          'Com média {:.2F}, está APROVADO'.format(note1, note2, media))
