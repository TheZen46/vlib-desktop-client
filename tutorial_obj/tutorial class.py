class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    def __len__(self):
        return self.health
