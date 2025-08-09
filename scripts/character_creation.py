import pygame
import json

from scripts.character import Character
from constants import *

class CharacterCreation:
    def __init__(self):
        self.name = self.load_name() or "Heinz"
        self.hp = 100
        self.att_dmg = 16
        self.attack_speed = 1.2
        self.user_ip = ""
        self.text_box = pygame.Rect(300, 180, 200, 50)
        self.cancel_box = pygame.Rect(300, 400, 200, 50)
        self.active = False
        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 22)

    def update_name(self, event, current_input):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                return current_input[:-1]
            elif event.key == pygame.K_RETURN:
                self.name = current_input or "Heinz"
                self.save_name()
                self.active = False
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
        
    def render(self, game_state):
        game_state.screen.fill((0, 0, 80))
        pygame.draw.rect(game_state.screen, (100, 0, 100) if self.active else (0, 100, 0), self.text_box)
        game_state.draw_text(self.user_ip, self.font, (10, 10, 10), self.text_box.x + 5, self.text_box.y + 5)
        pygame.draw.rect(game_state.screen, (0, 100, 0), self.cancel_box)
        game_state.draw_text("Cancel", self.font, (255, 255, 255), 365, 417)
        game_state.draw_text("Enter Name (Press ENTER to save)", self.small_font, (255, 255, 255), 275, 140)
        game_state.screen.blit(game_state.character.sprite, (370, 260))

    def handle_events(self, game_state, event):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.text_box.collidepoint(mouse_pos):
                self.active = True
            else:
                self.active = False
            if self.cancel_box.collidepoint(mouse_pos):
                self.user_ip = ""
                self.active = False
                game_state.state = "menu"
        if event.type == pygame.KEYDOWN and self.active:
            self.user_ip = self.update_name(event, self.user_ip)
            if event.key == pygame.K_RETURN:
                game_state.state = "menu"