from screencontrollers import limpiar_pantalla

def ingresar_item(campos):
    """Función genérica para solicitar datos al usuario."""
    item = {}
    for campo, tipo, mensaje in campos:
        while True:
            try:
                valor = tipo(input(mensaje))
                item[campo] = valor
                break
            except ValueError:
                print(f"Error: Entrada inválida. Por favor, ingrese un valor de tipo '{tipo.__name__}'.")
    return item

def inicializar_datos_manualmente():
    """Función principal para guiar la creación de todos los datos iniciales."""
    db = { "ingredientes": [], "categorias": [], "chefs": [], "hamburguesas": [] }

    limpiar_pantalla()
    print("--- ASISTENTE DE CONFIGURACIÓN INICIAL ---")
    print("No se encontraron archivos de datos. Vamos a crearlos.\n")

    # Ingresar Ingredientes
    print("--- 1. Ingresar Ingredientes ---")
    campos_ingrediente = [("nombre", str, "Nombre del ingrediente: "), ("descripcion", str, "Descripción: "), ("precio", float, "Precio (ej: 2.5): "), ("stock", int, "Stock inicial (ej: 100): ")]
    while True:
        db["ingredientes"].append(ingresar_item(campos_ingrediente))
        if input("¿Desea agregar otro ingrediente? (s/n): ").lower() != 's': break

    # Ingresar Categorías
    print("\n--- 2. Ingresar Categorías ---")
    campos_categoria = [("nombre", str, "Nombre de la categoría: "), ("descripcion", str, "Descripción: ")]
    while True:
        db["categorias"].append(ingresar_item(campos_categoria))
        if input("¿Desea agregar otra categoría? (s/n): ").lower() != 's': break

    # Ingresar Chefs
    print("\n--- 3. Ingresar Chefs ---")
    campos_chef = [("nombre", str, "Nombre del Chef: "), ("especialidad", str, "Especialidad: ")]
    while True:
        db["chefs"].append(ingresar_item(campos_chef))
        if input("¿Desea agregar otro chef? (s/n): ").lower() != 's': break
            
    print("\n¡Configuración inicial completada!")
    input("Presione Enter para continuar al menú principal...")
    return db