import pygame

from settings import Settings

class Debug:
    def __init__(self):
        self.settings = Settings()
        self.font = pygame.font.Font(size=self.settings.debug_text_size)

    def print(self, surface, info, **kwargs):
        debug_surface = self.font.render(
            str(info), True, self.settings.debug_text_color
        )
        debug_rect = debug_surface.get_rect(**kwargs)

        pygame.draw.rect(surface, self.settings.debug_bg_color, debug_rect)

        surface.blit(debug_surface, debug_rect)