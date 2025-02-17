# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#   Aritméticos: + - * / % ** //

suma = 5 + 2
resta = 4 - 2
producto = 7 * 2

#   lógicos: and or not

n1 = 10
n2 = 5

# print(n1 < n2) # False
# print(n1 > n2) # True

#   de comparación: == != > < >= <=

edad_adulta = 18
edad = 16

# print(edad < edad_adulta)

#   asignación: = += -= *= /= %= //= **= &= |= ^= >>= <<= :=

x = 5
x += 3
# print(x)

#   identidad: is is not
#   pertenencia: in not in
#   bits: & | ^ ~ << >>

numero = 6
# print(numero << 2) = 24 numero 6 en binario es 110 y se le añade dos ceros a la derecha siendo 11000 que sería el número 24


# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
# - Debes hacer print por consola del resultado de todos los ejemplos.
#   Condicionales -> if else elif

puntos = 100

print("nuevo record") if puntos > 90 else print("no hay nuevo record")

#   iterativas -> while loops or for loops

i = 1

while i < 5:
    print(i)
    i += 1

equipos = ["Real Madrid", "Barcelona", "Mallorca"]

for i in equipos:
    print(i)

#   excepciones: try except

saludo = "Hola"

try:
    print(saludo)
except NameError:
    print("No existe la variable saludo")
except:
    print("ocurrio un problema")

# Podemos crear nuestras excepciones para que salgan por consola

negativo = -1

# if negativo < 0:
    #raise Exception("La variable negativo no puede contener un número menor a 0")

# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

for i in range(10, 56): # hay que añadir 56 ya que, si ponemos 55 no lo incluiría
    if i % 3 != 0 and i != 16:
        print(i)