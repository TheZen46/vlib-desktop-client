#parte 6 del video di simple code: 1:15:05
#   VERSIONE SENZA helath E energy VARIABILI
class Monster:
    health = 50
    energy = 100
    '''
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    '''
    def attack(self, amount):
        print('The Monster has attaked!!')
        print(f'{amount} damage was dealt')
        self.energy -= 20


    def move(self, speed):
        print('The Monster has moved!!')
        print(f'He moved at the speed of {speed}')

class Shark(Monster):
    def __init__(self, speed) :
        self.speed = speed

    def bite(self):
        print('The shark has bitten')

    # se volessi modificare qualche parametro presente già nella classe 
    # madre allora basta sovrascriverlo ridefinendo la funzione del interessato
    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}')

shark = Shark(speed= 120)
print(shark.health)
shark.attack(9)
shark.bite()
shark.move()

