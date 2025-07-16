import pygame

from scripts.combat import Character

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
alive = True

character = Character("Heinz", 100, 16)
enemy = Character("Wolf", 100, 14)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

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
    screen.fill((0, 0, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character.hp = 100
                enemy.hp = 100
                update_log("You have chosen to rematch!")
                alive = True

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

    clock.tick(60)
    for i in range(len(combat_log)):
        screen.blit(font.render(combat_log[i], True, (255, 255, 255)), (0, (580 - (i * 25))))
    screen.blit(font.render(f"{character.name} HP: {character.hp}", True, (255, 255, 255)), (600, 10))
    screen.blit(font.render(f"{enemy.name} HP: {enemy.hp}", True, (255, 255, 255)), (600, 30))
    
    pygame.display.flip()
pygame.quit()