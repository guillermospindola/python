#### ESTRUCTURAS DE CONTROL ###

# IF-ELSE

# Se utiliza if-else para tomar decisiones y ejecutar distintas partes del código
# en función de una condición

# En Python la manera de indicar que estamos dentro de una condicion es el indentado
# es decir , de la siguiente manera

"La manera sencilla de trabajar con una condición es con un if simple"
edad = 15

if edad >= 18:
    # Esto es un indentado y se ejecutara el siguiente codigo de ser verdadera la condicion
    print("Puedes votar en las siguientes elecciones presidenciales")

"Si queremos utilizar distintas condiciones ocupamos if-else"
if edad <= 18:
    mensaje = "Eres menor de edad, deben cuidarte tus padres"
elif edad <= 65:
    mensaje = "Ya eres mayor de edad"
else:
    mensaje = "Inclusive ya eres un adulto mayor"

print(mensaje)

"De igual manera podemos trabajar con if anidados"
altura = 1.65
niño = False

if altura >= 1.65:
    if not niño:
        print("Puedes subirte al juego mecanico")

# BUCLES FOR (FOR LOOPS)
x = 1
for x in range(1,10):
    print("Este es el número:", format(x))

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for numero in numeros:
    if numero <= 10:
        print(f"Número válido {numero}")
    else:
        print(f"Número inválido {numero}")

"Existen ocasiones en las cuales vamos a necesitar romper el bucle si ocurre determinada condicion"
"Esto lo podemos llevar a cabo con la palabra reservada break"
for numero in numeros:
    if numero <= 10:
        print(f"Número {numero} válido")
    else:
        print(f"Error!, a partir del número {numero} es inválido, saliendo del bucle")
        break

"En ocasiones en vez de romprer el bucle, requerimos de no realizar ninguna acción para cierta iteracion"
"En estos casos se puede utilizar la palabra reservada pass"
for numero in numeros:
    if numero <= 10:
        print(f"Número {numero} válido")
    else:
        pass

"Existe una manera más simple de iterar los elementos de una lista y es la siguiente:"
[numero for numero in numeros if numero < 10]

"Es posible iterar las claves de un diccionario con un for"
frutas = {
    "durazno":10,
    "mandarina": 5,
    "pera": 3
}

for fruta in frutas:
    print(fruta)

"De igual manera se pueden iterar tanto claves como valores de un diccionario utilizando items"
for fruta, cantidad in frutas.items():
    print(f"Tenemos {cantidad} kilos de {fruta}")

"No solo las listas soportan el bucle for, de igual manera los strings"
ciudad = "CDMX"
for letra in ciudad:
    print(f"Dame una: {letra}")

print("Que dice...")
print(ciudad)

# TRY-EXCEPT 
"En ocasiones los programas fallan lanzando una excepcion" 
"Una manera de poder hacer que un programa continue su funcionamiento a pesar de haber fallado"
"Es atrapando dicha excepción. En python se realiza mediante el bloque try-except"
"""IMPORTANTE
Siempre que atrapemos una excepcion es importante imprimir el mensaje de error
Esto es una manera de asegurarnos que el programa falle sin darnos cuenta """
numero_str = "10.5"

try:
    #intentara convertir un número a string
    numero_int = int(numero_str)
except Exception as e:#si llega a ocurrir un error no se detendra el programa y ejecutara lo siguiente
    print(f"Error: el valor {numero_str} no se puede convertir a número entero")
    print("El mensaje de error es: ")
    print(type(e), e)

"""El problema de capturar todos los errores de nuestro programa es que podemos dejar pasar errores
que hagan que todo falle de manera silenciosa. Una manera más efectiva de capturar errores
es capturar unicamente aquellos que conozcamos y fallar en caso de un error que no conozcamos"""
numero_str = "10.5"

try:
    #intentara convertir un número a string
    numero_int = int(numero_str)
except ValueError:#Esto fallara para cualquier error que no se ValueError
    print(f"Error: el valor {numero_str} no se puede convertir a número entero")

# WHILE
"Los bucles while se ejecutan mientras una condición sea verdadera"
num_elefantes = 2
print("1 elefante se columpiaba sobre la tela de una araña, como veia que resitia fueron a lamar a otro elefante.")
while num_elefantes <= 10:
    print("{} elefantes se columpiaban sobre la tela de una araña, como veian que resitia fueron a lamar a otro elefante.".format(num_elefantes))
    #Usar num_elefantes += 1 es lo equivalwnte a decir num_elefantes = num_elefantes + 1
    num_elefantes += 1

"Hay que tener cuidado, ya que podemos generar un bucle infinito. Se puede deneter la ajecucion con CTRL+Z"
#while 1 > 0:
    #print("Esto es un bucle infinito")

"""Un uso comun del while es validar el input que nos da un usuario,
podemos obener el input de un usuario con la funcion input()"""
"""while 1:
    input_usuario=input("Dame un número del 1 al 10, escriba 'exit' para salir: ")
    try:
        if input_usuario == "exit":
            print("Adios")
            break
        elif int(input_usuario) <= 10:
            cuadrado = int(input_usuario) ** 2
            print("El cuadrado del número {} es: {}".format(input_usuario, cuadrado))
        else:
            print("El valor {} no es un valor valido".format(input_usuario))
    except ValueError:#Esto fallara para cualquier error que no se ValueError
        print(f"Error: el valor {numero_str} no se puede convertir a número entero")
"""
# EJERCICIOS
"Convertir todas las claves del siguiente diccionario a mayusculas"
dias_semana = {
    "Lunes": 1,
    "Martes": 2,
    "Miercoles": 3,
    "Jueves": 4,
    "Viernes": 5,
    "Sabado": 6,
    "Domingo": 7
}

#Esto no funciona, no podemos cambial el tamaño de un diccionario dentro de un loop 

"""for clave, valor in dias_semana.items():
    dias_semana[clave.upper()] = valor
    dias_semana.pop(clave)"""

dias_semana_mayusculas = {}
for clave, valor in dias_semana.items():
    dias_semana_mayusculas[clave.upper()] = valor
dias_semana = dias_semana_mayusculas
print(dias_semana)


"De e diccionario crear una lista de los dias de la semana que tengan una O"

dias_con_o = []
for clave in dias_semana:
    if "O" in clave:
        dias_con_o.append(clave)
print(dias_con_o)




