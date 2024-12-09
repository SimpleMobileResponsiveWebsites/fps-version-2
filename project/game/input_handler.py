import sys
from direct.showbase.DirectObject import DirectObject

class InputHandler(DirectObject):
    def __init__(self, game):
        self.game = game
        self.setup_key_map()
        self.setup_controls()
    
    def setup_key_map(self):
        self.key_map = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False
        }
    
    def setup_controls(self):
        # Movement controls
        self.accept("w", self.update_key_map, ["forward", True])
        self.accept("w-up", self.update_key_map, ["forward", False])
        self.accept("s", self.update_key_map, ["backward", True])
        self.accept("s-up", self.update_key_map, ["backward", False])
        self.accept("a", self.update_key_map, ["left", True])
        self.accept("a-up", self.update_key_map, ["left", False])
        self.accept("d", self.update_key_map, ["right", True])
        self.accept("d-up", self.update_key_map, ["right", False])
        
        # Other controls
        self.accept("escape", sys.exit)
        self.accept("mouse1", self.game.collision_manager.shoot)
    
    def update_key_map(self, key, value):
        self.key_map[key] = value
    
    def get_key_map(self):
        return self.key_map