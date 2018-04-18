"""
@author: gspindolab
"""
#%%
"""
Python tiene algunos tipos de variables basicas que forman parte del lenguaje
y se le conocen como tipos primitivos
"""

"""Los mas comunes son los string, numeros y booleanos """

"""STRINGS"""

print("Se usan para representar texto")

string1 = "Hola"
string2 = "Mundo"

print(string1)

# Utilizamos la función type para mostrar que tipo de variable es

print(type(string1))
print(type(string2))

# Podemos hacer uso del símbolo + en los string para concatenar cadenas y así obtener cadenas de texto más grandes

holamundo = string1 + "" + string2
print(holamundo)

# Podemos tambien multiplicas string

n = "jotos"
print(n * 10)

# Tambien podemos hacer uso de format que nos permite insertar string dentro de otros

nombre = "Guillermo"
apellido = "Spindola"
nombreCompleto = "Hola, mi nombre es {}, y me apellido {}".format(nombre, apellido)
print(nombreCompleto)

# Además se puede utilizar el metodo format para redondear numeros decimales
import math

pi = "El valor de PI es: {}".format(math.pi)
print(pi)

#restringir PI a 2 decimales
pi2 = "Los primeros dos decimales de PI son: {:.2f}".format(math.pi)
print(pi2)

#redondeara un entero
piE = "El valor de PI en un número entero es: {:.0f}".format(math.pi)
print(piE)

# A partir de la version 3.6 se puede utilizar format de la siguiente manera
formato = f"Hola, mi nombre es {nombre} y mi apellido es {apellido}"
print(formato)

# OPERACIONES CON STRINGS

texto = "introduccion a PYTHON"

print("Convertimos un string a mayusculas con upper")
print(texto.upper())
print("Convertimos un string a minusculas con lower")
print(texto.lower())
print("Ponemos las primeras letras de cada palabra en mayusculas con capitaliza")
print(texto.capitalize())

""" La función strip elimina caracteres al principio y al final de una cadena """
comas = ",Josh,"
print(comas.strip(","))

""" Se utiliza replace para remplazar partes de una cadena por otras """
print(nombre.replace("mo", "mina"))

""" Se pueden utilizar varias funciones a la vez """
print(comas.strip(",").replace("sh","rge"))

""" Con el método split se puede separar un string en varios """
frutas  = "Manzana|Pera|Guayaba"
frutas.split("|")
print(frutas)

#NUMEROS

""" Hay dos tipos numericos basicos primitivos en Python y son los int(enteros) y float(decimales) """
entero = 41
print(type(entero))

decimal = math.pi
print(type(decimal))

""" Se pueden convertir numeros a decimales con el metodo str """
print(type(str(entero)))

""" Tambien se puede utilizar el metodo format con números """
edad = 23
altura = 1.97
print(f"Hola, mi nombre es {nombre}, me apellido {apellido}, tengo {edad} años y mido {altura} centimetros")

""" De igual manera se pueden convertir strings a numeros """
kobe = "24"
dirk = "41"
print(int(kobe) + int(dirk))

""" Convertimos float a int """
flotante = 23.5
print(int(flotante))


