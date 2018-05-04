"""
Aqui se explica como crear funciones en Python
"""

"""Los scripts en Python se ejecutan línea a línea
Las funciones son formas de separar la lógica en partes sin tener que ejecutarlas línea a línea
y además permiten reutilizar varias partes del código que se repiten
"""

"""Las funciones se definen de la siguiente forma

def nombre_de_la_funcion(arg1, arg2, arg3, ...):
    logica de la funcion
"""

def saludar():
    print("Hola Mundo")

#Al crear la función, no tenemos que ejecutar el print cada vez que la queramos llamar
saludar()
print(type(saludar))

def saludar_nombre(nombre):
    print(f"Hola {nombre}, ¿Como estas?")

saludar_nombre("Guillermo")

"Si mandamos llamar esta función sin argumento, nos mandara un error"

"Las funciones tambien pueden tener valores por defecto en los argumentos"
def saludar_olvido(nombre="amigo"):
    saludar_nombre(nombre)
saludar_olvido("Ricardo")
saludar_olvido()

"Las funciones pueden devolver un valor"
def sumar(x, y):
    return x + y
    print("Esto no se va a imprimir porque la funcion acaba con el return")
resultado = sumar(10,5)
print(resultado)

"Ahora podemos usar el resultado de la función como input"
resultado_final = sumar(resultado, 35)
print(resultado_final)

"Una funcion que no tiene un return devuelve None"
def suma_erronea(a, b):
    resultado = a + b
print(suma_erronea(5,5))

"Solo debe de haber un return en la funcion"
def suma_y_resta(k , l):
    suma = k + l
    resta = k - l
    return suma, resta

resultado_suma_resta = suma_y_resta(25, 40)
print(resultado_suma_resta)

"Podemos desempaquetar el resultado directamente"
resultado_suma, resultado_resta = suma_y_resta (45, 15)
print(resultado_suma)
print(resultado_resta)

"""Existe otra forma de crear funciones, llamadas lambda o funciones anonimas
Se definen de la siguiente forma:

func_lambda = lambda imput:output

Se suelen utilizar cuando aplicamos una lógica de programación sencilla
Y por lo tanto definir una función oficial no es tan necesario """

suma_lambda = lambda c, d : c + d
print(suma_lambda(8,6))

### EJERCICIOS ###

"Crear una función que reste dos numeros y devuelva el resultado"
resta_lambda = lambda a, b : a - b
print(f"El resultado de la resta lambda es: {resta_lambda(33,25)}")

def resta (a, b):
    resta = a - b
    return resta
print(f"El resultado de la resta def es: {resta(10,5)}")

"Crear una función lambda que convierta string a minusculas"
string_lambda = lambda string : string
print(string_lambda("JOTOS").lower())

#string_lambda = lambda string : string.lower()
#print(string_lambda("JOTOS"))

"""Crear una función que acepte 3 argumentos, 2 números y 1 string. Si el string es "suma"
devolver la suma de los dos números. Si el string es "resta" devolver la resta de los números
"""
def sumaoresta(n1, n2 , string):
    if string == "suma":
        resultado = n1 + n2
    elif string == "resta":
        resultado = n1 - n2
    elif string == "multiplicacion":
        resultado = n1 * n2
    elif string == "division":
        resultado = n1 / n2
    else:
        resultado = "Ingresa una de las 4 operaciones basicas (suma, resta, multiplicacion o division)"
    return resultado

print(sumaoresta(10, 5 , "division"))

"""Crear una funcion que pregunte al usuario una frase y devuelva dicha frase con palabras en orden
inverso """

def invertirpalabras(frase):
    frase_invertida = ""
    palabras = frase.split(" ")
    for palabra in palabras[::-1]:
        frase_invertida += palabra
        frase_invertida += " "
    return frase_invertida
print(invertirpalabras("Anita lava la tina"))

def invertirpalabrasmejorado(frase):
    palabras = frase.split(" ")
    return " ".join(palabras[::-1])
print(invertirpalabrasmejorado("Anita lava la tina"))

"Crear una funcion que detecte si una palabra es palindormo"
def palindromo(frase):
    frase_invertida = frase[::-1]
    for i in range(len(frase_invertida)):
        if frase[i] != frase_invertida[i]:
            return False
        return True

print(palindromo("anitalavalatina"))
print(palindromo("jotostodos"))

"Crear una funcion que dada una lista de listas nos devuelva una lista simple"
def simplificarlista(listanesteada):
    listasimple = []
    for listainterna in listanesteada:
        for elemento in listainterna:
            listasimple.append(elemento)
    return listasimple

listanesteada = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

print(simplificarlista(listanesteada))