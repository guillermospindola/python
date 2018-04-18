### ESTRUCTURAS DE DATOS ###
"Las estructuras de datos son objetos que se utilizan para almacenar informacion,"
"los más basicos son los siguientes"

"LISTAS"

"Son conjuntos de elementos ordenados en donde cada elemento contiene una posicion"
frutas = ["piña", "naranja", "pera", "manzana"]
print(frutas)
print(type(frutas))
"Podemos acceder al elemento de una lista con[], el indice de una lista comienza con 0"
"Si queremos acceder al primer elemento de una lista se accede con [0]"
print(frutas[0])
"Podemos acceder al rango de elementos de una lista con [inicio:final], muestra los primeros 2"
print(frutas[:2])
"Accedemos a los elementos desde el 2 hasta el final, se muestran a partir del 3 elemento"
print(frutas[2:])
"Podemos acceder a los elementos empezando por el final accediendo a la lista con numeros negativos"
"Por ejemplo, accedemos a los ultimos dos elementos"
print(frutas[-2:])
"Se pueden saltar elementos de n en n usando [::n], por ejemplo si solo queremos los numeros impares"
print(frutas[::2])
"Si el orden es un numero negativo se devolvera la lista en un sentido inverso"
print(frutas[::-1])
"Podemos obtener el numero de elementos de una lista con el metodo len()"
print(len(frutas))
"Podemos añadir un nuevo elemento a la lista con append(). Esto modificara la lista"
frutas.append("sandia")
print(frutas)
"Podemos repetir una lista las veces que queramor, multiplicandola por un entero"
print(frutas*2)
"Al igual que los string, tambien se pueden concatenar listas con el simbolo +"
municipios = ["Tecamac", "Tultitlan"]
print(frutas + municipios)
"Podemos modificar elementos de una lista existente"
frutas[0] = "durazno"
print(frutas)
"Se puede agrandar una lista sin importar el tamaño inicial"
frutas[3:] = ["papaya","guanabana","mandarina","fresa","higo"]
print(frutas)
"Podemos evaluar si un elemento existe en una lista con in"
print("pera" in frutas)
print("arandano" in frutas)
"Podemos buscar la posicion de un elemento en una lista con inex"
print("La posición de la pera en la lista es: {}".format(frutas.index("pera")))
"Podemos eliminar un elemento de la lista con pop"
a = frutas.pop(2)
print(frutas)
print(a)
"Si combinamos index con pop podemos eliminar un elemento en concreto"
frutas.pop(frutas.index("mandarina"))
print(frutas)
"Las listas numericas se pueden ordenar con el metodo sort"
numeros = [23, 41, 24, 8, 35, 7, 10]
numeros.sort()
print(numeros)
"Se pueden generar listas de numeros con la funcion range"
print(list(range(10)))
"Los strings se pueden acceder de manera similar que las listas, se imprime T"
municipios = "Toluca"
print(municipios[0])
"Se imprime luca"
print(municipios[2:])

"TUPLAS"

"Las tuplas son versiones de las listas que no se pueden modificar"
grupof = ("Alemania", "Mexico", "Suecia", "Corea del Sur")
print(type(grupof))
print(grupof)
"Podemos acceder a los elementos de una tupla de la misma manera que a los de una lista"
print(grupof[1])
print(grupof[2:])
"Pero no podremos modificarla, marcaria un error"
"""grupof[0] = "Brasil"""

"DICCIONARIOS"

"Son un conjunto de claves (keys) asociadas a valores (values)."
"Si conocemos el valor de una clave, podemos saber su valor"
hermanos = {
    "Guillermo":23,
    "Ismael":26,
    "Christian":20
    }
print(type(hermanos))
print(hermanos)

"Podemos ver las claves que tiene un diccionario con el metodo keys()"
print(hermanos.keys())

"El metodo keys() no devuelve una lista, si deseamos acceder a una clave como lista es necesario convertirla"
#print(hermanos.keys()[0])
print(list(hermanos.keys())[0])

"Podemos ver los valores de un diccionario con el metodo values()"
print(hermanos.values())

"Accedemos a los elementos de un diccionario con []"
print(hermanos["Guillermo"])
"Si la clave que buscamos no existe nos arrojara un error: KeyError"
#print(hermanos["Ricardo"])

"Podemos evaluar si existe una clave en un diccionario de una manerca muy facil con in"
print("Guillermo" in hermanos)
print("Ricardo" in hermanos)

"Se puede eliminar una clava de un diccionario con pop"
edad_hermanos = hermanos.pop("Guillermo")
print("La edad de Guillermo es {}".format(edad_hermanos))
print(hermanos)

"Cada tipo de estructura de datos puede almacenar los otros"
estados_ciudades=[
    ["Mexico","Tecamac"],
    ["Tamaulipas","Cd Victoria"],
    ["Baja California","Tijuana"],
    ["Quintana Roo","Chetumal"]
]
print(estados_ciudades[2][0])

"Un diccionario con tuplas como valores"
municipios_colonias={
    "Tecamac": ("San Pedro Atzompa", "Ojo de Agua"),
    "Tultitlan": ("San Pablo de las Salinas", "Unidad Morelos 3a Seccion")
}
print(municipios_colonias.values())

"Una lista que contiene diccionarios"
lista_diccionarios = [
    {"origen":"Ozumbilla", "destino":"Prados"},
    {"origen":"Escandon", "destino":"Ozumbilla"}
]

# EJERCICIOS

# Crear un diccionario cuyas claves sean los dias de la semana y los valores
# sean la posicion en la semana de dicho dia
dias_semana = {
    "Lunes":1,
    "Martes":2,
    "Miercoles":3,
    "Jueves":4,
    "Viernes":5,
    "Sabado":6,
    "Domingo":7
}

# Convertir todas las claves del diccionario a mayusculas
print(list(dias_semana.keys())[0].upper())
print(list(dias_semana.keys())[1].upper())
print(list(dias_semana.keys())[2].upper())
print(list(dias_semana.keys())[3].upper())
print(list(dias_semana.keys())[4].upper())
print(list(dias_semana.keys())[5].upper())
print(list(dias_semana.keys())[6].upper())









