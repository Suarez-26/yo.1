from utils.screencontrollers import limpiar_pantalla, pausar_pantalla

def menu_reportes(db):
    while True:
        limpiar_pantalla()
        print("--- Reportes ---")
        print("1. Ingredientes con poco stock (<10)")
        print("2. Chefs registrados")
        print("3. Hamburguesas por categoría")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            reporte_stock_bajo(db)
        elif opcion == "2":
            reporte_chefs(db)
        elif opcion == "3":
            reporte_por_categoria(db)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
        pausar_pantalla()

def reporte_stock_bajo(db):
    print("\n--- Ingredientes con Bajo Stock ---")
    for ing in db["ingredientes"]:
        if ing["stock"] < 10:
            print(f"{ing['nombre']} | Stock: {ing['stock']}")

def reporte_chefs(db):
    print("\n--- Lista de Chefs ---")
    for chef in db["chefs"]:
        print(f"{chef['nombre']} | Especialidad: {chef['especialidad']}")

def reporte_por_categoria(db):
    print("\n--- Hamburguesas por Categoría ---")
    categorias = {}
    for hb in db["hamburguesas"]:
        categorias.setdefault(hb["categoria"], []).append(hb["nombre"])
    for cat, hbs in categorias.items():
        print(f"\n{cat}:")
        for h in hbs:
            print(f" - {h}")
