"""
Aqui se explica como añadir funcionalidad a los scripts
"""
#los imports se añaden al principio de un script
import sys
#Un modulo no es más que un archivo con extension .py
from modulo_importable import saludar_modulo

def parsear_argumentos_basicos():
    argumentos = sys.argv[1:]
    return argumentos

def main(argumentos):
    """
    Aqui ponemos la funcionalidad principal de nuestro script
    """
    if argumentos[0] == "saludar":
        nombre = argumentos[1]
        saludar_modulo[nombre]

if __name__ == "__main__":
    #Este codigo solo se ejecutara si ejecutamos este script directamente
    argumentos = parsear_argumentos_basicos()
    print("Argumentos pasados al script: ", argumentos)
    main(argumentos)