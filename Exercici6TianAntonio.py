# Antonio Tian 1DAM presncial
jugador = int(input("Dime cuantos jugadores hay: "))
numCartas = 1
puntuacionTotal = 0
nomGanador = str
puntuacionMax = 0
for i in range(jugador):
    print("------------------------------------------------")
    nombre = input("Dime tu nombre: ")
    puntuacionAccum = 0
    while numCartas != 0:
        puntuacion = 0
        carta = int(
            input("Dime el número de la carta, si no tiene más cartas introduzca 0: "))
        if carta == 0:
            break
        if carta == 1:
            puntuacion += 11
        elif carta == 10:
            puntuacion += 2
        elif carta == 11:
            puntuacion += 3
        elif carta == 12:
            puntuacion += 4
        puntuacionAccum = puntuacionAccum + puntuacion
        if puntuacionAccum >= puntuacionMax:
            nomGanador = nombre
        puntuacionTotal = puntuacionTotal + puntuacion
    print(f"Su puntuacion es {puntuacionAccum}")
print("------------------------------------------------")
print(f"Ha ganado {nomGanador}")
if puntuacionTotal > 120:
    print("Alguien ha hecho trampa")
else:
    print("Falta cartas")
