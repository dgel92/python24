import json


def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)


usuarios = cargar_usuarios()

