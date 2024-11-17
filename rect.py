import pygame

from settings import Settings
from debug import Debug
from counter import Counter

class Rect:
    def __init__(self, game):
        self.surface:pygame.Surface = game.screen
        self.surface_rect = self.surface.get_rect()

        self.settings = Settings()
        self.debug = Debug()
        self.timer = Counter()

        self.delta_time = game.delta_time
        
        self.rect = pygame.rect.Rect(0, 0,
            self.settings.rect_width, self.settings.rect_height
        )

        self.rect.centery = self.surface_rect.centery

        self.moving = False
        self.already_moved = False

    def update(self):
        if self.is_moving():
            if not self._get_right_wall_collision():
                self.rect.centerx += self._get_speed()
            else: 
                self.end_moving()

    def _get_right_wall_collision(self):
        return True if self.rect.right >= self.surface_rect.right else False
    
    def _get_speed(self):
        speed = self.settings.rect_speed * self.delta_time.get()
        return speed * self.settings.TARGET_FPS

    def start_moving(self):
        self.already_moved = True
        self.moving = True
        self.timer.start()

    def end_moving(self):
        self.moving = False
        self.timer.end()

    def is_moving(self):
        return self.moving

    def is_already_moved(self):
        return self.already_moved

    def blit(self):
        if self._get_right_wall_collision():
            self.debug.print(
                self.surface,
                f'{self.timer.duration():.2f}',
                center=self.surface_rect.center
            )

        pygame.draw.rect(self.surface, self.settings.rect_color, self.rect)