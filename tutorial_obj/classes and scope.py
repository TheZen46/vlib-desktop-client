
#problema sullo scope
def update_health(amount):
    monster.health += amount

'''
health = 10
print(health)
update_health(20)
print(20)
'''

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.set_energy(energy)

    def update_energy(self, amount):
        self.energy += amount

    def set_energy(self, energy):
        new_energy = energy * 2
        self.energy =  new_energy

monster = Monster(health= 100, energy= 50)
#monster.update_energy(20)
print(monster.energy)