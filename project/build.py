import os
import shutil
from pathlib import Path

def prepare_build():
    """Prepare the build directory"""
    build_dir = Path('build')
    
    # Create build directory
    build_dir.mkdir(exist_ok=True)
    
    # Copy required files
    files_to_copy = [
        'main.py',
        'requirements.txt',
        'index.html',
        'pygbag.json',
        'game',
        'assets'
    ]
    
    for file in files_to_copy:
        src = Path(file)
        dst = build_dir / src
        
        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

if __name__ == '__main__':
    prepare_build()