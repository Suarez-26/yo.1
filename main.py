import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

from utils.screencontrollers import limpiar_pantalla, pausar_pantalla
from utils.valideData import cargar_datos, guardar_estado_completo
from utils.data_initializer import inicializar_datos_manualmente
from config import INGREDIENTES_FILE, CATEGORIAS_FILE, CHEFS_FILE, HAMBURGUESAS_FILE
from controllers.ingredientes import gestionar_ingredientes
from controllers.categorias import gestionar_categorias
from controllers.categorias import gestionar_chefs
from controllers.categorias import gestionar_hamburguesas
from controllers.reportes import menu_reportes

def cargar_o_crear_datos():
    """
    Intenta cargar los datos desde los archivos JSON.
    Si algún archivo esencial no existe, inicia el asistente de creación manual.
    """
  
    data_dir = os.path.dirname(INGREDIENTES_FILE)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

   
    ingredientes = cargar_datos(INGREDIENTES_FILE)
    categorias = cargar_datos(CATEGORIAS_FILE)
    chefs = cargar_datos(CHEFS_FILE)
    hamburguesas = cargar_datos(HAMBURGUESAS_FILE)

  
    if ingredientes is None or categorias is None or chefs is None:
        return inicializar_datos_manualmente()
    else:
 
        return {
            "ingredientes": ingredientes,
            "categorias": categorias,
            "chefs": chefs,
            "hamburguesas": hamburguesas if hamburguesas is not None else []
        }

def main():

    db = cargar_o_crear_datos()

    while True:
        limpiar_pantalla()
        print("--- Sistema de Gestión de la Cafetería Campuslands ---")
        print("(Los datos se guardan al seleccionar 'Salir y Guardar')")
        print("\n1. Gestionar Ingredientes")
        print("2. Gestionar Categorías")
        print("3. Gestionar Chefs")
        print("4. Gestionar Hamburguesas")
        print("5. Ver Reportes")
        print("6. Salir y Guardar")
        
        opcion = input("\nSeleccione un módulo: ")
        
        if opcion == "1": gestionar_ingredientes()
        elif opcion == "2": gestionar_categorias()
        elif opcion == "3": gestionar_chefs()
        elif opcion == "4": gestionar_hamburguesas()
        elif opcion == "5": menu_reportes()
        elif opcion == "6":
            guardar_estado_completo()
            print("¡Hasta luego!")
            sys.exit()
        else:
            print("Opción no válida. Intente de nuevo.")
            pausar_pantalla()

if __name__ == "__main__":
    main()