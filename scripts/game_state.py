class GameState:
    def __init__(self, character):
        self.state = "menu"
        self.character = character
        self.alive = True
        self.running = True

    def change_scene():
        pass #Add info for each scene change. From fight to inventory and from fight to main menu would be different.