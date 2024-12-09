"""Utility functions for the game"""
from panda3d.core import CardMaker, NodePath, TextNode, Point3
from direct.gui.OnscreenText import OnscreenText

def create_ground_plane(render: NodePath, size: float = 20, color: tuple = (0.3, 0.3, 0.3, 1)) -> NodePath:
    """Create a simple ground plane when model loading fails"""
    cm = CardMaker('ground')
    cm.setFrame(-size, size, -size, size)
    ground = render.attachNewNode(cm.generate())
    ground.setP(-90)
    ground.setPos(0, 0, 0)
    ground.setColor(*color)
    return ground

def create_debug_text(text: str, pos: Point3, scale: float = 0.07) -> OnscreenText:
    """Create debug text overlay"""
    return OnscreenText(
        text=text,
        pos=pos,
        scale=scale,
        fg=(1, 1, 1, 1),
        bg=(0, 0, 0, 0.5),
        align=TextNode.ALeft
    )