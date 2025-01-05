from direct.showbase.DirectObject import DirectObject
from panda3d.core import KeyboardButton


class InputHandler(DirectObject):
    def __init__(self):
        super().__init__()

        self.key_map = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False,
            "jump": False
        }

        # Bind keys
        self.accept("w", self.update_key_map, ["forward", True])
        self.accept("w-up", self.update_key_map, ["forward", False])
        self.accept("s", self.update_key_map, ["backward", True])
        self.accept("s-up", self.update_key_map, ["backward", False])
        self.accept("a", self.update_key_map, ["left", True])
        self.accept("a-up", self.update_key_map, ["left", False])
        self.accept("d", self.update_key_map, ["right", True])
        self.accept("d-up", self.update_key_map, ["right", False])
        self.accept("space", self.update_key_map, ["jump", True])
        self.accept("space-up", self.update_key_map, ["jump", False])

    def update_key_map(self, key, value):
        self.key_map[key] = value

    def get_key_map(self):
        return self.key_map