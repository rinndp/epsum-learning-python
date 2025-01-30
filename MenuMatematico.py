from getpass import fallback_getpass

print("------------------------------------")
print("MENÚ MATEMATICO")
print("------------------------------------")

continuar = True

def calcularPrimo(numeroExaminarPrimo):
    print("-------------------------------")
    if (numeroExaminarPrimo > 0
            and numeroExaminarPrimo % numeroExaminarPrimo == 0
            and numeroExaminarPrimo % 2 != 0
            or numeroExaminarPrimo == 2):
        print(f"El número '{numeroExaminarPrimo}' ES primo")
    else:
        print(f"El número '{numeroExaminarPrimo}' NO primo'")
    print("-------------------------------")

def calcularPar (numeroExaminarPar):
    print("-------------------------------")
    if numeroExaminarPar > 0 and numeroExaminarPar % 2 == 0:
        print(f"El número '{numeroExaminarPar}' ES par")
    else:
        print(f"El número '{numeroExaminarPar}' NO par")
    print("-------------------------------")

def calcularYearBisiesto (yearExaminarBisiesto):
    print("-------------------------------")
    if yearExaminarBisiesto % 400 == 0 or yearExaminarBisiesto % 100 != 0 and yearExaminarBisiesto % 4 == 0:
        print(f"El año '{yearExaminarBisiesto}' es bisiesto")
    else:
        print(f"El año {yearExaminarBisiesto} NO es bisiesto")
    print("-------------------------------")

while continuar:
    print("[ 1 ] - Calcula si el número es primo")
    print("[ 2 ] - Calcula si el número es par")
    print("[ 3 ] - Calcula si el año es bisiesto")
    print("[ 4 ] - Salir\n")

    indiceMenu = int(input("Introduce un número del menú: "))

    if indiceMenu == 1:
        numeroExaminarPrimo = int(input("Introduce el número para saber si es primo: "))
        calcularPrimo(numeroExaminarPrimo)

    elif indiceMenu == 2:
        numeroExaminarPar = int(input("Introduce el número para saber si es par: "))
        calcularPar(numeroExaminarPar)

    elif indiceMenu == 3:
        yearExaminarBisiesto = int(input("Introduce el año: "))
        calcularYearBisiesto(yearExaminarBisiesto)

    elif indiceMenu == 4:
        continuar = False

    else:
        print("-------------------------------")
        print("NÚMERO NO VÁLIDO")
        print("-------------------------------")