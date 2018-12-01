import pygame

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, color, x, y, ancho, alto, izq):
        pygame.sprite.Sprite.__init__(self)
        self.ancho = ancho
        self.alto = alto
        self.izq = izq
        self.velocidad = 5

        self.superficie = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        pygame.draw.circle(self.superficie, color, (ancho//2,alto//2), ancho//2)

        self.rect = pygame.Rect(x, y, self.ancho, self.alto)

    def update(self, bordes, poblacion):
        if self.izq:
            self.rect.x -= self.velocidad
        else:
            self.rect.x += self.velocidad
        self.colisionar(bordes, poblacion)

    def colisionar(self, bordes, poblacion):
        blocks_hit_list = pygame.sprite.spritecollide(self, bordes, False)

        if len(blocks_hit_list) > 0:
            if self.izq:
                self.rect.x = blocks_hit_list[0].rect.right
            else:
                self.rect.x = blocks_hit_list[0].rect.left - self.ancho
            self.izq = not self.izq

        blocks_hit_list = pygame.sprite.spritecollide(self, poblacion, False)
        for elem in blocks_hit_list:
            elem.muerto = True