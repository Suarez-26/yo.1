from utils.screencontrollers import limpiar_pantalla, pausar_pantalla
from utils.screencontrollers import limpiar_pantalla, pausar_pantalla
from utils.screencontrollers import limpiar_pantalla, pausar_pantalla
from utils.screencontrollers import limpiar_pantalla, pausar_pantalla

def gestionar_categorias():

    while True:
        limpiar_pantalla()
        print("--- Gestión de Categorías --- \n 1. Crear \n 2. Ver \n 3. Volver")
        opcion = input("Opción: ")
        if opcion == '1':
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            ["categorias"].append({"nombre": nombre, "descripcion": descripcion})
            print("Categoría creada en memoria.")
        elif opcion == '2':
            print("\n--- Categorías ---")
            for cat in ["categorias"]: print(f"- {cat['nombre']}: {cat['descripcion']}")
        elif opcion == '3': break
        pausar_pantalla()




def gestionar_chefs(db):

    while True:
        limpiar_pantalla()
        print("--- Gestión de Chefs --- \n 1. Crear \n 2. Ver \n 3. Volver")
        opcion = input("Opción: ")
        if opcion == '1':
            nombre = input("Nombre: ")
            especialidad = input("Especialidad: ")
            ["chefs"].append({"nombre": nombre, "especialidad": especialidad})
            print("Chef creado en memoria.")
        elif opcion == '2':
            print("\n--- Chefs ---")
            for chef in ["chefs"]: print(f"- {chef['nombre']}, Especialidad: {chef['especialidad']}")
        elif opcion == '3': break
        pausar_pantalla()
        



def gestionar_hamburguesas():

        limpiar_pantalla()
        print("--- Gestión de Hamburguesas --- \n 1. Crear \n 2. Ver \n 3. Volver")
        opcion = input("Opción: ")
        if opcion == '1':
            print("Función de crear hamburguesa no implementada en este ejemplo.")
        elif opcion == '2':
            print("\n--- Hamburguesas ---")
            if not ["hamburguesas"]: print("No hay hamburguesas.")
            for ham in ["hamburguesas"]: print(f"- {ham['nombre']} (${ham['precio']})")
        elif opcion == '3': 
            pass
        else:
            pass
        pausar_pantalla()

def menu_reportes():
    while True:
        limpiar_pantalla()
        print("--- Menú de Reportes ---")
        print("1. Ingredientes con stock menor a un valor")
        print("2. Hamburguesas por categoría")
        print("3. Volver al Menú Principal")
        
        opcion = input("\nSeleccione un reporte: ")
        
        limpiar_pantalla()
        print("--- Resultado del Reporte ---\n")

        if opcion == '1':
            try:
                valor = int(input("Ingrese el valor máximo de stock (ej: 400): "))
                resultado = [ing for ing in ['ingredientes'] if ing['stock'] < valor]
                if not resultado: print("Ningún ingrediente cumple el criterio.")
                for ing in resultado: print(f"- {ing['nombre']} (Stock: {ing['stock']})")
            except ValueError:
                print("Valor inválido.")
        
        elif opcion == '2':
            categoria = input("Ingrese el nombre de la categoría a buscar: ")
            resultado = [ham for ham in ['hamburguesas'] if ham['categoria'].lower() == categoria.lower()]
            if not resultado: print("No se encontraron hamburguesas en esa categoría.")
            for ham in resultado: print(f"- {ham['nombre']}")
        
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")
            
        pausar_pantalla()