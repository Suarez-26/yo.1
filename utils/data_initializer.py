from utils.valideData import guardar_datos
from config import INGREDIENTES_FILE, CATEGORIAS_FILE, CHEFS_FILE, HAMBURGUESAS_FILE

def inicializar_datos_manualmente():
    print("\nInicializando datos...")

    ingredientes = []
    categorias = []
    chefs = []

    print("\nIngrese ingredientes iniciales:")
    while True:
        nombre = input("Nombre del ingrediente (Enter para salir): ")
        if not nombre:
            break
        stock = int(input("Stock: "))
        ingredientes.append({"nombre": nombre, "stock": stock})

    print("\nIngrese categorías:")
    while True:
        nombre = input("Nombre de la categoría (Enter para salir): ")
        if not nombre:
            break
        categorias.append({"nombre": nombre})

    print("\nIngrese chefs:")
    while True:
        nombre = input("Nombre del chef (Enter para salir): ")
        if not nombre:
            break
        especialidad = input("Especialidad: ")
        chefs.append({"nombre": nombre, "especialidad": especialidad})

    hamburguesas = []

    guardar_datos(INGREDIENTES_FILE, ingredientes)
    guardar_datos(CATEGORIAS_FILE, categorias)
    guardar_datos(CHEFS_FILE, chefs)
    guardar_datos(HAMBURGUESAS_FILE, hamburguesas)

    return {
        "ingredientes": ingredientes,
        "categorias": categorias,
        "chefs": chefs,
        "hamburguesas": hamburguesas
    }
