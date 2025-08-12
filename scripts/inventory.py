import pygame
import json

from scripts.scenes import Scene

class Inventory(Scene):
    def __init__(self):
        self.items = []
        self.font_heading_0 = pygame.font.Font(None, 40)
        self.sprites = {}
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.pop(item)
    
    def get_items(self):
        return self.items
    
    def create_inventory(self, spritesheet):
        with open("sprites/inventory.json") as f:
            data = json.load(f)
        for name, frame in data["frames"].items():
            rect = frame["frame"]
            self.sprites[name] = spritesheet.subsurface(pygame.Rect(rect["x"], rect["y"], rect["w"], rect["h"]))
    
    def handle_events(self, game_state, event):
        game_state.next_scene = game_state.state
        game_state.state = "inventory"

    def render(self, game_state, screen):
        game_state.screen.fill((0, 0, 50))
        game_state.draw_text("Inventory", self.font_heading_0, (255, 255, 255), 325, 240)
        screen.blit(self.sprites["Sprite-0001."], (100, 100))

class Item():
    def __init__(self, name, value=0, weight=0):
        self.name = name
        self.value = value
        self.weight = weight