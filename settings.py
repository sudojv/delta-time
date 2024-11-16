class Settings:
    def __init__(self):
        # screen settings
        self.FPS = 60
        self.WIDTH = 640
        self.HEIGHT = 480
        self.screen_size = (self.WIDTH, self.HEIGHT)
        self.screen_caption = 'Delta time in PyGame'
        self.screen_color = 'black'
        # debug settings
        self.debug_text_size = 20
        self.debug_text_color = 'white'
        self.debug_bg_color = 'black'