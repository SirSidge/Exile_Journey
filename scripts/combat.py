import random

from constants import *
from scripts.inventory import Inventory

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
        self.inventory = Inventory()
        self.combat_log = []

    def attack_target(self, target):
        damage = random.randint(self.att_dmg, self.att_dmg * 2)
        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
        self.is_attacking = True
        self.attack_anim = FRAMERATE #attack animation over 1second, or 60 frames
        return damage
    
    def update_log(self, text):
        if len(self.combat_log) == 10:
            self.combat_log.pop(0)
        self.combat_log.insert(0, text)
    
    def reset_combat_log(self):
        self.combat_log = []