from panda3d.core import LVector3, Point3
from direct.task.Task import Task
from .utils import create_debug_text

class Player:
    def __init__(self, game):
        self.game = game
        self.camera = game.camera
        self.setup_camera()
        self.mouse_sensitivity = 0.2
        self.movement_speed = 5
        self.setup_debug_display()
    
    def setup_camera(self):
        self.game.disableMouse()
        self.camera.setPos(0, 0, 2)
        self.setup_crosshair()
    
    def setup_crosshair(self):
        self.crosshair = self.game.loader.loadModel("models/misc/sphere")
        self.crosshair.setScale(0.01)
        self.crosshair.setColor(1, 0, 0, 1)
        self.crosshair.reparentTo(self.camera)
    
    def setup_debug_display(self):
        """Setup debug information display"""
        self.pos_text = create_debug_text("", Point3(-1.3, 0, 0.9))
    
    def update(self):
        self.process_mouse()
        self.process_movement()
        self.update_debug_display()
    
    def process_mouse(self):
        if self.game.mouseWatcherNode.hasMouse():
            md = self.game.win.getPointer(0)
            x = md.getX()
            y = md.getY()
            
            self.game.win.movePointer(0, 400, 300)
            self.camera.setH(self.camera.getH() - (x - 400) * self.mouse_sensitivity)
            self.camera.setP(self.camera.getP() - (y - 300) * self.mouse_sensitivity)
    
    def process_movement(self):
        speed = self.movement_speed * globalClock.getDt()
        direction = LVector3(0, 0, 0)
        key_map = self.game.input_handler.get_key_map()
        
        if key_map["forward"]:
            direction += self.camera.getQuat().getForward()
        if key_map["backward"]:
            direction -= self.camera.getQuat().getForward()
        if key_map["left"]:
            direction -= self.camera.getQuat().getRight()
        if key_map["right"]:
            direction += self.camera.getQuat().getRight()
        
        direction.setZ(0)
        if not direction.isZero():
            direction.normalize()
            self.camera.setPos(self.camera.getPos() + direction * speed)
    
    def update_debug_display(self):
        """Update debug information"""
        pos = self.camera.getPos()
        self.pos_text.setText(f"Pos: {pos.x:.1f}, {pos.y:.1f}, {pos.z:.1f}")