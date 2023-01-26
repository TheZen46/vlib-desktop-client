class Monster:
    '''A monster that has some attributes'''
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

        # private attributes -----> qualcosa che è immodificabile all'esterno della classe
        self._id = 5  #----> può essere qualsiasi cosa
        #più che aaltro questa funzione serve per poter dire agli altri developer di non modificare quella parte


    def attack(self, amount):
        print('The Monster has attaked!!')
        print(f'{amount} damage was dealt')
        self.energy -= 20


    def move(self, speed):
        print('The Monster has moved!!')
        print(f'He moved at the speed of {speed}')

monster = Monster(20, 10)
print(monster._id)

#-----------------------------------------------------------

# hasattr and setattr  ----> le due funzioni si dividono in 
#1) hasattr (obj, name): che verifica che un attributo sia presente in un oggetto, con questo risponde con True o False
if hasattr(monster, 'health'):
    print(f'the mosnter has {monster.health} health')

#2) setattr (obj, name, value): serve per aggiungere un nuovo attributo all'oggetto selezionato
setattr(monster, 'weapon', 'Sword')
print(monster.weapon)

new_attributes = (['weapon', 'Axe'],['Armor', 'Shield'], ['potion', 'mana'])

for attr,value in new_attributes:
    setattr(monster, attr, value)
print(vars(monster))

#-----------------------------------------------------------

# doc
print(monster.__doc__)
help(monster)
