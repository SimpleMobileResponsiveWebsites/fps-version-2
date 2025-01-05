from panda3d.core import loadPrcFileData
from .game import FPSGame
from .config import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE
from .collision_manager import CollisionManager  # Import the CollisionManager class
from .input_handler import InputHandler  # Import the InputHandler class

class WebGame(FPSGame):
    def __init__(self):
        # Configure Panda3D for web
        self.configure_panda()

        # Initialize collision manager
        self.collision_manager = CollisionManager(self)

        # Initialize the input handler with the game instance (self)
        self.input_handler = InputHandler(self)

        # Call the parent constructor (FPSGame)
        super().__init__()

    def configure_panda(self):
        """Configure Panda3D settings for web environment"""
        loadPrcFileData("", f"""
            win-size {WINDOW_WIDTH} {WINDOW_HEIGHT}
            window-title {WINDOW_TITLE}
            framebuffer-multisample 1
            multisamples 2
            texture-anisotropic-degree 2
            texture-magfilter linear
            texture-minfilter linear
            cursor-hidden 1
            show-frame-rate-meter 1
            support-threads 0
            audio-library-name null
        """)
