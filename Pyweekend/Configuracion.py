#velocidad de la animación (frames por segundos). Mayor el valor, más rápida la animación
fps = 60

#Tamaño inicial de la población
cuantos = 100

#máximo número de movimientos permitidos para un jugador
maxMovimientos = 10

#incremento en el número máximo de movimientos que reciben los jugadores
incMovimientos = 10

#número de generaciones que tienen que pasar para recibir incremento de movimientos
#Por ejemplo, si pasarGeneraciones es 5, cada 5 generaciones los jugadores reciben
#el incremento de movimientos.
pasarGeneraciones = 5

#número de generaciones que han pasado
generaciones = 0

#probabilidad de mutación de la generación. Debe ser entre 0 y 1
#usted puede cambiar este valor para obtener resultados diferentes en sus experimentos
probMutacion = 0.05

#número de pasos mínimos para resolver el problema
minPasos = 10000000000

#x,y original del jugador
xPlayer = 137 #137
yPlayer = 145 #145
#x,y del objetivo
xObjetivo = 595 #137 #495
yObjetivo = 140 #337 #140

#Objetivo alcanzado
objetivoAlcanzado = False

#Mejor jugador
mejor = None

#Objetivo final
objetivoFinal = None