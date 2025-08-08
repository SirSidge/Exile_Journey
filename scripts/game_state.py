class GameState:
    def __init__(self, character, enemy, player_timer, enemy_timer):
        self.state = "menu"
        self.character = character
        self.alive = True
        self.running = True
        self.enemy = enemy
        self.player_timer = player_timer
        self.enemy_timer = enemy_timer

    def change_scene():
        pass #Add info for each scene change. From fight to inventory and from fight to main menu would be different.