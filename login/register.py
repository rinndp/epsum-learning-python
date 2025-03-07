import hashlib
import json
import os

print("---------------------")
print("CREAR USUARIO")
print("---------------------")

#Comprobar si existe el archivo
if not os.path.exists("users-data"):
    crearArchivo = open("users-data", "x")
    with open("users-data", "w") as file:
        file.write(json.dumps({"listaDeUsuarios": []}, indent=4))

#Cargar el archivo
with open('users-data', "r") as f:
    json_cargado = json.load(f)
    print(json_cargado)

#Comprobar si usuario repetido y guardar usuario
usuario_unico = False
while not usuario_unico:
    usuario_unico = True
    usuario_ingresado = input("Introduzca su usuario:\n")
    for user in json_cargado["listaDeUsuarios"]:
        if user["usuario"] == usuario_ingresado:
            print("Usuario ya EXISTE")
            usuario_unico = False

#Guardar contraseña
password = input("Introduzca su passsword:\n")
passwordHash = hashlib.sha256(password.encode()).hexdigest()

#Guardar JSON actualizado
json_cargado["listaDeUsuarios"].append({"usuario": usuario_ingresado, "password": passwordHash})
print(json_cargado)
with open("users-data", "w") as file:
    file.write(json.dumps(json_cargado, indent=4))