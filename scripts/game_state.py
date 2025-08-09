import pygame

from scripts.combat import Combat

class GameState:
    def __init__(self, character, enemy, screen, combat):
        self.state = "menu"
        self.next_scene = ""
        self.character = character
        self.alive = True
        self.running = True
        self.enemy = enemy
        self.player_timer = pygame.event.custom_type()
        self.enemy_timer = pygame.event.custom_type()
        self.screen = screen
        self.combat = combat

        pygame.time.set_timer(self.player_timer, int(1000 / character.attack_speed))
        pygame.time.set_timer(self.enemy_timer, int(1000 / enemy.attack_speed))

    def change_scene(self):
        self.to_combat_scene()

    def to_menu_scene(self):
        pass

    def to_combat_scene(self):
        if self.state == "menu":
            self.combat.reset_combat_log()
            self.combat.update_log("Fight!")
        else:
            self.combat.reset_combat_log()
            self.combat.update_log("You have chosen to rematch!")
        self.state = "combat"
        self.alive = True
        self.character.hp = 100
        self.enemy.hp = 80
        pygame.time.set_timer(self.player_timer, int(1000 / self.character.attack_speed))
        pygame.time.set_timer(self.enemy_timer, int(1000 / self.enemy.attack_speed))

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def render(self):
        pass # check which state it's on and then call that object's render.
    # Note, inefficient to do above as the object then needs to be passed, but that requires an if-statement to see which object it is.
    # Maybe one can have the 'state' include whatever object needs to do whatever. if the state is 'menu' then the object is in "game_state.scene_obj" or something