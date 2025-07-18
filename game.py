import pygame

from scripts.combat import Character
from scripts.character_creation import CharacterCreation
from constants import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
alive = True
state = "menu"
combat_log = []

# Character creation
char_creator = CharacterCreation()
character = Character("Heinz", 100, 16, pygame.transform.scale(pygame.image.load("sprites/Player_001.png"), (64, 64)), [80, 100], attack_speed=1.2)
enemy = Character("Wolf", 100, 14, pygame.transform.scale(pygame.image.load("sprites/Wolf_001.png"), (64, 64)), [200, 100], attack_speed=1.0)

# Fonts
font = pygame.font.Font(None, 30)
small_font = pygame.font.Font(None, 22)
font_heading = pygame.font.Font(None, 40)

# Buttons (in main menu)
start_button = pygame.Rect(300, 280, 200, 50)
exit_button = pygame.Rect(300, 360, 200, 50)
name_button = pygame.Rect(300, 440, 200, 50)

# Button (in character creation)
user_ip = ""
text_box = pygame.Rect(300, 180, 200, 50)
active = False

# Time
clock = pygame.time.Clock()

# Pre-character timers
player_timer = pygame.event.custom_type()
enemy_timer = pygame.event.custom_type()
pygame.time.set_timer(player_timer, int(1000 / character.attack_speed))
pygame.time.set_timer(enemy_timer, int(1000 / enemy.attack_speed))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def update_log(text):
    if len(combat_log) == 10:
        combat_log.pop(0)
    combat_log.insert(0, text)

while running:
    dt = clock.tick(FRAMERATE) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                combat_log = []
                character.hp = 100
                enemy.hp = 100
                alive = True
                if state == "battle":
                    update_log("You have chosen to rematch!")
                else:
                    state = "battle"
                    update_log("Fight!")
            if event.key == pygame.K_q:
                state = "menu"
        if state == "battle":
            if alive:
                if event.type == player_timer and character.hp > 0:
                    update_log(f"{character.name} attacks {enemy.name} and deals {character.attack_target(enemy)} damage, leaving them with {enemy.hp} hp left.")
                if event.type == enemy_timer and enemy.hp > 0:
                    update_log(f"{enemy.name} attacks {character.name} and deals {enemy.attack_target(character)} damage, leaving them with {character.hp} hp left.")
                if character.hp <= 0 or enemy.hp <= 0:
                    alive = False
                    update_log("The game has ended.")
                    if character.hp > 0:
                        update_log(f"{character.name} won!")
                    if enemy.hp > 0:
                        update_log(f"{enemy.name} won!")
        elif state == "menu":
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    combat_log = []
                    character = char_creator.create_character()  # Use new character
                    state = "battle"
                    character.hp = 100
                    enemy.hp = 100
                    alive = True
                    update_log("Fight!")
                    pygame.time.set_timer(player_timer, int(1000 / character.attack_speed))
                    pygame.time.set_timer(enemy_timer, int(1000 / enemy.attack_speed))
                elif name_button.collidepoint(mouse_pos):
                    state = "character_creation"
                elif exit_button.collidepoint(mouse_pos):
                    running = False
        elif state == "character_creation":
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if text_box.collidepoint(mouse_pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN and active:
                user_ip = char_creator.update_name(event, user_ip)
                if event.key == pygame.K_RETURN:
                    state = "menu"

    # Draw Battle scene
    if state == "battle":
        screen.fill((25, 25, 100))
        for entity in [character, enemy]:
            if entity.is_attacking:
                entity.attack_anim -= 1
                if entity.attack_anim > 40:
                    offset = 10 * (1 - (entity.attack_anim - 40) / 20)
                    if entity == character:
                        screen.blit(entity.sprite, (entity.base_pos[0] + offset, entity.base_pos[1]))
                    else:
                        screen.blit(entity.sprite, (entity.base_pos[0] - offset, entity.base_pos[1]))
                elif entity.attack_anim > 20:
                    if entity == character:
                        screen.blit(entity.sprite, (entity.base_pos[0] + 10, entity.base_pos[1]))
                    else:
                        screen.blit(entity.sprite, (entity.base_pos[0] - 10, entity.base_pos[1]))
                elif entity.attack_anim > 0:
                    offset = 10 * (entity.attack_anim / 20)
                    if entity == character:
                        screen.blit(entity.sprite, (entity.base_pos[0] + offset, entity.base_pos[1]))
                    else:
                        screen.blit(entity.sprite, (entity.base_pos[0] - offset, entity.base_pos[1]))
                else:
                    entity.is_attacking = False
                    screen.blit(entity.sprite, entity.base_pos)
            else:
                screen.blit(entity.sprite, entity.base_pos)
        for i in range(len(combat_log)):
            draw_text(combat_log[i], font, (255, 255, 255), 0, 580 - i * 25)
        draw_text(f"{character.name} HP: {character.hp}", small_font, (255, 255, 255), 70, 60)
        draw_text(f"{enemy.name} HP: {enemy.hp}", small_font, (255, 255, 255), 200, 60)
    elif state == "character_creation":
        screen.fill((0, 0, 80))
        pygame.draw.rect(screen, (100, 0, 100) if active else (0, 100, 0), text_box)
        draw_text(user_ip, font, (10, 10, 10), text_box.x + 5, text_box.y + 5)
        screen.blit(character.sprite, (370, 260))
    elif state == "menu":
        screen.fill((0, 0, 50))
        draw_text("Main Menu", font_heading, (255, 255, 255), 325, 240)
        pygame.draw.rect(screen, (0, 100, 0), start_button)
        pygame.draw.rect(screen, (100, 0, 0), exit_button)
        pygame.draw.rect(screen, (100, 100, 100), name_button)
        draw_text("Start", font, (255, 255, 255), 375, 297)
        draw_text("Exit", font, (255, 255, 255), 379, 377)
        draw_text("Name", font, (255, 255, 255), 372, 457)

    pygame.display.flip()
pygame.quit()