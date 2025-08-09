import pygame

from scripts.scenes import Scene
from scripts.inventory import Item

class Combat(Scene):
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 22)
        self.combat = 0
        self.attack_sound = pygame.mixer.Sound("sounds/attack.wav")
        self.combat_log = []

    def handle_events(self, game_state, event):
        if game_state.alive:
            if event.type == game_state.player_timer and game_state.character.hp > 0:
                self.update_log(f"{game_state.character.name} attacks {game_state.enemy.name} and deals {game_state.character.attack_target(game_state.enemy)} damage, leaving them with {game_state.enemy.hp} hp left.")
                self.attack_sound.play()
            if event.type == game_state.enemy_timer and game_state.enemy.hp > 0:
                self.update_log(f"{game_state.enemy.name} attacks {game_state.character.name} and deals {game_state.enemy.attack_target(game_state.character)} damage, leaving them with {game_state.character.hp} hp left.")
                self.attack_sound.play()
            if game_state.character.hp <= 0 or game_state.enemy.hp <= 0:
                game_state.alive = False
                self.update_log("The game has ended.")
                if game_state.character.hp > 0:
                    self.update_log(f"{game_state.character.name} won!")
                    wolf_pelt = Item("Wolf pelt", 10, 1) #item, value, weight
                    game_state.character.inventory.add_item(wolf_pelt)
                    self.update_log(f"{game_state.character.name} has collected a {wolf_pelt.name}")
                if game_state.enemy.hp > 0:
                    self.update_log(f"{game_state.enemy.name} won!")

    def render(self, game_state):
        game_state.screen.fill((25, 25, 100))

        for entity in [game_state.character, game_state.enemy]:
            if entity.is_attacking:
                entity.attack_anim -= 1
                if entity.attack_anim > 40:
                    offset = 10 * (1 - (entity.attack_anim - 40) / 20)
                    if entity == game_state.character:
                        game_state.screen.blit(entity.sprite, (entity.base_pos[0] + offset, entity.base_pos[1]))
                    else:
                        game_state.screen.blit(entity.sprite, (entity.base_pos[0] - offset, entity.base_pos[1]))
                elif entity.attack_anim > 20:
                    if entity == game_state.character:
                        game_state.screen.blit(entity.sprite, (entity.base_pos[0] + 10, entity.base_pos[1]))
                    else:
                        game_state.screen.blit(entity.sprite, (entity.base_pos[0] - 10, entity.base_pos[1]))
                elif entity.attack_anim > 0:
                    offset = 10 * (entity.attack_anim / 20)
                    if entity == game_state.character:
                        game_state.screen.blit(entity.sprite, (entity.base_pos[0] + offset, entity.base_pos[1]))
                    else:
                        game_state.screen.blit(entity.sprite, (entity.base_pos[0] - offset, entity.base_pos[1]))
                else:
                    entity.is_attacking = False
                    game_state.screen.blit(entity.sprite, entity.base_pos)
            else:
                game_state.screen.blit(entity.sprite, entity.base_pos)
        for i in range(len(self.combat_log)):
            game_state.draw_text(self.combat_log[i], self.font, (255, 255, 255), 0, 580 - i * 25)
        game_state.draw_text(f"{game_state.character.name} HP: {game_state.character.hp}", self.small_font, (255, 255, 255), 70, 60)
        game_state.draw_text(f"{game_state.enemy.name} HP: {game_state.enemy.hp}", self.small_font, (255, 255, 255), 200, 60)
        for item in game_state.character.inventory.get_items():
            game_state.draw_text(f"Inventory: {item.name}", self.small_font, (255, 255, 255), 70, (game_state.character.inventory.items.index(item) * 20 + 180))
    
    def update_log(self, text):
        if len(self.combat_log) == 10:
            self.combat_log.pop(0)
        self.combat_log.insert(0, text)
    
    def reset_combat_log(self):
        self.combat_log = []