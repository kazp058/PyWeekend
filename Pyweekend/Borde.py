import pygame

class Borde(pygame.sprite.Sprite):
    def __init__(self, color, x, y, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.ancho = ancho
        self.alto = alto

        self.superficie = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        self.superficie.fill(color)

        self.rect = pygame.Rect(x, y, self.ancho, self.alto)
