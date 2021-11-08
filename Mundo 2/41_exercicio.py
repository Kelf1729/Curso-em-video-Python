"""Um programa para classificação
de um conjunto de alunos
* até 9 anos: mirim
* até 14 anos: infantil
* até 19 anos: junior
* até 20 anos: sênior
* Acima: Master"""

import datetime

year = int(input("Digite o ano de nascimento:  "))

if datetime.date.today().year - year <= 9:
    print("Classificação: MIRIM \n"
          "Idade de {}".format(datetime.date.today().year - year))
elif 9 <= datetime.date.today().year - year <= 14:
    print("Classificação: INFANTIL \n"
          "Idade de {}".format(datetime.date.today().year - year))
elif 14 <= datetime.date.today().year - year <= 19:
    print("Classificação: JUNIOR \n"
          "Idade de {}".format(datetime.date.today().year - year))
elif 19 <= datetime.date.today().year - year <= 20:
    print("Classificação: SÊNIOR \n"
          "Idade de {}".format(datetime.date.today().year - year))
elif datetime.date.today().year - year > 20:
    print("Classificação: MASTER \n"
          "Idade de {}".format(datetime.date.today().year - year))