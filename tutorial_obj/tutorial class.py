from typing import Any


class Monster:
    '''
     __dunder__methos: è una funzione che si applica AUTOMATICAMENTE e non è quindi avviabile
     dall'utente, ci sono vari __dunder__methos:
            __init__  -->  è applicato ALLA CREAZIONE dell'oggetto
            __len__   -->  è applicato quando l'oggetto è passato sotto la funzione len()
            __abs__   -->  è applicato quando l'oggetto è passato sotto la funzione abs()
            __call__  -->  è applicato quando l'oggetto è passato sotto la fu

    '''
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

  #  '''

    def __len__(self):
        return self.health
    
    def __abs__(self):
        return self.energy
    
    def __call__(self):
        print('The monster was called')
        #questa funzione rende l'oggetto una funzione
    
    def __add__(self, other):
        return self.health + other
    
  #  '''
    def __str__(self):
        return f'The monster has {self.health} points of health and {self.energy} points of energy'
        #veramente utile

    #funzioni
    def attack(self, amount):
        print('The Monster has attaked!!')
        print(f'{amount} damage was dealt')
        self.energy -= 20
        print(self.energy)

    def move(self, speed):
        print('The Monster has moved!!')
        print(f'He moved at the speed of {speed}')


monster1 = Monster(10, 20)
print(str(monster1))