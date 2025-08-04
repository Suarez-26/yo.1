from utils.screencontrollers import limpiar_pantalla, pausar_pantalla

def gestionar_hamburguesas(db):
    while True:
        limpiar_pantalla()
        print("--- Gestión de Hamburguesas ---")
        print("1. Crear Hamburguesa")
        print("2. Ver Hamburguesas")
        print("3. Eliminar Hamburguesa")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_hamburguesa(db)
        elif opcion == "2":
            leer_hamburguesas(db)
        elif opcion == "3":
            eliminar_hamburguesa(db)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
        pausar_pantalla()

def crear_hamburguesa(db):
    nombre = input("Nombre de la hamburguesa: ")
    chef = input("Chef responsable: ")
    categoria = input("Categoría: ")
    ingredientes = input("Ingredientes (separados por coma): ").split(",")
    precio = float(input("Precio: "))
    db["hamburguesas"].append({
        "nombre": nombre,
        "chef": chef,
        "categoria": categoria,
        "ingredientes": [i.strip() for i in ingredientes],
        "precio": precio
    })
    print("Hamburguesa creada.")

def leer_hamburguesas(db):
    print("\n--- Hamburguesas ---")
    for hb in db["hamburguesas"]:
        print(f"{hb['nombre']} | {hb['categoria']} | {hb['chef']} | ${hb['precio']}")

def eliminar_hamburguesa(db):
    leer_hamburguesas(db)
    nombre = input("Nombre de la hamburguesa a eliminar: ")
    db["hamburguesas"] = [hb for hb in db["hamburguesas"] if hb["nombre"].lower() != nombre.lower()]
    print("Hamburguesa eliminada si existía.")
