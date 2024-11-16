import pygame

from settings import Settings

class Debug:
    def __init__(self):
        self.settings = Settings()
        self.font = pygame.font.Font(size=self.settings.debug_text_size)

    def print(self, surface, info, x_offset=5, y_offset=5):
        debug_surface = self.font.render(
            str(info), True, self.settings.debug_text_color
        )
        debug_rect = debug_surface.get_rect(topleft=(x_offset, y_offset))

        pygame.draw.rect(surface, self.settings.debug_bg_color, debug_rect)

        surface.blit(debug_surface, debug_rect)