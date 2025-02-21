import colorama
from colorama import Fore, Back, Style

monedas = [2, 1, 0.50, 0.20, 0.10, 0.05]
billetesValidos = [5, 10]
cantidadMonedasTipo = [20, 20, 20, 20, 20, 20]
nombreProductos = [
    "Agua 💧",
    "CocaCola 🥤",
    "Nestea 🍹",
    "Fanta 🍊",
    "Café ☕",
    "Aquarius 🔵",
    "Agua con gas 🫧",
    "Zumo de naranja 🍊"]
precioProductos = [1, 3, 2.5 , 3, 2.5, 2, 1.25, 2]

def printBebidas():
    print("----------------------------------------------------------")
    print("MÁQUINA DE BEBIDAS (no se aceptan billetes de mas de 10€)")
    print("----------------------------------------------------------")

    for i in range(0, len(nombreProductos)):
        print(f"[{i+1}] {nombreProductos[i]} -- {precioProductos[i]}€")

    print("-----------------------------")


while True:

    #SELECCIÓN DE BEBIDA

    bebidaValida = False
    while not bebidaValida:
        printBebidas()
        indexBebidaSeleccionada = int(input("Elija la bebida que desea: ")) - 1
        if indexBebidaSeleccionada not in range(0, len(nombreProductos)):
            print("-----------------------------")
            print(f"\033[31mPRODUCTO NO IDENTIFICADO\033[0m")
            bebidaValida = False
        else:
            print("-----------------------------")
            print(f"Ha selecionado la bebida: {nombreProductos[indexBebidaSeleccionada]}")
            print(f"Importe por introducir: {precioProductos[indexBebidaSeleccionada]}€")
            print("-----------------------------")
            bebidaValida = True



    #CHECK SI CAMBIO INSUFICIENTE

    precioBebidaPagado = False
    dineroAcumulado = 0
    mensajePrecioExacto = ""
    contadorTipoMonedasVacias = 0

    for i in range(len(cantidadMonedasTipo)):
        if cantidadMonedasTipo[i] == 0:
            contadorTipoMonedasVacias += 1

    if contadorTipoMonedasVacias == 2 or cantidadMonedasTipo[len(cantidadMonedasTipo)-1] == 0:
        mensajePrecioExacto = "\033[31m - SOLO PRECIOS EXACTOS (CAMBIO INSUFICIENTE) - \033[0m"

    #COBRO DE LA BEBIDA

    while not precioBebidaPagado:
        dineroIntroducido = float(input(f"INTRODUZCA MONEDA O BILLETE{mensajePrecioExacto}: "))
        if dineroIntroducido not in monedas and dineroIntroducido not in billetesValidos:
            print(f"\033[31mVALOR NO VÁLIDO\033[0m")
        else:
            for i in range(0, len(monedas)):
                if dineroIntroducido == monedas[i]:
                    cantidadMonedasTipo[i] += 1
            dineroAcumulado += dineroIntroducido
            print(f"Dinero introducido: {round(dineroAcumulado,4)}€")
            if dineroAcumulado >= precioProductos[indexBebidaSeleccionada]:
                precioBebidaPagado = True


    # CAMBIO AL CLIENTE

    cambioDevuelto = False
    cambio = dineroAcumulado - precioProductos[indexBebidaSeleccionada]
    roundedCambio = round(cambio,2)
    if cambio == 0:
        cambioDevuelto = True

    while not cambioDevuelto:
        print("-----------------------------")
        print(f"Cambio por devolver: {roundedCambio}€")
        print("-----------------------------")

        for i in range(len(monedas)):
            if monedas[i] <= roundedCambio:
                while roundedCambio - monedas[i] >= 0 and cantidadMonedasTipo[i] > 0:
                    cantidadMonedasTipo[i] -= 1
                    print(f"Se ha devuelto una moneda: {monedas[i]}€")
                    roundedCambio = round(roundedCambio - monedas[i], 2)
                    print(f"Cambio por devolver: {roundedCambio}€")
            if roundedCambio == 0:
                cambioDevuelto = True

    #MENSAJE FINAL

    print("-----------------------------")
    print("¡MUCHAS GRACIAS POR SU COMPRA!")
    print(f"\033[32m{monedas}\033[0m")
    print(f"\033[32m{cantidadMonedasTipo}\033[0m")




