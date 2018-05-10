# -*- coding: utf-8 -*-
"""
Aqui se explica como leer y escribir archvos
"""

"""CREACIÓN DE CARPETAS"""
 #Podemos crear directorios con os.makedirs()
import os
os.makedirs("./data/nombres/", exist_ok=True)

"""LISTADO DE ARCHIVOS"""
archivos_carpeta_actual = os.listdir(".")
print(archivos_carpeta_actual)

"""ESCRITURA DE ARCHIVOS"""
#Podemos usar open para abrir archivos. Si el archivo no existe dara un error
archivo_insexistente = open("./data/nombres/usuarios.txt")

#Si queremos crear un archivo para escribir, debemos de especificar el metodo de escritura "w"
archivo_para_escribir = open("./data/nombres/usuarios.txt", "w")
archivo_para_escribir.write("Hola")
archivo_para_escribir.write("Mundo")

#No se escribira nada hasta que cerremos el archivo
archivo_para_escribir.close()

#Podemos utilizar el metodo a para escribir añadiendo sin borrar el archivo original
archivo_para_escribir = open("./data/nombres/usuarios.txt", "w")
archivo_para_escribir.write("Hola")
archivo_para_escribir.write("Mundo")
archivo_para_escribir.close()

"""
Usar el metodo close no es ideal ya que si llega a ocurrir un error entre los metodos open y close
podemos llegar a perder los archivos. La mejor manera de leer y escribir archivos es mediante el
contexto with
"""
usuarios = ["Guillermo", "Ricardo", "Spindola", "Brisuela"]
with open("usuarios.txt", "w") as fname:
    for usuario in usuarios:
        fname.write(usuario)

#Si queremos escribir cada elemento de la lista en una línea escribimos \b entre lineas
amigos = ["Luis", "Marco", "Maruri", "Eduardo", "Luis", "Diego"]
with open("./data/nombres/usuarios.txt", "w") as fname:
    for amigo in amigos:
        fname.write(amigo)
        fname.write("\n")

"""LECTURA DE ARCHIVOS"""
with open("./data/nombres/usuarios.txt") as fname:
    datos = fname.read()
print(datos)
print(type(datos))

#Si queremos separar los usuarios, debemos separar el texto en líneas
#para esto es mejor usar el metodo readlines() que no lee todo el archivo a la vez
#sino de forma iterativa, así no consume tanta memoria
usuarios_desde_archivo = []

with open("./data/nombres/usuarios.txt") as fname:
    lineas = fname.readlines()
    for linea in lineas:
        usuarios_desde_archivo.append(linea.strip("\n"))
print(usuarios_desde_archivo)
print(type(usuarios_desde_archivo))

"""USANDO PATHLIB
En Windows las carpetas se definen como \ mientras que en mac o linux se usa /
Esto puede dar errores. Una manera de garantizar que podemos acceder a archivos independientemente
del sistema operativo es con el modulo pathlib (disponible solamente en python3)

from pathlib import Path

carpeta = Path ("./data/nombres/")
archivo = carpeta / "usuarios.txt"
print(type(archivo)) #PosixPath o WindowsPath
#no tenemos que usar with
archivo.read_text()

"Con pathlib podemos escribir facilmente un archivo"
carpeta = Path ("./data/nombres/")
archivo = carpeta / "usuarios_2.txt"
archivo.write_text("Jotos todos")

print(archivo.read_text())

#Para añadir al final de un archivo seguimos necesitando
compañeros = ["Roger", "Mario", "Jose", "Richard", "Gerardo"]
carpeta = Path ("./data/nombres/")
archivo = carpeta / "usuarios_2.txt"

with open(archivo, "a") as fcompas:
    for compas in compañeros:
        fcompas.write(compas)
        fcompas.write("\n")

archivo.read_text()
"""

###EJERCICIOS"""

"""Crear una funcion que dado el nombre de un archivo lo lea y devuelva la linea con la mayor longitud"""
def linea_mas_larga(nombre):
    with open(nombre) as fname:
        lineas = [linea.strip("\n") for linea in fname.readlines()]
    linea_mas_larga = lineas[0]
    for linea in lineas:
        if len(linea) > len(linea_mas_larga):
            linea_mas_larga = linea
    return linea_mas_larga

linea_mas_larga("./data/nombres/usuarios.txt")

"""Hacer una funcion que tenga como argumentos un nombre de un archivo y un numero n y devuelva las n
ultimas lineas """
def leer_n_ultimas(nombre, n):
    with open(nombre, "r") as fname:
        lineas = [linea.strip("\n") for linea in fname.readlines()]
    return lineas[-n:]

leer_n_ultimas("./data/nombres/usuarios.txt", 3)

"""Hacer una funcion que dado un diccionario cree un archivo csv con los datos del diccionario"""
datos = {
    "nombre": ["Luis", "Maruri", "Marco", "Eduardo"],
    "edad": [23, 25, 26, 23],
    "ciudad": ["Laboratorios", "Nopalera", "5 de Nayo", "Chiconautla"]
}

def dic_a_csv(datos, nombre):
    claves = list(datos.keys())
    n_items = len(datos[claves[0]])
    with open(nombre, "w") as fname:
        fname.write(",".join(claves))
        fname.write("\n")
        for i in range(n_items):
            fila = ",".join([str(datos[clave][i]) for clave in claves])
            fname.write(fila)
            fname.write("\n")

dic_a_csv(datos, "data/nombres/nombres.csv")