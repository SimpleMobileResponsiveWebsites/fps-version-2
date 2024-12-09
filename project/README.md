# Panda3D Web FPS Game

A web-based First Person Shooter game built with Panda3D and Pygbag, featuring modern web technologies and 3D graphics.

## Features

- First-person camera controls with mouse look
- WASD movement system
- Collision detection and raycasting for shooting mechanics
- Cross-platform web compatibility
- Responsive window handling
- Debug information display
- Crosshair targeting system

## Project Structure

```
.
├── assets/
│   └── models/
│       └── environment/
├── game/
│   ├── __init__.py
│   ├── collision_manager.py
│   ├── config.py
│   ├── constants.py
│   ├── game.py
│   ├── input_handler.py
│   ├── player.py
│   ├── utils.py
│   ├── web_adapter.py
│   ├── web_game.py
│   └── window_manager.py
├── build.py
├── index.html
├── main.py
├── pygbag.json
├── pyproject.toml
├── requirements.txt
└── serve.py
```

## Technical Details

### Core Components

1. **Game Engine**: Built on Panda3D, a powerful 3D engine and framework
2. **Web Framework**: Uses Pygbag 0.9.2 for web compatibility
3. **Physics**: Basic collision detection system for shooting mechanics
4. **Input System**: Mouse and keyboard handling for FPS controls

### Key Modules

- `game.py`: Core game logic and initialization
- `player.py`: Player movement and camera controls
- `collision_manager.py`: Handles collision detection and raycasting
- `web_adapter.py`: Web-specific adaptations for browser compatibility
- `window_manager.py`: Handles window properties and resizing
- `input_handler.py`: Processes keyboard and mouse input
- `utils.py`: Utility functions for common operations

## Development Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Build the project:
```bash
python build.py
```

3. Run the development server:
```bash
python -m pygbag .
```

## Project Architecture

### Component Overview

1. **Core Game Logic**
   - Main game loop
   - Scene management
   - Asset loading

2. **Player System**
   - Camera controls
   - Movement mechanics
   - Shooting mechanics

3. **Web Integration**
   - Browser compatibility layer
   - Async operations handling
   - Window management

4. **Physics System**
   - Collision detection
   - Raycasting for shooting
   - Basic physics calculations

### Design Patterns

- **Component Pattern**: Separates game elements into reusable components
- **Observer Pattern**: Used for event handling (input system)
- **Singleton Pattern**: Applied to core game systems
- **Factory Pattern**: Used for object creation and management

## Browser Compatibility

The game is designed to run in modern web browsers using Pygbag's Python-to-WebAssembly compilation. Supported browsers:

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## Performance Considerations

- Optimized asset loading
- Efficient collision detection
- Minimal DOM interactions
- Asynchronous operations for smooth gameplay

## Future Improvements

1. **Graphics**
   - Enhanced lighting system
   - More detailed models
   - Particle effects

2. **Gameplay**
   - Advanced physics
   - Enemy AI
   - Multiple weapons

3. **Technical**
   - Better error handling
   - Performance optimizations
   - Enhanced debugging tools

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - feel free to use this code for your own projects.

## Credits

- Built with [Panda3D](https://www.panda3d.org/)
- Web compatibility by [Pygbag](https://pygame-web.github.io/)
- 

---

update to the .readme file for the project
the game/inventory.py, 
game/gui_manager.py, 
and the game/player.py have been updated
