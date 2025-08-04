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
        if opcion == "1": crear_ingrediente(db)
        elif opcion == "2": leer_ingredientes(db)
        elif opcion == "3": print("Función no implementada.")
        elif opcion == "4": print("Función no implementada.")
        elif opcion == "5": break
        else: print("Opción no válida.")
        pausar_pantalla()

def crear_ingrediente(db):
    print("\n--- Crear Nuevo Ingrediente ---")
    try:
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock inicial: "))
        db["ingredientes"].append({"nombre": nombre, "descripcion": descripcion, "precio": precio, "stock": stock})
        print(f"¡Ingrediente '{nombre}' creado en memoria!")
    except ValueError:
        print("Error: Precio y stock deben ser números.")

def leer_ingredientes(db):
    print("\n--- Listado de Ingredientes ---")
    if not db["ingredientes"]:
        print("No hay ingredientes registrados.")
        return
    for item in db["ingredientes"]:
        print(f"- {item['nombre']} (Precio: ${item['precio']:.2f}, Stock: {item['stock']})")