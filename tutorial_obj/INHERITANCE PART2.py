#parte 6 del video di simple code: 1:15:05
#   VERSIONE CON helath E energy VARIABILI
class Monster:

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print('The Monster has attaked!!')
        print(f'{amount} damage was dealt')
        self.energy -= 20


    def move(self, speed):
        print('The Monster has moved!!')
        print(f'He moved at the speed of {speed}')

class Shark(Monster):
    def __init__(self, speed, health, energy):
        #Monster.__init__(self, health, energy)
        super().__init__(health, energy)
        #super().move(10) #----> esegue la funzione della classe madre anche se c'è sovrascrizione
        self.speed = speed

    def bite(self):
        print('The shark has bitten')

    # se volessi modificare qualche parametro presente già nella classe 
    # madre allora basta sovrascriverlo ridefinendo la funzione del interessato
    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}')

'''
shark = Shark(speed=120, health=100, energy=80)
print(shark.speed)
print(shark.health)
print(shark.energy)
'''
#exercise
#create scorpin class that inherits from monster
# health and enrgy from the parent
# poison_damage attirbute
# overwrite the damage method to show poison damage

class Scorpion(Monster):
    def __init__(self, poison_damage, health, energy):
        self.poison_damage = poison_damage
        super().__init__(health, energy)

    def attack(self):
        print('The scorpion has attaked!!')
        print(f'{self.poison_damage} damage was dealt for poison damage')

scorpion = Scorpion(50, 5065)
scorpion.attack()