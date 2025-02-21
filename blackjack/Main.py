from threading import Thread

from blackjack.Carta import Carta
import random
import time

baraja = []
palos = ["♣️", "♠️", "♥️", "♦️"]
letras = ["J", "Q", "K", "A"]

barajaCasa = []
barajaJugador = []

def rellenar_baraja():
    for palo in palos:
        for i in range(2, 11):
            baraja.append(Carta(i, palo, f"{i} de {palo}"))

        for letra in letras:
            baraja.append(Carta(letra, palo, f"{letra} de {palo}"))

def barajear(baraja):
    random.shuffle(baraja)


def valor_baraja(baraja):
    suma_baraja = 0
    for carta in baraja:
        valor_carta = carta.valor
        if carta.valor == "K" or carta.valor == "J" or carta.valor == "Q":
            valor_carta = 10

        if carta.valor == "A":
            if (suma_baraja + 11) > 21:
                valor_carta = 1
            else:
                valor_carta = 11

        suma_baraja = suma_baraja + valor_carta

    return suma_baraja

def repartir_carta(baraja, to_baraja):
    nombre = ""
    if to_baraja == barajaCasa:
        nombre = "cupier"
    if to_baraja == barajaJugador:
        nombre = "jugador"
    print(f"repartiendo carta al {nombre}...")
    time.sleep(3)
    carta_sacada = baraja.pop()
    to_baraja.append(carta_sacada)
    print(f"LA CARTA ES UN -> {carta_sacada.nombre}")
    print("-----------------------------------------")
    print(f"La suma de la baraja del {nombre_jugador(to_baraja)} es: {valor_baraja(to_baraja)}")
    print("-----------------------------------------")

def nombre_jugador(baraja):
    nombre = ""
    if baraja == barajaCasa:
        nombre = "cupier"
    if baraja == barajaJugador:
        nombre = "jugador"

    return nombre

def inicio_partida():
    for i in range (0, 2):
        repartir_carta(baraja, barajaJugador)

def comprobar_valor_baraja():
    if valor_baraja(barajaJugador) > 21:
        print("EL JUGADOR HA PERDIDO")
        exit(0)
    if valor_baraja(barajaCasa) > 21:
        print("EL CUPIER HA PERDIDO")
        exit(0)

def comprobar_ganador():
    if valor_baraja(barajaJugador) > valor_baraja(barajaCasa):
        print("-----------------------------------------")
        print("EL JUGADOR GANA")
        print("-----------------------------------------")
        exit(0)
    else:
        print("-----------------------------------------")
        print("EL CUPIER GANA")
        print("-----------------------------------------")
        exit(0)


print("--------------------------------------------")
print("ES HORA DE JUGA AL BLACKJACK ¿ESTÁS LISTO?")
print("--------------------------------------------")
rellenar_baraja()
barajear(baraja)

inicio_partida()
repartir_carta(baraja, barajaCasa)

resp_plantarse = ""
plantarse = False
while valor_baraja(barajaJugador) < 21 and plantarse == False:
    resp_plantarse = input("¿Te quieres plantar? (S/N)")
    if resp_plantarse.lower() == "n":
        repartir_carta(baraja, barajaJugador)
        comprobar_valor_baraja()
    else:
        plantarse = True
        print("")
        print("--------------------------------------------")
        print("El jugador se ha cagado que flipas")
        print("--------------------------------------------")
        print("")
        time.sleep(1)


if valor_baraja(barajaCasa) >= 17:
    print("El cupier TAMBIÉN se caga")
    comprobar_ganador()
else:
    while valor_baraja(barajaCasa) < 17 or valor_baraja(barajaJugador) == 21:
        repartir_carta(baraja, barajaCasa)
        comprobar_valor_baraja()

comprobar_ganador()



