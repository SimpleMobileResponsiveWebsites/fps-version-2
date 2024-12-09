from panda3d.core import WindowProperties
from .config import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, FULLSCREEN

class WindowManager:
    def __init__(self, game):
        self.game = game
        self.setup_window()
    
    def setup_window(self):
        properties = WindowProperties()
        properties.setSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        properties.setTitle(WINDOW_TITLE)
        properties.setFullscreen(FULLSCREEN)
        properties.setUndecorated(FULLSCREEN)
        self.game.win.requestProperties(properties)
    
    def update_window_size(self, width, height):
        """Update window size, maintaining aspect ratio"""
        properties = WindowProperties()
        properties.setSize(width, height)
        self.game.win.requestProperties(properties)
        
        # Update camera lens for new aspect ratio
        aspect_ratio = width / height
        self.game.camLens.setAspectRatio(aspect_ratio)