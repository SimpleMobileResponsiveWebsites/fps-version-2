from panda3d.core import CardMaker, NodePath, Vec3, Point3
from direct.showbase.ShowBase import ShowBase
from panda3d.core import LineSegs


class Environment:
    def __init__(self, game):
        """
        Initializes the Environment class.
        Args:
            game: The main game instance
        """
        self.game = game
        self.render = game.render
        self.loader = game.loader

        # Configuration settings
        self.floor_size = 1000
        self.wall_height = 10
        self.wall_thickness = 1
        self.terrain_type = "desert"

        # Map details and buildings
        self.buildings = [
            {"name": "barracks", "position": Vec3(45, 50, 10)},
            {"name": "Med Tent", "position": Vec3(450, 550, 10)},
            {"name": "Med Tent", "position": Vec3(600, 650, 10)},
            {"name": "Med Tent", "position": Vec3(700, 750, 10)},
            {"name": "Mechanic", "position": Vec3(800, 850, 10)},
            {"name": "Armory", "position": Vec3(900, 901, 10)},
            {"name": "Hangar", "position": Vec3(7, 4, 10)},
            {"name": "Hospital", "position": Vec3(1200, 1201, 30)},
            {"name": "Hospital Maintenance Building", "position": Vec3(1290, 1291, 10)},
            {"name": "Hospital Parcade Shack", "position": Vec3(1300, 1301, 10)},
        ]

        self.load_environment()
        self.create_floor()
        self.create_walls()
        self.create_buildings()

        # Debug floor grid (optional, helps with orientation)
        self.create_debug_grid()

    def load_environment(self):
        """Loads the main environment model"""
        try:
            model = self.loader.loadModel("assets/models/environment/environment.egg")
            if model:
                model.reparentTo(self.render)
                print("Environment model loaded successfully")
            else:
                print("Failed to load environment model")
        except Exception as e:
            print(f"Error loading environment model: {e}")

    def create_floor(self):
        """Creates a large floor (desert terrain) using a simple card."""
        card_maker = CardMaker("floor")
        card_maker.setFrame(-self.floor_size / 2, self.floor_size / 2, -self.floor_size / 2, self.floor_size / 2)

        floor = self.render.attachNewNode(card_maker.generate())
        floor.setPos(0, 0, 0)
        floor.setScale(1, 1, 1)
        floor.setColor(0.8, 0.7, 0.5, 1)  # Desert sand color

    def create_walls(self):
        """Creates four walls around the environment."""
        self.create_wall(-self.floor_size / 2, 0, self.wall_height, self.floor_size, self.wall_thickness)  # Left
        self.create_wall(self.floor_size / 2, 0, self.wall_height, self.floor_size, self.wall_thickness)  # Right
        self.create_wall(0, -self.floor_size / 2, self.wall_height, self.floor_size, self.wall_thickness)  # Front
        self.create_wall(0, self.floor_size / 2, self.wall_height, self.floor_size, self.wall_thickness)  # Back

    def create_wall(self, x: float, y: float, height: float, length: float, thickness: float):
        """Helper function to create individual walls."""
        card_maker = CardMaker("wall")
        card_maker.setFrame(-length / 2, length / 2, -height / 2, height / 2)

        wall = self.render.attachNewNode(card_maker.generate())
        wall.setPos(x, y, height / 2)
        wall.setScale(1, thickness, 1)
        wall.setColor(0.8, 0.4, 0.2, 1)

    def create_buildings(self):
        """Creates buildings and points of interest."""
        for building in self.buildings:
            self.create_building(building["name"], building["position"])

    def create_building(self, name: str, position: Vec3):
        """Helper function to create buildings."""
        card_maker = CardMaker(name)
        card_maker.setFrame(-10, 10, -10, 10)
        building = self.render.attachNewNode(card_maker.generate())
        building.setPos(position)
        building.setScale(1, 1, position.z / 10)
        building.setColor(0.6, 0.6, 0.6, 1)

    def create_debug_grid(self):
        """Creates a visual grid on the floor for debugging."""
        grid_size = 100
        grid_spacing = 10

        for x in range(-grid_size, grid_size + 1, grid_spacing):
            self.create_line(Point3(x, -grid_size, 0.1), Point3(x, grid_size, 0.1))
        for y in range(-grid_size, grid_size + 1, grid_spacing):
            self.create_line(Point3(-grid_size, y, 0.1), Point3(grid_size, y, 0.1))

    def create_line(self, start, end):
        """Helper function to create a line segment."""
        segs = LineSegs()
        segs.moveTo(start)
        segs.drawTo(end)
        segs.setThickness(1)
        segs.setColor(0.3, 0.3, 0.3, 1)
        node = segs.create()
        self.render.attachNewNode(node)
