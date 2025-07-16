import pygame

from scripts.combat import Character

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

character = Character("Heinz", 100, 50)
enemy = Character("Wolf", 100, 10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if event.key == pygame.K_SPACE:
                character.attack(enemy)
                print(f"{character.name} attacks {enemy.name}, leaving them with {enemy.hp}hp left.")
    
    screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()