#qualcosa di complesso e molto usato per dei progetti molto lunghi sono i multiparents working.

class Monster:

    def __init__(self, health, energy, **kwargs):
        print(kwargs)
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)
    
    def attack(self, amount):
        print('The Monster has attaked!!')
        print(f'{amount} damage was dealt')
        self.energy -= 20


    def move(self, speed):
        print('The Monster has moved!!')
        print(f'He moved at the speed of {speed}')

class Fish:

    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')

class Shark(Monster, Fish):
    def __init__(self, bite_streght, health, energy, speed, has_scales):
        self.bite_streght = bite_streght
        #MRO ---> method resolution order
        super().__init__(health = health, energy = energy, speed= speed, has_scales= has_scales) #prende il primo della lista (Monster)

#print(Shark.mro()) ----> da qui capiamo che Shark vale 0, Monster vale 1 e Fish 2

shark = Shark(
    bite_streght= 50, 
    health= 200, 
    energy=55, 
    speed = 120, 
    has_scales= False
    )

print(shark.has_scales)
print(shark.speed)