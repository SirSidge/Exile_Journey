import random

class Character:
    def __init__(self, name, hp, att_dmg):
        self.name = name
        self.hp = hp
        self.att_dmg = att_dmg

    def attack_target(self, target):
        damage = random.randint(self.att_dmg, self.att_dmg * 2)
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        return damage