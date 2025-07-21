import pygame
import json
from scripts.combat import Character
from constants import *

class CharacterCreation:
    def __init__(self):
        self.name = self.load_name() or "Heinz"
        self.hp = 100
        self.att_dmg = 16
        self.attack_speed = 1.2

    def update_name(self, event, current_input):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return current_input[:-1]
            elif event.key == pygame.K_RETURN:
                self.name = current_input or "Heinz"
                self.save_name()
                return ""
            elif event.unicode.isprintable() and len(current_input) < 10:
                return current_input + event.unicode
        return current_input

    def create_character(self):
        return Character(self.name, self.hp, self.att_dmg,
                        pygame.transform.scale(pygame.image.load("sprites/Player_001.png"), (64, 64)),
                        [80, 100], self.attack_speed)
    
    def save_name(self):
        with open("save_data.json", "w") as f:
            json.dump({"player_name": self.name}, f)

    def load_name(self):
        try:
            with open("save_data.json", "r") as f:
                data = json.load(f)
                return data.get("player_name", "")
        except FileNotFoundError:
            return ""