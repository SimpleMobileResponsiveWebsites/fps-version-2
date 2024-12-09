import asyncio
from game.web_game import WebGame
import os
import sys

# Configure Python path for web environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

async def main():
    """Async main entry point for the web game"""
    game = WebGame()
    
    try:
        while True:
            game.taskMgr.step()
            await asyncio.sleep(0)  # Allow other async operations
    except Exception as e:
        print(f"Game error: {e}")
        game.cleanup()

if __name__ == "__main__":
    asyncio.run(main())