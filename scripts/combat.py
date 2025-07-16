import random

class Character:
    def __init__(self, name, hp, att_dmg):
        self.name = name
        self.hp = hp
        self.att_dmg = att_dmg

    def attack(self, target):
        target.hp -= random.randint(5, 15)