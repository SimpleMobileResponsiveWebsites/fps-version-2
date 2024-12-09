from panda3d.showbase.ShowBase import ShowBase
from .input_handler import InputHandler
from .player import Player
from .window_manager import WindowManager
from .collision_manager import CollisionManager
from .web_adapter import WebAdapter
from .config import MODEL_PATH
from .utils import create_ground_plane

class FPSGame(ShowBase):
    def __init__(self):
        super().__init__()
        
        # Initialize game components
        self.window_manager = WindowManager(self)
        self.player = Player(self)
        self.input_handler = InputHandler(self)
        self.collision_manager = CollisionManager(self)
        self.web_adapter = WebAdapter(self)
        
        # Load scene
        self.setup_scene()
        
        # Add game update task
        self.taskMgr.add(self.update, "update")
    
    def setup_scene(self):
        try:
            self.scene = self.loader.loadModel(f"{MODEL_PATH}/environment")
            self.scene.reparentTo(self.render)
            self.scene.setScale(0.25, 0.25, 0.25)
            self.scene.setPos(-8, 42, 0)
        except:
            # Fallback to creating a simple ground plane if model loading fails
            self.scene = create_ground_plane(self.render)
    
    def update(self, task):
        self.player.update()
        return task.cont
    
    def cleanup(self):
        """Clean up resources before quitting"""
        self.ignoreAll()
        self.cleanup_scene()
    
    def cleanup_scene(self):
        """Clean up scene resources"""
        if hasattr(self, 'scene'):
            self.scene.removeNode()