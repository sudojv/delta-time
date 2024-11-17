import pygame

class Counter:
    def __init__(self):
        self.starting = 0
        self.ending = 0
    
    def start(self):
        self.starting = pygame.time.get_ticks()
    
    def end(self):
        self.ending = pygame.time.get_ticks() - self.starting

    def duration(self):
        return self.ending / 1000