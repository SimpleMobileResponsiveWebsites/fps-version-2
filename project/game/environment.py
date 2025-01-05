from panda3d.core import CardMaker, Point3
from direct.showbase.ShowBase import ShowBase
import random
from panda3d.core import NodePath

class Environment(ShowBase):
    def __init__(self):
        """
        Initializes the Environment class.
        """
        super().__init__()

        self.floor_size = 100  # 100 meters by 100 meters for floor
        self.wall_height = 10  # 10 meters tall walls
        self.wall_thickness = 1  # 1 meter thick walls

        # Create the environment objects
        self.create_floor()
        self.create_walls()
        self.create_obstacles()

        # Add player to the environment
        self.create_player()

        # Hide the mouse cursor
        self.disableMouse()

    def create_floor(self) -> None:
        """
        Creates a large floor using a simple card.
        """
        card_maker = CardMaker("floor")
        card_maker.setFrame(-self.floor_size / 2, self.floor_size / 2, -self.floor_size / 2, self.floor_size / 2)

        floor = self.render.attachNewNode(card_maker.generate())
        floor.setPos(0, 0, 0)
        floor.setScale(1, 1, 1)
        floor.setColor(0.5, 0.5, 0.5, 1)  # Light gray color for the floor

    def create_walls(self) -> None:
        """
        Creates four walls around the floor.
        """
        self.create_wall(-self.floor_size / 2, 0, self.wall_height, self.floor_size, self.wall_thickness)  # Left wall
        self.create_wall(self.floor_size / 2, 0, self.wall_height, self.floor_size, self.wall_thickness)  # Right wall
        self.create_wall(0, -self.floor_size / 2, self.wall_height, self.floor_size, self.wall_thickness)  # Front wall
        self.create_wall(0, self.floor_size / 2, self.wall_height, self.floor_size, self.wall_thickness)  # Back wall

    def create_wall(self, x: float, y: float, height: float, length: float, thickness: float) -> None:
        """
        Helper function to create individual walls.
        """
        card_maker = CardMaker("wall")
        card_maker.setFrame(-length / 2, length / 2, -height / 2, height / 2)

        wall = self.render.attachNewNode(card_maker.generate())
        wall.setPos(x, y, height / 2)  # Raise the wall to match its height
        wall.setScale(1, thickness, 1)  # Adjust thickness of the wall
        wall.setColor(0.8, 0.4, 0.2, 1)  # Wall color: Brown

    def create_obstacles(self) -> None:
        """
        Add random obstacles to the map (for variety).
        """
        num_obstacles = 5
        for _ in range(num_obstacles):
            x = random.uniform(-self.floor_size / 2 + 5, self.floor_size / 2 - 5)
            y = random.uniform(-self.floor_size / 2 + 5, self.floor_size / 2 - 5)
            size = random.uniform(1, 3)  # Random size for each obstacle
            self.create_obstacle(x, y, size)

    def create_obstacle(self, x: float, y: float, size: float) -> None:
        """
        Creates a simple obstacle on the floor.
        """
        card_maker = CardMaker("obstacle")
        card_maker.setFrame(-size / 2, size / 2, -size / 2, size / 2)

        obstacle = self.render.attachNewNode(card_maker.generate())
        obstacle.setPos(x, y, size / 2)  # Position it slightly above the floor
        obstacle.setColor(0.7, 0.7, 0.7, 1)  # Gray color for the obstacle

    def create_player(self) -> None:
        """
        Create a simple player model.
        """
        # For now, let's use a simple cube to represent the player
        player = self.loader.loadModel("models/misc/sphere")  # Use any placeholder model
        player.setScale(0.5, 0.5, 1)
        player.setPos(0, 0, 1)  # Place the player above the floor
        player.reparentTo(self.render)

        # Store player node to move it later
        self.player = player

        # Attach a camera to the player
        self.camera.reparentTo(self.player)
        self.camera.setPos(0, -10, 5)  # Position the camera slightly behind the player

env = Environment()
env.run()
