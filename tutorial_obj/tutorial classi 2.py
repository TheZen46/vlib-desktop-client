'''
def add(a, b):
    return a + b

class Test:
    def __init__(self, add_function):
        self.add_function = add_function

test = Test(add_function = add)
return test.add_function(1, 2))
'''
#create a Monster class with a parameter called func, store this func as parameter

#create another class, called Attacks, that has 4methods:
#bite, strike, slash, kick (each method just prints some text)

#create a monster object and give it one of the attack methods from the attack class

class Monster:
    def __init__(self, func):
        self.func = func

class Attacks:

    def bite(self):
        print('the attack was a bite')
    
    def strike(self):
        print('the attack was a strike')
    
    def slash(self):
        print('the attack was a slash')
    
    def kick(self):
        print('the attack was a kick')
    

monster1 = Monster(func = Attacks().slash)

monster1.func()
