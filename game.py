import pygame

from scripts.character import Character
from scripts.character_creation import CharacterCreation
from constants import *
from scripts.inventory import Inventory, Item
from scripts.main_menu import Main_Menu
from scripts.game_state import GameState
from scripts.combat import Combat

pygame.init()
pygame.mixer.init(buffer=512)
screen = pygame.display.set_mode(SCREEN_SIZE)
attack_sound = pygame.mixer.Sound("sounds/attack.wav")

# Scenes initialization
main_menu = Main_Menu()
character_creation = CharacterCreation()
combat = Combat()
inventory = Inventory()
spritesheet = pygame.image.load("sprites/inventory.png").convert_alpha()
inventory.create_inventory(spritesheet)

# Character creation
user_ip = character_creation.name
character = Character(character_creation.name or "Heinz", 100, 16, pygame.transform.scale(pygame.image.load("sprites/Player_001.png"), (64, 64)), [80, 100], attack_speed=1.2)
enemy = Character("Wolf", 100, 14, pygame.transform.scale(pygame.image.load("sprites/Wolf_001.png"), (64, 64)), [200, 100], attack_speed=1.0)

# Game State init
game_state = GameState(character, enemy, screen, combat)

# Fonts
font = pygame.font.Font(None, 30)
small_font = pygame.font.Font(None, 22)
font_heading = pygame.font.Font(None, 40)

# Time
clock = pygame.time.Clock()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

while game_state.running:
    dt = clock.tick(FRAMERATE) / 1000
    for event in pygame.event.get():
        # Check for Quit
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            game_state.running = False
        
        # Input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state.state != "character_creation":
                game_state.next_scene = "combat"
                game_state.change_scene()
            if event.key == pygame.K_q and not character_creation.active:
                if game_state.state == "menu":
                    game_state.running = False
                else:
                    game_state.state = "menu"
            if event.key == pygame.K_i and not character_creation.active:
                if game_state.state == "inventory":
                    game_state.state = game_state.next_scene
                else:
                    game_state.next_scene = game_state.state
                    game_state.state = "inventory"
        
        # Checking state and then handling events in said scene
        if game_state.state == "combat":
            combat.handle_events(game_state, event)
        elif game_state.state == "menu":
            if pygame.mouse.get_pressed()[0]:
                main_menu.handle_events(game_state)
        elif game_state.state == "character_creation":
            character_creation.handle_events(game_state, event)
            character.name = character_creation.name
        #elif game_state.state == "inventory":
            #inventory.handle_events(game_state, event)

    # Draw character scene
    if game_state.state == "combat":
        combat.render(game_state)
    elif game_state.state == "character_creation":
        character_creation.render(game_state)
    elif game_state.state == "menu":
        main_menu.render(game_state)
    elif game_state.state == "inventory":
        inventory.render(game_state, screen)

    pygame.display.flip()
pygame.quit()



# Known bugs:
# 1 - Name change only takes effect once game has been relaunched. (Completed)
# 2 - Pressing space on the character creation screen immediately starts combat. (Completed)
# 3 - The end game message isn't always displayed correctly. When Player kills the monster, it doesn't record the final attack.
# 4 - When fight is over and the player collects the loot, the log doesn't always display that loot was collected.