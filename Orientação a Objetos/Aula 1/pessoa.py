#Módulo 
from datetime import datetime



#OOP
class Pessoa():
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome 
        self.idade = idade 
        self.comendo = comendo 
        self.falando = falando 
    
    def comer(self,alimento):
        if self.comendo:
            print("Já está comendo algo")
            return
        
        print(f'A pessoa {self.nome} está comendo {alimento}')
        self.comendo = True
        
    def parar_comer(self):
        if not self.comendo:
            print("Ele já não está comendo")
            return 
        print("Parou de comer, segundo a ordem")
        self.comendo = False
        
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome}, não pode falar, está comendo')
            return
        if self.falando:
            print("ele já está falando de um assunto")
            
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True
        
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade 