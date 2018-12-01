import pygame
import Borde as borde
import Relleno as relleno
import Obstaculo as obstaculo

def crearMundo(archivo):
    pygame.init()
    grupoBordes = pygame.sprite.Group()
    grupoRellenos = pygame.sprite.Group()

    with open(archivo, 'r') as f:
        f.readline()
        ancho,alto = f.readline().strip().split(',')
        ancho = int(ancho)
        alto = int(alto)
        screen = pygame.display.set_mode((ancho, alto))
        f.readline()
        xIni,yIni = f.readline().strip().split(',')
        xIni = int(xIni)
        yIni = int(yIni)
        f.readline()
        espesor = int(f.readline().strip())
        linea = f.readline().strip()
        if linea == '#Rellenos':
            linea = f.readline().strip()
            while linea != '#Bordes':
                linea = f.readline().strip()
                if linea != '#Bordes':
                    x,y,ancho,alto,color = linea.split(',')
                    x = int(x)
                    y = int(y)
                    ancho = int(ancho)
                    alto = int(alto)
                    r,g,b = color.split('-')
                    color = (int(r), int(g), int(b))
                    grupoRellenos.add(relleno.Relleno(color, x + xIni, y + yIni,ancho, alto))
        f.readline()
        f.readline()
        f.readline()
        for linea in f:
            # tipo_linea,longitud,x,y (en pixeles)
            tipoLinea,longitud,x,y = linea.split(',')
            tipoLinea = int(tipoLinea)
            longitud = int(longitud)
            x = int(x)
            y = int(y)
            color = (0,0,0) #negro
            if tipoLinea == 1:
                ancho = longitud
                alto = espesor
            elif tipoLinea == 2:
                ancho = espesor
                alto = longitud
            grupoBordes.add(borde.Borde(color, x + xIni, y + yIni, ancho, alto))
    return (screen, grupoBordes, grupoRellenos)

def crearObstaculo():
    grupoObstaculos = pygame.sprite.Group()
    # x,y,ancho,alto,color,izq/der
    grupoObstaculos.add(obstaculo.Obstaculo((0, 0, 128), 140 + 100, 40 + 140, 25, 25, False))
    grupoObstaculos.add(obstaculo.Obstaculo((0, 0, 128), 437 + 100, 73 + 140, 25, 25, True))
    grupoObstaculos.add(obstaculo.Obstaculo((0, 0, 128), 140 + 100, 106 + 140, 25, 25, False))
    grupoObstaculos.add(obstaculo.Obstaculo((0, 0, 128), 437 + 100, 139 + 140, 25, 25, True))
    return grupoObstaculos