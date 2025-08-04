import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

INGREDIENTES_FILE = os.path.join(DATA_DIR, "ingredientes.json")
CATEGORIAS_FILE = os.path.join(DATA_DIR, "categorias.json")
CHEFS_FILE = os.path.join(DATA_DIR, "chefs.json")
HAMBURGUESAS_FILE = os.path.join(DATA_DIR, "hamburguesas.json")
