import pygame

from settings import Settings
from delta_time import DeltaTime
from debug import Debug

class Game:
    def __init__(self):
        self.settings = Settings()
        self.delta_time = DeltaTime()
        self.debug = Debug()

        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption(self.settings.screen_caption)

        self.clock = pygame.time.Clock()

        self.running = True

    def run(self):
        while self.running:
            self._update_events()
            self._update_screen()

    def _update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def _update_screen(self):
        self.screen.fill(self.settings.screen_color)
        
        self.delta_time.update()

        self._print_debug()

        pygame.display.flip()
        
        self.clock.tick(self.settings.FPS)

    def _print_debug(self):
        fps_info = f'FPS: {self.clock.get_fps():.1f}'
        self.debug.print(self.screen, fps_info)

        delta_time_info = f'DT: {self.delta_time.get():.4f}'
        self.debug.print(self.screen, delta_time_info, y_offset=25)

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()