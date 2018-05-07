"""Python: Es un lenguaje orientado a objetos. Esto significa que a pesar de que podemos trabajar
de manera funcional con el uso de funciones, muchas de las ventajas de Python están en el uso
de las clases"""

"""Las clases en Python 3 se definen de la siguiente manera """

"""
class Clase:
    def metodo1(self):-->TODOS LOS MÉTODOS DE CLASES TOMAN 'self' COMO PRIMER ARGUMENTO
        #método que tienen los objetos de la clase

    def metodo2(self):
        #otro método que tienen los objetos de la clase
"""

#En el siguiente ejemplo se crea una clase llamada CocheBasico
class CocheBasico:
    def girar_izquierda(self):
        print("Girando a la izquierda")
    def girar_derecha(self):
        print("Girando a la derecha")
    def acelerar(self):
        #podemos usar pass cuando definimos una funcion para que no haga nada
        pass
    def frenar(self):
        pass
print(CocheBasico)

"""Hemos creado una clase CocheBasico. Las clases se pueden considerar como plantillas que se pueden usar 
para generar objetos. Por ejemplo l plantilla(clase) CocheBasico nos da instrucciones para fabricar
un coche. En el mundo de la programación se le conoce como instanciar una clase, es decir, se crea una
instancia(objeto) de la clase CocheBasico."""
coche_guillermo = CocheBasico()
print(coche_guillermo)

"Este objeto es un objeto de la clase CocheBasico"
print(type(coche_guillermo)==CocheBasico)

"""Este objeto tiene todas las caracteristicas de la clase coche y podemos acceder a ellas de la siguiente
manera:"""

coche_guillermo.girar_izquierda()
coche_guillermo.girar_derecha()
coche_guillermo.acelerar()
coche_guillermo.frenar()

"""
Al igual que con las funciones, generalmente creemos que los objetos que creamos tengan algunas
caracteristicas definidas de manera variable. Con la clase coche teniamos que todos los coches creados
serían 100 % iguales. A continuación un ejemplo de como podríamos generar coches que tengan distinto color.
Podemos hacer uso del método especial _init_ que se ejecuta cuando se crea un objeto de una clase
"""

class CocheColor:
    def __init__(self, color):
        self.color = color #->Este es un atributo
    def describir(self):
        print("Coche de color {}". format(self.color))
    def girar_izquierda(self):
        print("Girando a la izquierda")
    def girar_derecha(self):
        print("Girando a la derecha")
    def acelerar(self):
        #podemos usar pass cuando definimos una funcion para que no haga nada
        pass
    def frenar(self):
        pass

coche_rojo = CocheColor(color = "azul")
coche_rojo.describir()
print(coche_rojo.color)

"Tambien podemos añadir atributos a instancias"
coche_rojo.matricula = "SIBG940601"
print(coche_rojo.matricula)

"Al crear un CocheColor, tenemos que especificar forzosamente un color"
"coche_bn = CocheColor()"

"Podemos evitar esto, indicando un valor por defecto en el metodo _init_"
class PorDefecto:
    def __init__ (self, color="negro"):
        self.color = color
    def describir(self):
        print("Coche de color {}". format(self.color))
    def girar_izquierda(self):
        print("Girando a la izquierda")
    def girar_derecha(self):
        print("Girando a la derecha")
    def acelerar(self):
        #podemos usar pass cuando definimos una funcion para que no haga nada
        pass
    def frenar(self):
        pass

coche_bn = PorDefecto()
coche_bn.describir()

"De igual forma podemos definir todas las variables que necesitamos para definir"
class CocheVariable:
    def __init__ (self, modelo, velocidad_maxima, color = "azul"):
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad = 0
    def describir(self):
        print(f"Modelo: {self.modelo}, Velocidad Maxima: {self.velocidad_maxima} Km/h, Color: {self.color}")
    def estado(self):
        if self.velocidad == 0:
            print("El coche esta detenido")
        else:
            print(f"El coche va a {self.velocidad} kilometros por hora")
    def girar_izquierda(self):
        print("Girando a la izquierda")
    def girar_derecha(self):
        print("Girando a la derecha")
    def acelerar(self):
        #podemos usar pass cuando definimos una funcion para que no haga nada
        pass
    def frenar(self):
        pass

variable = CocheVariable(modelo = "Renault Logan", velocidad_maxima = 180, color = "dorado")
variable.describir()
variable.estado()

#En cualquier momento podamos cambiar el valor del atributo de un objeto
variable.velocidad = 150
variable.color = "Aquamarina"
variable.describir()
variable.estado()

"""Uno de los usos principales de las clases es conservar el estado de un objeto. Si no usaramos clases
para almacenar la velocidad de un coche tendríamos que tener un diccionario con los identificadores
de los coches y su velocidad y cada ve que cambiaramos la velocidad tendríamos que cambiar el diccionario

A continuación se muestra un ejemplo para obtener un vehiculo completo"""

class Vehiculo:
    def __init__ (self, modelo, velocidad_maxima, color = "Azul"):
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad = 0
    
    def describir(self):
        descripcion = "VEHICULO Modelo: {}, Velocidad maxima: {}, Color: {}".format(self.modelo,
        self.velocidad_maxima, self.color)
        return descripcion

#El metodo _repr_ es un metodo magico que se usa cuando queremos representar algo (con el metodo print).
    def _repr_(self):
        return self.describir()

    def estado(self):
        if self.velocidad == 0:
            print("El vehiculo esta detenido")
        elif self.velocidad > 0:
            print(f"El vehiculo va a {self.velocidad} kilometros por hora")
        else:
            print(f"El vehiculo va de reversa a {self.velocidad} kilometros por hora")

    def girar_izquierda(self):
        print("Girando a la izquierda")

    def girar_derecha(self):
        print("Girando a la derecha")

    def acelerar(self, diferencia):
        print("Acelerando a {} Km/h".format(diferencia))
        #abs devuelve un numero positivo si es negativo
        self.velocidad += abs(diferencia)
        #min devuelve el valor minimo de una lista de numeros
        self.velocidad = min(self.velocidad, self.velocidad_maxima)

    def frenar(self, diferencia):
        print("Frenando a {} Km/h".format(diferencia))
        self.velocidad -= abs(diferencia)
        #max nos devuelve el malor maximo de una lista de numeros
        self.velocidad = max(self.velocidad, -5)

coche = Vehiculo(modelo = "Jetta Europa 2010", velocidad_maxima = 210, color = "Plata")
coche.estado()
coche.acelerar(20)
coche.estado()
coche.acelerar(20)
coche.estado()
coche.frenar(50)
coche.estado()
coche.acelerar(5)
coche.estado()
print(coche)

"""HERENCIA DE CLASES
Se pueden crear clases utilizando como plantillas otras clases, es decir, un clase hereda de la otra.
A esto se le conoce como herencia.
Eato nos permite crear una clase base con funcionalidades genericas y despues crear clases avanzadas
con funcionalidades más especificas.
Por ejemplo podemos crear una clase autobus que herede de vehiculo que no tiene marcha atras
y tiene una velocidad maxima de 100 Km/h.
"""

class Autobus(Vehiculo): # Esto indica que Autobus hereda de Vehiculo
    def acelerar(self, diferencia):
        print(f"Autobus acelerando a {diferencia} kilometros por hora")
        self.velocidad += abs(diferencia)
        self.velocidad = min(self.velocidad, 100)

    def frenar(self, diferencia):
        print(f"Autobus frenando a {diferencia} kilometros por hora")
        self.velocidad -= abs(diferencia)
        self.velocidad = max(self.velocidad, 0)

autobus_pasajeros = Autobus(modelo = "EUROCAR Y790", velocidad_maxima = 100, color = "Rojo")
autobus_pasajeros.estado()
autobus_pasajeros.acelerar(50)
autobus_pasajeros.estado()
autobus_pasajeros.frenar(80)
autobus_pasajeros.estado()

### EJERCICIOS ###

"""1.- Crear una clase Taxi que herede de Vehiculo y que pueda obrarnos un trayecto. Tiene que tener
el atributo "distancia recorrida" y tres metodos adicionales:
-metodo cobrar: Donde se imprime la cantidad a cobrar (3 euros por kilometro recorrido).
-metodo añadir_distancia: Donde se suma a la distancia recorrida un numero de kilometros.
-metodo añadir_tiempo: donde dado un tiempo (en horas) se añade distancia en funcion de la velocidad actual"""
class Taxi(Vehiculo):
    def __init__(self, modelo, velocidad_maxima):
        self.color = "Blanco"
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad = 0 #el coche empieza parado
        self.distancia_recorrida = 0
        self.tarifa = 3

    def cobrar(self):
        print(f"El total es {self.distancia_recorrida*self.tarifa}")

    def añadir_distancia(self, distancia):
        self.distancia_recorrida += distancia

    def añadir_tiempo(self, tiempo):
        self.añadir_distancia(tiempo*self.velocidad)

uber = Taxi(modelo = "Mercedes Benz", velocidad_maxima = 250)
uber.acelerar(150)
uber.añadir_tiempo(1)
uber.cobrar()
uber.añadir_tiempo(5)
uber.cobrar()

"""2.- Creae una clase Parking, donde puedan aparcar un limite determinado de Vehiculos(solo vehiculos)
y donde se pueda validar si esta aparcado o no"""
class Parking:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = []

    def nivel_ocupacion(self):
        return len(self.vehiculos) / self.capacidad

    def __repr__(self):
        return "Parking con capacidad {}. Nível de ocupación {:.2f}".format(self.capacidad,
        self.nivel_ocupacion())

    def aparcar_vehiculo(self, vehiculo):
        if not type(vehiculo) == Vehiculo or vehiculo in self.vehiculos:
            print("Solo se admiten vehiculos que no estan aparcados")
        elif len(self.vehiculos) < self.capacidad:
            print("Aparcando vehiculo {}".format(vehiculo))
            self.vehiculos.append(vehiculo)

    def sacar_vehiculo(self, vehiculo):
        if vehiculo in self.vehiculos:
            print("Sacando el vehiculo {}".format(vehiculo))
            self.vehiculos.pop(self.vehiculos.index(vehiculo))
        else:
            print("Vehiculo {} no esta aparcado".format(vehiculo))

parking_josh = Parking(capacidad=100)

coche1 = Vehiculo(modelo = "Renault Logan", velocidad_maxima = 180, color = "Dorado")
coche2 = Vehiculo(modelo = "Renault Sandero", velocidad_maxima = 200, color = "Negro")
taxi = Taxi(modelo = "FIAT Italia", velocidad_maxima = 150)

parking_josh.aparcar_vehiculo(coche1)
parking_josh.aparcar_vehiculo(coche2)
parking_josh.aparcar_vehiculo(taxi)

print(parking_josh)

parking_josh.sacar_vehiculo(taxi)

print(parking_josh)