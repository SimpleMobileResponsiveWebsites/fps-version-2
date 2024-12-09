import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000

def serve():
    """Serve the game locally"""
    build_dir = Path('build')
    
    if not build_dir.exists():
        print("Build directory not found. Running build first...")
        from build import prepare_build
        prepare_build()
    
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    serve()