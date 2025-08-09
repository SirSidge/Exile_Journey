import pygame

from scripts.scenes import Scene
from scripts.character import Character

class Main_Menu(Scene):
    def __init__(self):
        self.start_button = pygame.Rect(300, 280, 200, 50)
        self.exit_button = pygame.Rect(300, 360, 200, 50)
        self.name_button = pygame.Rect(300, 440, 200, 50)
        self.font_heading_0 = pygame.font.Font(None, 40)
        self.font_heading_1 = pygame.font.Font(None, 30)
    
    def handle_events(self, game_state):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.start_button.collidepoint(mouse_pos):
                game_state.next_scene = "combat"
                game_state.change_scene()
            elif self.name_button.collidepoint(mouse_pos):
                game_state.state = "character_creation"
            elif self.exit_button.collidepoint(mouse_pos):
                game_state.running = False

    def update(self):
        #print("updater")
        pass

    def render(self, game_state):
        game_state.screen.fill((0, 0, 50))
        game_state.draw_text("Main Menu", self.font_heading_0, (255, 255, 255), 325, 240)
        pygame.draw.rect(game_state.screen, (0, 100, 0), self.start_button)
        pygame.draw.rect(game_state.screen, (100, 0, 0), self.exit_button)
        pygame.draw.rect(game_state.screen, (100, 100, 100), self.name_button)
        game_state.draw_text("Start", self.font_heading_1, (255, 255, 255), 375, 297)
        game_state.draw_text("Exit", self.font_heading_1, (255, 255, 255), 379, 377)
        game_state.draw_text("Name", self.font_heading_1, (255, 255, 255), 372, 457)