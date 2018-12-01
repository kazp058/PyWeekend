import random as rnd
import Player as ply
import Configuracion as cfg

def crearIndividuo(listaMovimientos):
    '''
    Esta función crea un individuo para la primera generación
    :param listaMovimientos: lista con los movimientos para el jugador
    :return: el jugador
    '''
    return ply.Player(listaMovimientos,(255,0,0),cfg.xPlayer,cfg.yPlayer,12,12)

def crearHijo(padre, color = (0, 255, 0)):
    '''
    Esta función crea un hijo (Player) manteniendo la lista de movimientos del padre
    :param padre: Padre
    :param color: El color del hijo al momento de dibujarlo. El hijo del mejor jugador
                  de la generación anterior debe ser verde. Los hijos de otros padres
                  deben ser rojos
    :return: el hijo
    '''
    return ply.Player(padre.movimientos.copy(), color,cfg.xPlayer,cfg.yPlayer,12,12)

def actualizarPoblacion(poblacion, bordes):
    #actualiza a cada uno de los jugadores de la población
    for individuo in poblacion:
        if not individuo.muerto:
            individuo.update(poblacion, bordes)

def incrementaMovimientos(poblacion):
    '''
    Incrementa el número máximo de movimientos que puede realizar cada jugador.
    Añade a la lista de movimientos de cada jugador los nuevos movimientos que le falta
    :param poblacion: la generación actual
    :return: nada
    '''
    if cfg.maxMovimientos >= cfg.minPasos:
        cfg.maxMovimientos = cfg.minPasos
        for individuo in poblacion:
            individuo.movimientos = individuo.movimientos[:cfg.minPasos]
    else:
        cfg.maxMovimientos += cfg.incMovimientos
        for individuo in poblacion:
            for i in range(cfg.incMovimientos):
                individuo.movimientos.append(rnd.randint(1,4))

def contarMuertos(poblacion):
    '''
    Cuenta cuántos jugadores de la generación actual ya han muerto
    :param poblacion: la generación actual
    :return: el número de jugadores muertos
    '''
    contador = 0
    for individuo in poblacion:
        if individuo.muerto:
            contador += 1
    return contador