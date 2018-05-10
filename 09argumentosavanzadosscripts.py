"""
Aqui se explica como aladir argumentos avanzados a los scripts
"""

#Los imports se añaden al principio de un scripts
import argparse
from modulo_importable import saludar_modulo, felicitar_modulo

def parsear_argumentos_avanzado():
    parser = argparse.ArgumentParser(
        description = "Descripcion del script"
    )

    parser.add_argument("metodo", help="""
                        Indica el metodo que se quiere usar.
                        Valores validos son saludar, felicitar
                        """, choices = ["saludar", "felicitar"])   
    parser.add_argument("usuario", help="""
                        Indica el usuario con quien se quiere interactuar.
                        """)

    parser.add_argument("--capitalizar", help="Capitaliza el nombre del usuario",
                        action = "store_true")
    argumentos = parser.parse_args()
    return argumentos

def main(argumentos):
    """
    Aqui ponemos la funcionalidad principal de nuestro script
    """
    nombre = argumentos.usuario
    if argumentos.capitalizar:
        nombre = nombre.capitalize()
        print(nombre)
    
    if argumentos.metodo == "saludar":
        saludar_modulo(nombre)
    elif argumentos.metodo == "felicitar":
        felicitar_modulo(nombre)

if __name__ == "__main__":
    #Este codigo se ejecutara si ejecutamos este script directamente
    argumentos = parsear_argumentos_avanzado()
    print("Argumentos pasados al script:", argumentos)
    main(argumentos)