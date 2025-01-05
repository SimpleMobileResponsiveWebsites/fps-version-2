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

---
# development logs:

12/8/24
Update to the readme.md file for the project
Created the game/inventory.py
Created game/gui_manager.py
Updated game/player.py have been updated



-------
# current map configuration

Current Configuration
{
"heightfield_image":"none"
"focal_point":[
0:7
1:4
]
"horizontal_scale":1.5000000000000004
"vertical_scale":235
"polygon_count":100000
"visibility_radius":1000
"max_triangles":100000
"map_details":{
"terrain_type":"desert"
"water_level":0
"vegetation_density":0.5
"buildings":[
0:{
"name":"barracks"
"position":[
0:45
1:50
]
"height":10
}
1:{
"name":"Med Tent"
"position":[
0:450
1:550
]
"height":10
}
2:{
"name":"Med Tent"
"position":[
0:600
1:650
]
"height":10
}
3:{
"name":"Med Tent"
"position":[
0:700
1:750
]
"height":10
}
4:{
"name":"Mechanic"
"position":[
0:800
1:850
]
"height":10
}
5:{
"name":"Armory"
"position":[
0:900
1:901
]
"height":10
}
6:{
"name":"Hangar"
"position":[
0:7
1:4
]
"height":10
}
7:{
"name":"Hospital"
"position":[
0:1200
1:1201
]
"height":30
}
8:{
"name":"Hospital Maintenance Building"
"position":[
0:1290
1:1291
]
"height":10
}
9:{
"name":"Hospital Parcade Shack"
"position":[
0:1300
1:1301
]
"height":10
}
]
"lanes":[]
"points_of_interest":[
0:{
"name":"barracks"
"position":[
0:45
1:50
]
"description":"barracks is a barracks where there a gun crates, ammo crates, helmet crates, tactical rig crates, ballistic vest crates, item crates and additional loot spawns, where players can loot."
}
1:{
"name":"Med Tent"
"position":[
0:450
1:550
]
"description":"Med Tent is where there is medical supply crates that have heals that players can loot."
}
2:{
"name":"Med Tent"
"position":[
0:600
1:650
]
"description":"Med Tent is where there is medical supply crates that have heals that players can loot."
}
3:{
"name":"Med Tent"
"position":[
0:700
1:750
]
"description":"Med Tent is where there is medical supply crates that have heals that players can loot."
}
4:{
"name":"Mechanic"
"position":[
0:800
1:850
]
"description":"Mechanic is an auto repair shop next to the med tents that is now repurposed as a gun parts cache for players to loot weapons parts from crates all over the building.
"
}
5:{
"name":"Hangar"
"position":[
0:7
1:4
]
"description":"Hangar is a point of interest where players spawn at.   Hanger is a military base hanger that has gun parts cache for players to loot weapons parts from crates all over the building, medical supply crates that have heals that players can loot and gun crates, ammo crates, helmet crates, tactical rig crates, ballistic vest crates, item crates and additional loot spawns, where players can loot."
}
6:{
"name":"Hospital"
"position":[
0:1200
1:1201
]
"description":"Hospital is a building, where players and find medical supply crates that have heals that players can loot."
}
7:{
"name":"Hospital Maintenance Building"
"position":[
0:1290
1:1291
]
"description":"Hospital Maintenance Building is where players can find mission items, rare items and rare loot spawns.  "
}
8:{
"name":"Hospital Parcade Shack"
"position":[
0:0
1:0
]
"description":"Hospital Parcade Shack is where players can find mission items, rare items and rare loot spawns,  has gun parts cache for players to loot weapons parts from crates all over the building, medical supply crates that have heals that players can loot and gun crates, ammo crates, helmet crates, tactical rig crates, ballistic vest crates, item crates and additional loot spawns, where players can loot."
}
9:{
"name":"Armory"
"position":[
0:900
1:901
]
"description":"Armory is where the military supply is.  Players can find the bosses, among the compound.  Additionally,  players can find mission items, rare items and rare loot spawns,  has gun parts cache for players to loot weapons parts from crates all over the building, medical supply crates that have heals that players can loot and gun crates, ammo crates, helmet crates, tactical rig crates, ballistic vest crates, item crates and additional loot spawns, where players can loot."
}
]
}
}

