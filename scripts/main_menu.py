import pygame

from scripts.scenes import Scene
from scripts.combat import Character
#from scripts.game_state import GameState

start_button = pygame.Rect(300, 280, 200, 50)
exit_button = pygame.Rect(300, 360, 200, 50)
name_button = pygame.Rect(300, 440, 200, 50)

class Main_Menu(Scene):
    def __init__(self):
        pass
    
    def handle_events(self, game_state):
        if pygame.mouse.get_pressed()[0]:
            #print("Event handler")
            mouse_pos = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_pos):
                Character.reset_combat_log(Character)
                Character.update_log(Character, "Fight!")
                game_state.state = "battle"
                game_state.alive = True
                print("Start clicked.")
                game_state.character.hp = 100
                game_state.enemy.hp = 80
                pygame.time.set_timer(game_state.player_timer, int(1000 / game_state.character.attack_speed)) #Move to Fight scene
                pygame.time.set_timer(game_state.enemy_timer, int(1000 / game_state.enemy.attack_speed)) #Move to Fight scene
            elif name_button.collidepoint(mouse_pos):
                game_state.state = "character_creation"
            elif exit_button.collidepoint(mouse_pos):
                game_state.running = False

    def update(self):
        #print("updater")
        pass

    def render(self):
        #print("renderer")
        pass