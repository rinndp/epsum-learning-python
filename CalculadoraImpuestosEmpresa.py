print("------------------------------------")
print("CALCULADORA IMPUESTOS  Y GASTOS EMPRESA ")
print("------------------------------------")

cabeceras = ["Nombre del trabajador", "Sueldo neto del trabajador"]
trabajadores = []
continuar = True

def calcularSueldoNeto(sueldoBrutoMensual):

    descontadoIRPF = sueldoBrutoMensual * 0.12
    descontadoSeguridadSocial = sueldoBrutoMensual * 0.052
    descuentoTotal = descontadoIRPF + descontadoSeguridadSocial
    sueldoNeto = sueldoBrutoMensual - descuentoTotal

    return sueldoNeto,descontadoIRPF, descontadoSeguridadSocial

valoresEmpleado = []
sueldoBrutoMensual = 0
totalSueldosNetos = 0
totalIRPF = 0
totalSS = 0

while continuar:
    sueldoBrutoMensual = float(input("Introduce su sueldo bruto mensual:\n"))
    if sueldoBrutoMensual >= 0:
        nombreEmpleado = input("Introduce el nombre del empleado:\n")

        valoresEmpleado = calcularSueldoNeto(sueldoBrutoMensual)
        totalSueldosNetos += valoresEmpleado[0]
        totalIRPF += valoresEmpleado[1]
        totalSS += valoresEmpleado[2]
        trabajador = [nombreEmpleado, valoresEmpleado[0]]
        trabajadores.append(trabajador)

    continuarResp = input("¿Desea continuar? (Para salir pulse 'N'):\n")
    if continuarResp.lower() == "n":
        continuar = False

print(cabeceras)
for i in trabajadores:
    print(i)

print(f"\nTotal de IRPF: {round(totalIRPF)}€")
print(f"Total de SS: {round(totalSS)}€")
print(f"Inversión de la empresa: {round(totalSueldosNetos)}€")



