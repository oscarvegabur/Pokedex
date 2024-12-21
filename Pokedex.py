import requests
import os
import json

#con este codigo se crea la carpeta pokedex si no existe dicha carpeta
if not os.path.exists("pokedex"):
    os.makedirs("pokedex")

#Aqui empezarmo por obtener los datos de los pokemon desde la API
def obtener_datos_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        print("Error: No se encuentra un pokemon")
        return None
#Aqui guardamos los datos de los pokemon en un archivo JSOn
def guardar_datos_json(nombre, datos):
    archivo = f"pokedex/{nombre.lower()}.json"
    with open(archivo, "w") as archivo_json:
        json.dump(datos, archivo_json, indent=4)
        print(f"Datos de {nombre.capitalize()} guardados en {archivo}")

#Se define la funcon primaria para buscar y mostrar la informacion de los pokemon
def buscar_pokemon():
    nombre = input("Nombra algun pokemon: ").strip()
    datos = obtener_datos_pokemon(nombre)
#Se obitienen los datos que nos piden
    if datos:
        peso = datos["weight"]
        altura = datos["height"]
        movimientos = [movimiento["move"]["name"] for movimiento in datos["moves"]]
        habilidades = [habilidad["ability"]["name"] for habilidad in datos["abilities"]]
        tipos = [tipo["type"]["name"] for tipo in datos["types"]]
        imagen = datos["sprites"]["front_default"]
#mostramos los datos solicitados
        print(f"\nInformacion de {nombre.capitalize()}:")
        print(f"- Peso: {peso} Kg.")
        print(f"- Altura: {altura} M.")
        print(f"- Movimientos: {'.'.join(movimientos[:5])}...")
        print(f"- Tipos: {'.'.join(tipos)}")
        print(f"- Imagen: {imagen}\n")
#SE guardan los daots en archivo JSON
        datos_guardar = {
            "nombre": nombre.capitalize(),
            "peso" : peso,
            "altura" : altura,
            "movimientos": movimientos,
            "tipos": tipos,
            "imagen": imagen,
            }
        guardar_datos_json(nombre, datos_guardar)
    else:
        print("No se encontro ese pokemon")
#se programa la interfaz con la que el usuario
def menu():
    print("Esta es tu pokedex personal")
while True:
    print("\n0piciones:")
    print("1. Busca un pokemon")
    print("2. Salir")
    opcion = input ("Selecciona una opcion: ")

    if opcion == "1":
        buscar_pokemon()
    elif opcion == "2":
        print("Nos vemos pronto:")
        break
    else:
        print("opcon no valida. Intentalo de nuevo.")

menu()