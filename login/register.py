import hashlib
import json
import os

print("---------------------")
print("CREAR USUARIO")
print("---------------------")

if (not os.path.exists("users-data")):
    crearArchivo = open("users-data", "x")

with open('users-data') as f:
    json_cargado = json.load(f)
    print(json_cargado)

usuario_unico = False
while usuario_unico == False:
    usuario_unico = True
    usuario_ingresado = input("Introduzca su usuario:\n")
    for user in json_cargado:
        print(user)



password = input("Introduzca su passsword:\n")
passwordHash = hashlib.sha256(password.encode()).hexdigest()
with open("users-data", "a") as file:
    file.write(json.dumps(
        {"usuario": usuario_ingresado,
         "password": passwordHash
         }, indent=4))