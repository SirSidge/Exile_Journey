import pygame

from scripts.combat import Character

pygame.init()
player_sprite = pygame.image.load("sprites/Player_001.png")
player_sprite = pygame.transform.scale(player_sprite, (64, 64))
screen = pygame.display.set_mode((800, 600))
running = True
alive = True
state = "menu"

character = Character("Heinz", 100, 16)
enemy = Character("Wolf", 100, 14)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
font_heading = pygame.font.Font(None, 40)

#buttons
start_button = pygame.Rect(300, 280, 200, 50)
exit_button = pygame.Rect(300, 360, 200, 50)

timer_event = pygame.event.custom_type()
pygame.time.set_timer(timer_event, 1000)

combat_log = []

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def update_log(text):
    #if len(combat_log) == 5:
        #combat_log.pop(len(combat_log) - 1)
    combat_log.insert(0, text)

while running:
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
                if event.type == timer_event:
                    if character.hp > 0:
                        update_log(f"{character.name} attacks {enemy.name} and deals {character.attack_target(enemy)} damage, leaving them with {enemy.hp} hp left.")
                    if enemy.hp > 0:
                        update_log(f"{enemy.name} attacks {character.name} and deals {enemy.attack_target(character)} damage, leaving them with {character.hp} hp left.")
                    if character.hp <= 0 or enemy.hp <= 0:
                        alive = False
                        update_log("The game has ended.")
                        if character.hp > 0:
                            update_log(f"{character.name} won!")
                        if enemy.hp > 0:
                            update_log(f"{enemy.name} won!")
        if state == "menu":
            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    combat_log = []
                    state = "battle"
                    character.hp = 100
                    enemy.hp = 100
                    alive = True
                    update_log("Fight!")
                if exit_button.collidepoint(mouse_pos):
                    running = False

    clock.tick(60)
    if state == "battle":
        screen.fill((25, 25, 100))
        screen.blit(player_sprite, (100, 100))
        for i in range(len(combat_log)):
            draw_text(combat_log[i], font, (255, 255, 255), 0, 580 - i * 25)
        draw_text(f"{character.name} HP: {character.hp}", font, (255, 255, 255), 600, 10)
        draw_text(f"{enemy.name} HP: {enemy.hp}", font, (255, 255, 255), 600, 30)
    elif state == "menu":
        screen.fill((0, 0, 50))
        draw_text("Main Menu", font_heading, (255, 255, 255), 325, 240)
        pygame.draw.rect(screen, (0, 100, 0), start_button)
        pygame.draw.rect(screen, (100, 0, 0), exit_button)
        draw_text("Start", font, (255, 255, 255), 375, 297)
        draw_text("Exit", font, (255, 255, 255), 379, 377)
    
    pygame.display.flip()
pygame.quit()