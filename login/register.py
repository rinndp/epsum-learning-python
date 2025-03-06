import hashlib
import json
import os

print("---------------------")
print("CREAR USUARIO")
print("---------------------")

if not os.path.exists("users-data"):
    crearArchivo = open("users-data", "x")
    with open("users-data", "w") as file:
        file.write(json.dumps({"listaDeUsuarios": []}, indent=4))

with open('users-data', "r") as f:
    json_cargado = json.load(f)
    print(json_cargado)

usuario_unico = False
while not usuario_unico:
    usuario_unico = True
    usuario_ingresado = input("Introduzca su usuario:\n")
    for user in json_cargado["listaDeUsuarios"]:
        print(user["usuario"])
        if user["usuario"] == usuario_ingresado:
            usuario_unico = False

password = input("Introduzca su passsword:\n")
passwordHash = hashlib.sha256(password.encode()).hexdigest()

json_cargado["listaDeUsuarios"].append({"usuario": usuario_ingresado, "password": passwordHash})
print(json_cargado)
with open("users-data", "w") as file:
    file.write(json.dumps(json_cargado, indent=4))