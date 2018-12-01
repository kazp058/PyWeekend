import pygame
import Configuracion as cfg

class Objetivo(pygame.sprite.Sprite):
    def __init__(self, color, x, y, ancho, alto, final = False):
        pygame.sprite.Sprite.__init__(self)
        self.ancho = ancho
        self.alto = alto
        self.alcanzado = False
        self.final = final #es este el objetivo final o no?
        if final:
            self.distanciaFin = 0
        else:
            self.distanciaFin = 10000

        self.superficie = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        self.superficie.fill(color)

        self.rect = pygame.Rect(x, y, self.ancho, self.alto)