"""Aqui se explican estructuras de datos avanzadas"""

""" SETS
Son conjuntos de elementos no repetidos. Sirven para dos funciones principales
 """

 #Los sets se pueden crear a través de una lista
amigosPrados = set(["Luis", "Diego"])

#Tambien se pueden crear con llaves
amigosTecamac = {"Luis", "Eduardo", "Marco", "Maruri"}

#Se pueden utilizar para evaluar la pertenencia de un elemento en un grupo
print("Jovan" in amigosTecamac)

#Tambien se pueden ver los elementos comunes o dispares de los mismos
amigosTodos = amigosPrados.union(amigosTecamac)
print(amigosTodos)

amigosComunes = amigosTecamac.intersection(amigosPrados)
print(amigosComunes)

amigosExclusivos = amigosTecamac - amigosPrados
print(amigosExclusivos)

#Se pueden añadir o quitar elementos de un set
avengers = {"Iron Man", "Thor", "Hulk", "Viuda Negra", "Capitan America", "Ojo de Halcon"}
avengers.add("Spiderman")
print(avengers)
avengers.remove("Ojo de Halcon")
print(avengers)

#Los sets tambien son utiles para eliminar elementos duplicados de una lista
avengers_repetidos = ["Iron Man", "Thor", "Hulk", "Viuda Negra", "Capitan America", "Ojo de Halcon",
"Ojo de Halcon", "IronMan", "Thor", "Hulk", "Viuda Negra", "Hulk", "Thor"]
print(len(avengers_repetidos))

avengers_unicos =list(set(avengers_repetidos))
print(avengers_unicos)

#Tambien se pueden comparar sets
set1 = {"frutilla", "cambur"}
set2 = {"fresa", "banana"}
print(set1 == set2)

#Un set es más grande que otro si tiene los mismos elementos que con el que se esta comparando 
#y al menos uno más
set3 = {"fresa", "banana", "manzana"}
print(set3 > set2)
print(set3 > set1)

"""COUNTER
La clase counter sirve para contar cosas
"""
from collections import Counter
votos = [
    "PRI", "PRI", "PAN", "PRI", "PAN", "MORENA", "MORENA", "MORENA", "PRI", "PAN", "PRI", "MORENA"
]
voto_por_voto = Counter(votos)
print(voto_por_voto)

#Podemos ver el número de veces que un elemento en particular aparece
print(voto_por_voto["MORENA"])

#Si un elemento no existe nos devuelve 0
print(voto_por_voto["PRD"])

#Se pueden añadir elementos a un counter de manewra dinamica
print(voto_por_voto["PVEM"])
voto_por_voto.update(["PVEM"])
print(voto_por_voto["PVEM"])

#Tambien podemos aumentar el recuento utilizando un diccionario
voto_por_voto.update({"MORENA": 5, "PRI":3})
print(voto_por_voto)

#Tambien podemos especificar directamente el recuento de un elemento
voto_por_voto["MORENA"] = 25
print(voto_por_voto)

"""DefaulDict
La clase DefaultDict nos permite crear diccionarios que permiten devolver un valor por defecto
si una clase no existe. DefaultDict se inicia pasandole una funcion que indicara el valor a devolver en
caso de no existir la clave especificada. DefaultDict no existe como primitivo de Pthon, más bien
este n el modulo collections, esto significa que tenemos que importarlo para poder utilizarlo
"""

from collections import defaultdict
#esto va a fallar, vainilla no es un diccionario
#sabores_helado = defaultdict("vainilla")

sabores_helado = defaultdict(lambda : "vainilla")
print(sabores_helado)

sabores_helado["Guillermo"] = "Fresa"
print(sabores_helado["Guillermo"])
#Maria no es una clave existente por lo tanto devolvera el valor por defecto
print(sabores_helado["Maria"])

"""Un uso muy recuente de defaultdict es cuando tenemos un conjunto de elementos en donde
cada elemento tiene multiples caracteristicas y queremos hacer un diccionario para poder obtener
rapidamente su lista de caracteristicas
"""
pokemon_entrenadores_lista=[
    ["Ash", "Nidoran"],
    ["Ash", "Charmander"],
    ["Ash", "Jigglypuff"],
    ["Ash", "Rattata"],
    ["Ash", "Pikachu"],
    ["Ash", "Pidgey"],
    ["Misty", "Pikachu"],
    ["Misty", "Charmander"],
    ["Misty", "Jigglypuff"],
    ["Brock", "Nidoran"],
    ["Brock", "Charmander"],
    ["Brock", "Jigglypuff"]
]

pokemon_individual = defaultdict(list)
for entrenador, pokemon in pokemon_entrenadores_lista:
    pokemon_individual[entrenador].append(pokemon)
print(pokemon_individual)

### EJERCICIOS ###
"""Convertir la lista de pokemon_entrenadores_lista en una lista de diccionarios con las
claves "entrenador" y "pokemon"""

pokemon_entrenadores_diccionario = []

for tupla_entrenador in pokemon_entrenadores_lista:
    pokemon_entrenadores_diccionario.append({"Entrenador": tupla_entrenador[0],
    "Pokemon": tupla_entrenador[1]})

print(pokemon_entrenadores_diccionario)
#otra forma seria
pokemon_entrenadores_diccionario2 = []
for pokemon, entrenador in pokemon_entrenadores_lista:
    pokemon_entrenadores_diccionario2.append({"Entrenador": entrenador,
    "Pokemon": pokemon})

print(pokemon_entrenadores_diccionario2)

"Hacer una funcion que toma una frase y devuelva las 5 letras mas comunes"
def contar_letras(frase):
    contador = Counter([letra for letra in frase if letra not in ",.\n"])
    return contador.most_common(5)

print(contar_letras("jotos todos"))

"""Crear una funcion que dados dos listas de elementos nos devuelva su coeficiente de Jaccard
El coeficiente de Jaccard es una medida de similaridad entre dos grupos y se define como el numero de
elementos en los dos grupos dividido entre el numero de elementos entre uno u otro grupo"""

def jaccard(grupo1, grupo2):
    union = len(set(grupo1).union(set(grupo2)))
    interseccion = len(set(grupo1).intersection(set(grupo2)))
    return interseccion / union

amigos1 = ["Luis", "Diego"]
#Tambien se puede crear con llaves
amigos2 = {"Luis", "Eduardo", "Marco", "Maruri"}

amigos_jaccard = jaccard(amigos1, amigos2)
print(amigos_jaccard)
