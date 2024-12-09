"""Web-specific adaptations for Panda3D"""
from direct.showbase.DirectObject import DirectObject
import asyncio

class WebAdapter(DirectObject):
    def __init__(self, game):
        self.game = game
        self.setup_web_handlers()
        self.setup_async_loop()
    
    def setup_web_handlers(self):
        # Handle window resize
        self.accept('window-event', self.handle_window_event)
        
        # Handle browser-specific events
        self.accept('browser-quit', self.handle_quit)
    
    def setup_async_loop(self):
        """Setup async event loop for web compatibility"""
        self.loop = asyncio.get_event_loop()
        self.game.taskMgr.setupTaskChain('async', 
                                       numThreads=0,
                                       frameSync=True,
                                       threadPriority=None)
    
    async def run_async(self, coro):
        """Run coroutine in async task chain"""
        try:
            await coro
        except Exception as e:
            print(f"Async error: {e}")
    
    def handle_window_event(self, window):
        """Handle window resize events"""
        props = window.getProperties()
        if props.getXSize() != self.game.win.getXSize() or props.getYSize() != self.game.win.getYSize():
            self.game.window_manager.update_window_size(props.getXSize(), props.getYSize())
    
    def handle_quit(self):
        """Handle browser quit event"""
        self.game.cleanup()
        self.game.userExit()