from aterrizar import *
from datetime import datetime

from persistencia import cargar_todos


if __name__ == "__main__":
    for asiento in cargar_todos().values(): 
        asiento.liberar()

        
    print(datetime.now(), "Estoy liberando las prendas. creeme")