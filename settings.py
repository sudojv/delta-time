class Settings:
    def __init__(self):
        # screen settings
        self.FPS = 30
        self.TARGET_FPS = 60
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.screen_size = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.screen_caption = 'Delta time in PyGame (PRESS SPACE!)'
        self.screen_color = 'black'
        # debug settings
        self.debug_text_size = 30
        self.debug_text_color = 'white'
        self.debug_bg_color = 'black'
        # rect settings
        self.rect_width = 100
        self.rect_height = 100
        self.rect_color = 'white'
        self.rect_speed = 5