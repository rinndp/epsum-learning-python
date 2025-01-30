print("------------------------------------")
print("CALCULADORA SUELDO NETO")
print("------------------------------------")

nombreEmpleado = input("Introduce el nombre del empleado:\n")
sueldoBrutoMensual = float(input("Introduce su sueldo bruto mensual:\n"))

def descontarImpuestos (sueldoBrutoMensual):
    descontadoIRPF = sueldoBrutoMensual * 0.12
    descontadoSeguridadSocial = sueldoBrutoMensual * 0.052
    descuentoTotal = descontadoIRPF + descontadoSeguridadSocial
    sueldoNeto = sueldoBrutoMensual - descuentoTotal
    return sueldoNeto

print(f"El sueldo neto de {nombreEmpleado} es: {descontarImpuestos(sueldoBrutoMensual)}€")

