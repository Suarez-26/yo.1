from utils.screencontrollers import limpiar_pantalla, pausar_pantalla

def gestionar_ingredientes(db):
    while True:
        limpiar_pantalla()
        print("--- Gestión de Ingredientes ---")
        print("1. Crear Ingrediente")
        print("2. Ver Ingredientes")
        print("3. Actualizar Ingrediente")
        print("4. Eliminar Ingrediente")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_ingrediente(db)
        elif opcion == "2":
            leer_ingredientes(db)
        elif opcion == "3":
            actualizar_ingrediente(db)
        elif opcion == "4":
            eliminar_ingrediente(db)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
        pausar_pantalla()

def crear_ingrediente(db):
    print("\n--- Crear Nuevo Ingrediente ---")
    try:
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        db["ingredientes"].append({
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock
        })
        print(f"Ingrediente '{nombre}' creado.")
    except ValueError:
        print("Error: Precio y stock deben ser números.")

def leer_ingredientes(db):
    print("\n--- Lista de Ingredientes ---")
    if not db["ingredientes"]:
        print("No hay ingredientes.")
        return
    for i, ing in enumerate(db["ingredientes"], 1):
        print(f"{i}. {ing['nombre']} | Stock: {ing['stock']} | Precio: ${ing['precio']}")

def actualizar_ingrediente(db):
    leer_ingredientes(db)
    nombre = input("\nIngrese el nombre del ingrediente a actualizar: ")
    for ing in db["ingredientes"]:
        if ing["nombre"].lower() == nombre.lower():
            ing["descripcion"] = input("Nueva descripción: ")
            ing["precio"] = float(input("Nuevo precio: "))
            ing["stock"] = int(input("Nuevo stock: "))
            print("Ingrediente actualizado.")
            return
    print("Ingrediente no encontrado.")

def eliminar_ingrediente(db):
    leer_ingredientes(db)
    nombre = input("\nIngrese el nombre del ingrediente a eliminar: ")
    for i, ing in enumerate(db["ingredientes"]):
        if ing["nombre"].lower() == nombre.lower():
            del db["ingredientes"][i]
            print("Ingrediente eliminado.")
            return
    print("Ingrediente no encontrado.")
