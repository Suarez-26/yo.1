import json
from config import INGREDIENTES_FILE, CATEGORIAS_FILE, CHEFS_FILE, HAMBURGUESAS_FILE

def cargar_datos(archivo):
    """Carga datos desde un archivo JSON. Devuelve None si el archivo no existe o está corrupto."""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def guardar_datos(archivo, datos):
    """Guarda una lista de diccionarios en un archivo JSON."""
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def guardar_estado_completo():
    """Guarda todas las listas del estado en memoria en sus respectivos archivos."""
    print("\nGuardando todos los datos...")
    try:
        guardar_datos(INGREDIENTES_FILE, ["ingredientes"])
        guardar_datos(CATEGORIAS_FILE, ["categorias"])
        guardar_datos(CHEFS_FILE, ["chefs"])
        guardar_datos(HAMBURGUESAS_FILE, ["hamburguesas"])
        print("¡Datos guardados exitosamente!")
    except Exception as e:
        print(f"Ocurrió un error al guardar los datos: {e}")