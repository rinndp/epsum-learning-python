import random

print("--------------------------------------------------------------------------------")
print("Bienvenido al juego de ADVINAR el número (1, 100) ")
print("TIENES 5 INTENTOS")
print("--------------------------------------------------------------------------------")
numeroParaAdivinar = random.randint(1, 100)
numeroIngresado = 0
intentos = 0
continuar = True
while continuar:
    if intentos > 5:
        print("HAS SUPERADO EL NÚMERO DE INTENTOS RETRASAO ERES MALÍSIMO")
        continuar = False

    print(f"INTENTO: {intentos}")
    numeroIngresado = int(input("Ingrese un número:\n"))
    if numeroParaAdivinar == numeroIngresado:
        print("--------------------------------------------------------------------------------")
        print(f"HAS ADIVINADO -- EL NÚMERO ERA: {numeroParaAdivinar} -- 😈 FELICITACIONES 😈")
        print("--------------------------------------------------------------------------------")
        continuar = False

    if numeroParaAdivinar > numeroIngresado:
        print("- ⬆️ MÁS ALTO ⬆️ -")
    else:
        print("- ⬇️ MÁS BAJO ⬇️ -")
    intentos += 1
    print("----------------------------------------------------")


