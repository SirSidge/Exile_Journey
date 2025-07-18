import random

from constants import *

class Character:
    def __init__(self, name, hp, att_dmg, sprite, pos, attack_speed=1.0):
        self.name = name
        self.hp = hp
        self.att_dmg = att_dmg
        self.sprite = sprite
        self.pos = pos
        self.is_attacking = False
        self.attack_anim = 0
        self.base_pos = pos[:]
        self.attack_speed = attack_speed

    def attack_target(self, target):
        damage = random.randint(self.att_dmg, self.att_dmg * 2)
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        self.is_attacking = True
        self.attack_anim = FRAMERATE #attack animation over 1second, or 60 frames
        return damage