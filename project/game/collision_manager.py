from panda3d.core import (
    CollisionTraverser,
    CollisionNode,
    CollisionRay,
    CollisionHandlerQueue
)
from .constants import GROUND_MASK, PROJECTILE_MASK

class CollisionManager:
    def __init__(self, game):
        self.game = game
        self.setup_collision_system()
    
    def setup_collision_system(self):
        self.traverser = CollisionTraverser()
        self.handler = CollisionHandlerQueue()
    
    def shoot(self):
        ray = CollisionRay()
        ray.setOrigin(self.game.camera.getPos())
        ray.setDirection(self.game.camera.getQuat().getForward())
        
        collision_node = CollisionNode("ray")
        collision_node.addSolid(ray)
        collision_node.setFromCollideMask(PROJECTILE_MASK)
        collision_node_path = self.game.camera.attachNewNode(collision_node)
        
        self.traverser.addCollider(collision_node_path, self.handler)
        self.traverser.traverse(self.game.render)
        
        if self.handler.getNumEntries() > 0:
            self.handler.sortEntries()
            hit = self.handler.getEntry(0).getIntoNodePath()
            print(f"Hit: {hit}")
        else:
            print("Missed!")
        
        collision_node_path.removeNode()