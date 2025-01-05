from direct.showbase.ShowBase import ShowBase
from panda3d.core import load_prc_file_data
from game.environment import Environment
from game.player import Player
from game.input_handler import InputHandler

# Configure engine settings
load_prc_file_data("", """
    window-title FPS Game
    model-path $MAIN_DIR/assets/models
    framebuffer-multisample 1
    multisamples 2
    show-frame-rate-meter 1
    sync-video #f
""")


class Game(ShowBase):
    def __init__(self):
        super().__init__()

        # Initialize input handler first
        self.input_handler = InputHandler()

        # Initialize game components
        self.environment = Environment(self)
        self.player = Player(self)

        # Set up update task
        self.taskMgr.add(self.update, "update")

    def update(self, task):
        """Main game update loop"""
        dt = globalClock.getDt()
        self.player.update()
        return task.cont


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()