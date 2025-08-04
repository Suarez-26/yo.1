from utils.screencontrollers import limpiar_pantalla, pausar_pantalla

def gestionar_categorias(db):
    while True:
        limpiar_pantalla()
        print("--- Gestión de Categorías ---")
        print("1. Crear Categoría")
        print("2. Ver Categorías")
        print("3. Actualizar Categoría")
        print("4. Eliminar Categoría")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_categoria(db)
        elif opcion == "2":
            leer_categorias(db)
        elif opcion == "3":
            actualizar_categoria(db)
        elif opcion == "4":
            eliminar_categoria(db)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
        pausar_pantalla()

def crear_categoria(db):
    nombre = input("Nombre de la categoría: ")
    descripcion = input("Descripción: ")
    db["categorias"].append({"nombre": nombre, "descripcion": descripcion})
    print("Categoría creada.")

def leer_categorias(db):
    print("\n--- Categorías ---")
    for cat in db["categorias"]:
        print(f"{cat['nombre']}: {cat['descripcion']}")

def actualizar_categoria(db):
    leer_categorias(db)
    nombre = input("Nombre de la categoría a actualizar: ")
    for cat in db["categorias"]:
        if cat["nombre"].lower() == nombre.lower():
            cat["descripcion"] = input("Nueva descripción: ")
            print("Categoría actualizada.")
            return
    print("Categoría no encontrada.")

def eliminar_categoria(db):
    leer_categorias(db)
    nombre = input("Nombre de la categoría a eliminar: ")
    db["categorias"] = [cat for cat in db["categorias"] if cat["nombre"].lower() != nombre.lower()]
    print("Categoría eliminada si existía.")
