import pygame
import algoritmo as pbl
import Configuracion as cfg
import Objetivo as objetivo

class Player(pygame.sprite.Sprite):
    def __init__(self, movimientos, color, x, y, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.ancho = ancho
        self.alto = alto
        self.movimientos = movimientos #lista de movimientos aleatorios
        self.idxMovimientos = 0 #índice del siguiente movimiento a realizar
        self.pasos = 0 #número de movimientos hechos por el jugador
        self.salud = -1 #el valor del salud del jugador. Más alto es mejor
        self.alcanzoObjetivo = False #resolvió el problema o no?
        self.grupoObjetivos = self.crearObjetivos()

        self.muerto = False #sigue activo el jugador

        self.velocidad = 7 #velocidad en pixeles del jugador

        self.superficie = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
        self.superficie.fill(color)
        pygame.draw.rect(self.superficie, (0,0,0), pygame.Rect(0,0,self.ancho,self.alto),1)

        self.rect = pygame.Rect(x, y, self.ancho, self.alto)

    def update(self, poblacion, bordes):
        if self.muerto or len(self.movimientos) == 0:
            return
        movimiento = self.movimientos[self.idxMovimientos]
        up = down = left = right = False
        if movimiento == 3:
            # movimiento a la izquierda
            self.rect.x -= self.velocidad
            left = True
        elif movimiento == 4:
            # movimiento a la derecha
            self.rect.x += self.velocidad
            right = True
        elif movimiento == 1:
            # movimiento arriba
            self.rect.y -= self.velocidad
            up = True
        elif movimiento == 2:
            # movimiento abajo
            self.rect.y += self.velocidad
            down = True

        #verifica colisión con los bordes
        self.colisionar(up, down, left, right, bordes)
        #incremento los pasos
        self.pasos += 1
        #incremento indice
        self.idxMovimientos += 1
        if self.idxMovimientos == len(self.movimientos):
            self.muerto = True

    def colisionar(self, up, down, left, right, bordes):
        block_hit_list = pygame.sprite.spritecollide(self, bordes, False)

        if len(block_hit_list) > 0:
            borde = block_hit_list[0]
            if left:
                self.rect.x = borde.rect.right
            elif right:
                self.rect.x = borde.rect.left - self.ancho
            elif up:
                self.rect.y = borde.rect.bottom
            elif down:
                self.rect.y = borde.rect.top - self.alto

        pygame.sprite.spritecollide(self, self.grupoObjetivos, True)
        if len(self.grupoObjetivos) == 0:
            self.alcanzoObjetivo = True
            self.muerto = True
            cfg.objetivoAlcanzado = True
            if self.pasos < cfg.minPasos:
                cfg.minPasos = self.pasos

    def crearObjetivos(self):
        grupoObjetivos = pygame.sprite.Group()
        objetivoFinal = objetivo.Objetivo((255, 255, 0), 595, 140, 26, 26, True)
        grupoObjetivos.add(objetivoFinal)

        if cfg.objetivoFinal == None:
            cfg.objetivoFinal = objetivoFinal

        listaObjetivos = grupoObjetivos.sprites()
        for i in range(1, len(listaObjetivos)):
            listaObjetivos[i].distanciaFin = listaObjetivos[i - 1].distanciaFin + \
                                             pbl.calcularDistancia(listaObjetivos[i - 1],listaObjetivos[i])

        return grupoObjetivos

