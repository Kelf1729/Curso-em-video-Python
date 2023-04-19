#Estudo de OOP
from pessoa import Pessoa 

p1 = Pessoa("Luiz", 29)
p2 = Pessoa("Lucas", 42)

#Ações 
p1.comer("Arroz")
p1.falar("Música")

#saída 
print(p1.get_ano_nascimento())
