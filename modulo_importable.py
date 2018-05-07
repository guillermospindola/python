"""
Aqui se puede poner codigo que se importa desde otros scripts (o la terminal de python)
Cuando un script se hace muy largo, es conveniente el agrupar distintos trozos de la logica
en distintos archivos (modulos)
"""

def saludar_modulo(nombre):
    print("Hola, {} esta función se a importado del modulo {}, {}". format(nombre, __file__, __name__))

def felicitar_modulo(nombre):
    print(f"Felicidades: {nombre}")

def main():
    saludar_modulo("Tu")

if __name__ == "__main__":
    main()