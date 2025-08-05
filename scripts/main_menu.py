import pygame

from scripts.scenes import Scene
from scripts.combat import Character

start_button = pygame.Rect(300, 280, 200, 50)
exit_button = pygame.Rect(300, 360, 200, 50)
name_button = pygame.Rect(300, 440, 200, 50)

class Main_Menu(Scene):
    def __init__(self):
        pass
    
    def handle_events(self):
        #print("Event handler")
        mouse_pos = pygame.mouse.get_pos()
        if start_button.collidepoint(mouse_pos):
            Character.reset_combat_log(Character)
            Character.update_log(Character, "Fight!")
            print("Start clicked.")

    def update(self):
        #print("updater")
        pass

    def render(self):
        #print("renderer")
        pass