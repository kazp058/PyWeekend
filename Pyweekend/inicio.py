import pygame
import creaMundo as mundo
import algoritmo as pbl
import Configuracion as cfg
import funciones as fn

screen,grupoBordes,grupoRellenos = mundo.crearMundo('mundo.txt')
grupoObstaculos = mundo.crearObstaculo()

poblacion = pbl.crearPoblacion()

font = pygame.font.SysFont("comicsansms", 24)
timer = pygame.time.Clock()
up = down = left = right = space = False

while True:
    timer.tick(cfg.fps)

    for e in pygame.event.get(): #captura los eventos generados
        #verifica que se haya pulsado la X en la esquina superior derecha de la ventana
        if e.type == pygame.QUIT: raise SystemExit("QUIT")
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE: #verifica que el evento sea la tecla ESC
                raise SystemExit("ESCAPE")

    #borra la pantalla
    screen.fill((87,160,211))

    for relleno in grupoRellenos:
        screen.blit(relleno.superficie, relleno.rect)

    for borde in grupoBordes:
        screen.blit(borde.superficie, borde.rect)

    for obstaculo in grupoObstaculos:
        obstaculo.update(grupoBordes, poblacion)
        screen.blit(obstaculo.superficie, obstaculo.rect)

    objetivo = cfg.objetivoFinal
    screen.blit(objetivo.superficie, objetivo.rect)

    if fn.contarMuertos(poblacion) < len(poblacion):
        fn.actualizarPoblacion(poblacion, grupoBordes)
        for individuo in poblacion.sprites()[::-1]:
            if not individuo.muerto:
                screen.blit(individuo.superficie, individuo.rect)
    else:
        padres = pbl.seleccionNatural(poblacion)
        poblacion = pbl.reproducir(padres, len(poblacion))
        if cfg.generaciones % cfg.pasarGeneraciones == 0:
            fn.incrementaMovimientos(poblacion)
        pbl.mutarHijos(poblacion)
        grupoObstaculos = mundo.crearObstaculo()

    mensaje = 'Generaciones: ' + str(cfg.generaciones)
    text = font.render(mensaje, True, (255, 255, 255))
    screen.blit(text,
                (150 - text.get_width() // 2, 50 - text.get_height() // 2))

    if cfg.objetivoAlcanzado:
        mensaje = 'Pasos mínimos: ' + str(cfg.minPasos)
    else:
        mensaje = 'Pasos mínimos: ??'
    text = font.render(mensaje, True, (255, 255, 255))
    screen.blit(text,
                (600 - text.get_width() // 2, 50 - text.get_height() // 2))

    pygame.display.update()