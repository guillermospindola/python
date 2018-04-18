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

### Operaciones numericas ###

"""Se pueden utilizar los simbolos basicos de aritmetica para realizar operaciones"""

#suma
print("La suma de 2+2 es igual a:", 2+2)
#resta
print("La resta de 3-9 es igual a:", 3-9)
#multiplicacion
print("El resultado de multiplicar 5*4 es:", 5*4)
#division
print("La division de 4/3 da como resultado:", 4/3)


"""Además de las operaciones básicas se pueden realizar algunas otras operaciones adicionales"""

a=7
b=2

#multiplo inferior: realiza la division eliminando el resto
print(f"{a}//{b}=", a//b)
#modulo: realizar una division y quedarse solo con el resto
print(f"{a}%{b}=", a%b)
#negacion: cambiar de sentido un valor
print(f"La negacion de {a} es:", -a)
#potencias: elevar un numero al cuadrado, cubo, etcetera
print(f"El numero {a} elevado a la potencia de {b} da como resultado:", a**b)

### BOOLEANAS ###

"""Las variables boleanas son aquellas que pueden tener un valor verdadero o falso"""

verdadero = True
falso = False

print(type(verdadero))
print(type(falso))

"Como tipo primitivo especial existe None, que es una variable nula"

nulo = None
print(type(nulo))

"Cualquier tipo de variable se puede convertir a boleano, transformandola en true"

fruta = "platando"
print(type(bool(fruta)))

"0 se transforma en false"
print(bool(0))

"De igual manera None se convierte en false"
print(bool(nulo))

### Comparaciones Logicas ###
#Se pueden realizar comparaciones entre variables, el resultado de estas siempre es una variable boleana

"<: Este comparador significa menor que"
print(f"El valor {a} es menor que {b}:", a < b)
"<=: Este comparador nos indica si es menor o igual"
print(f"El valor de {b} es menor o igual que {a}:", b <= a)
">: Este comparador significa mayor que"
print(f"El valor {a} es mayor que {b}:", a > b)
">=: Este comparador nos indica mayor o igual"
print(f"El valor {b} es mayor o igual que {a}:", b >= a)
"==: Este comparador significa igual a"
print(f"El número {a} es igual a {b}:", a == b)
"!=: Este comparador nos indica que es diferente de"
print(f"El valor de {b} es diferente a {a}:", b != a)
"not: Con not podemos obtener el opuesto de un resultado logico"
print(f"not {a} != 23", not a != 23)
"and: Con and se pueden evaluar que varias condiciones se cumplan"
print(f"{a} != 23 and {a} > {b}=", a != 23 and a > b)
"or: Se utiliza para evaluar si se cumple una condición u otra"
print(f"{b} >= {a} or {b} == 2 =", b >= a or b == 2)
"is: Se utiliza para comparar si algo es verdadero o falso, en vez de utilizar =="
print("Verdadero es True", verdadero is True)
print("Falso es True", falso is True)



