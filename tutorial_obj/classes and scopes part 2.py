
#exercise
#1. create a hero class with 2 parameters: damage, monster
#2. the monster class should have a method that lowers the health -> get_damage(amount)
#3. the hero class should have an attack method that callls the get_damage method from the monster
#the amount of damage is hero.damage

class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster
    
    def attach(self):
        self.monster.get_damage(self.damage)
        
        
class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    '''
    def update_energy(self, amount):
        self.energy += amount
    '''
    def get_damage(self, amount):
        self.health -= amount

monster1 = Monster(150, 50)
hero = Hero(90, monster1)
hero.attach()
print(monster1.health)