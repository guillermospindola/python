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

numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    print(numero)