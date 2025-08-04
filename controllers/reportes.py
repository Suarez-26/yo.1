from config import INGREDIENTES_FILE, HAMBURGUESAS_FILE, CHEFS_FILE, CATEGORIAS_FILE
from utils.valideData import cargar_datos, guardar_datos
from utils.screencontrollers import limpiar_pantalla, pausar_pantalla

def menu_reportes():
    while True:
        limpiar_pantalla()
        print("--- Menú de Reportes ---")
        # Imprime las 20 opciones de reportes aquí...
        print("1. Ingredientes con stock menor a 400.")
        print("...")
        print("21. Volver al Menú Principal")

        opcion = input("\nSeleccione un reporte o acción: ")
        
        # Carga los datos necesarios para los reportes
        ingredientes = cargar_datos(INGREDIENTES_FILE)
        hamburguesas = cargar_datos(HAMBURGUESAS_FILE)
        chefs = cargar_datos(CHEFS_FILE)
        categorias = cargar_datos(CATEGORIAS_FILE)

        limpiar_pantalla()
        print("--- Resultado ---")

        # Aquí va la lógica completa de los 20 reportes (el bloque if/elif/else de la respuesta anterior)
        if opcion == '1':
            resultado = [ing for ing in ingredientes if ing['stock'] < 400]
            for ing in resultado: print(f"{ing['nombre']} - Stock: {ing['stock']}")
        
        elif opcion == '2':
            # Lógica del reporte 2
            pass
        
        # ... y así sucesivamente para los 20 reportes ...

        elif opcion == '21':
            break
        else:
            print("Opción no válida.")

        pausar_pantalla()