from panda3d.core import loadPrcFileData
from .game import FPSGame
from .config import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE

class WebGame(FPSGame):
    def __init__(self):
        # Configure Panda3D for web
        self.configure_panda()
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