from utils.screencontrollers import limpiar_pantalla, pausar_pantalla

def gestionar_chefs(db):
    while True:
        limpiar_pantalla()
        print("--- Gestión de Chefs ---")
        print("1. Crear Chef")
        print("2. Ver Chefs")
        print("3. Actualizar Chef")
        print("4. Eliminar Chef")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_chef(db)
        elif opcion == "2":
            leer_chefs(db)
        elif opcion == "3":
            actualizar_chef(db)
        elif opcion == "4":
            eliminar_chef(db)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")
        pausar_pantalla()

def crear_chef(db):
    nombre = input("Nombre del chef: ")
    especialidad = input("Especialidad: ")
    db["chefs"].append({"nombre": nombre, "especialidad": especialidad})
    print("Chef creado.")

def leer_chefs(db):
    print("\n--- Chefs ---")
    for chef in db["chefs"]:
        print(f"{chef['nombre']} | Especialidad: {chef['especialidad']}")

def actualizar_chef(db):
    leer_chefs(db)
    nombre = input("Nombre del chef a actualizar: ")
    for chef in db["chefs"]:
        if chef["nombre"].lower() == nombre.lower():
            chef["especialidad"] = input("Nueva especialidad: ")
            print("Chef actualizado.")
            return
    print("Chef no encontrado.")

def eliminar_chef(db):
    leer_chefs(db)
    nombre = input("Nombre del chef a eliminar: ")
    db["chefs"] = [chef for chef in db["chefs"] if chef["nombre"].lower() != nombre.lower()]
    print("Chef eliminado si existía.")
