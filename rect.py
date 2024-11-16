import pygame
import time

from settings import Settings
from debug import Debug

class Rect:
    def __init__(self, game):
        self.surface:pygame.Surface = game.screen
        self.surface_rect = self.surface.get_rect()

        self.settings = Settings()
        self.debug = Debug()
        self.delta_time = game.delta_time
        
        self.rect = pygame.rect.Rect(0, 0,
            self.settings.rect_width, self.settings.rect_height
        )

        self.rect.centery = self.surface_rect.centery

        self.counter_start = 0
        self.counter_end = 0

        self.moving = False

    def update(self):
        if self.moving:
            if self.counter_start == 0:
                self.counter_start = time.time()
            if self.rect.right < self.surface_rect.right:
                speed = self.settings.rect_speed * self.delta_time.get() 
                self.rect.centerx += speed * self.settings.TARGET_FPS
            else: 
                self.counter_end = time.time() - self.counter_start
                self.moving = False

    def blit(self):
        self.debug.print(
            self.surface,
            f'{self.counter_end:.2f}',
            self.surface_rect.centerx,
            self.surface_rect.centery
        )
        pygame.draw.rect(self.surface, self.settings.rect_color, self.rect)