import json
from config import INGREDIENTES_FILE, CATEGORIAS_FILE, CHEFS_FILE, HAMBURGUESAS_FILE

def cargar_datos(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def guardar_datos(archivo, datos):
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def guardar_estado_completo(db):
    print("\nGuardando todos los datos...")
    try:
        guardar_datos(INGREDIENTES_FILE, db["ingredientes"])
        guardar_datos(CATEGORIAS_FILE, db["categorias"])
        guardar_datos(CHEFS_FILE, db["chefs"])
        guardar_datos(HAMBURGUESAS_FILE, db["hamburguesas"])
        print("¡Datos guardados exitosamente!")
    except Exception as e:
        print(f"Ocurrió un error al guardar los datos: {e}")
