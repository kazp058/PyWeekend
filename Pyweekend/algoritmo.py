import math
import pygame
import random as rnd
import Configuracion as cfg
import funciones as fn
import calculos as fo

def crearPoblacion():
    poblacion = pygame.sprite.Group()
    cfg.generaciones = 1
    for i in range(cfg.cuantos):
        lista = []
        for k in range(cfg.maxMovimientos+1):
           movimiento=rnd.randint(1,4)
           lista.append(movimiento)
        poblacion.add(fn.crearIndividuo(lista))
    return poblacion
def calcularSalud(individuo):
    individuo.salud = 0
    xo=individuo.rect.x
    yo=individuo.rect.y
    x=cfg.xObjetivo
    y=cfg.yObjetivo
    distancia=fo.calculo(x,y,xo,yo)
    distanciao=fo.calculo(xo,yo,cfg.xPlayer,cfg.yPlayer)
    if distanciao != 0:
        individuo.salud=(distancia/distanciao)
    else:
        individuo.salud= distancia

def seleccionNatural(poblacion):
    listaPadres = [] ; listapuntos=[] ; listapapa=[] ; populi=[]
    for individuo in poblacion:
        populi.append(individuo)
        calcularSalud(individuo)
        listapuntos.append(individuo.salud)
    listapoints=sorted(listapuntos)
    long=len(listapoints)//2
    listamejores=listapoints[:2]
    listapeores=listapoints[:-2]
    mejores = len(listamejores)
    peores=len(listapeores)
    mejoreslong=mejores
    peoreslong=(peores*20)//100
    for i in range(1,(mejoreslong+1)):
        listaPadres.append(listamejores[rnd.randint(0,mejores-1)])
    for i in range(1,peoreslong+1):
        listaPadres.append(listapeores[rnd.randint(0,peores-1)])
    for k in listaPadres:
        a=listapuntos.index(k)
        listapapa.append(populi[a])
    return listapapa

def reproducir(padres, cuantos):
    nuevaPoblacion = pygame.sprite.Group()
    cfg.generaciones += 1
    cantidadpadres=len(padres)-1
    nuevaPoblacion.add(fn.crearHijo(padres[0]))
    for idx in range(cuantos-1):
        hijo = []
        didx = rnd.randint(0,cantidadpadres)
        midx = rnd.randint(0,cantidadpadres)
        padre = padres[didx].movimientos
        madre = padres[midx].movimientos
        a=cfg.maxMovimientos
        for gene in range(a):
            probGene = rnd.randint(0,1)
            if probGene == 1:
                hijo.append(padre[gene])
            elif probGene == 0:
                hijo.append(madre[gene])
        nuevaPoblacion.add(fn.crearIndividuo(hijo))
    return nuevaPoblacion

def mutarHijos(poblacion):
    for individuo in poblacion:
        mutarMovimientos(individuo, cfg.probMutacion)

def mutarMovimientos(individuo, probabilidad):
    k=rnd.random()
    if k>=probabilidad:
        l=rnd.randint(1,4)
        indx=rnd.randint(0,cfg.maxMovimientos-1)
        individuo.movimientos[indx]=l