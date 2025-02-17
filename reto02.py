# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes
#   posibilidades del lenguaje:
#   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

def Saludo():
    saludo = "Hola Python!"

def SaludarPersona(nombre):
    return "Hola, " + nombre + "."

# print(Saludo()) -> Salida None
# print(SaludarPersona("Adrián")) -> Salida Hola, Adrián.

# ---------------------------------------------------------------------------------------------------- #

# - Comprueba si puedes crear funciones dentro de funciones.

def Nombre(nombre):
    def Apellido(apellido):
        return apellido
    return nombre + " " + Apellido("Sánchez")

# print(Nombre("Adrián")) -> Salida Adrián Sánchez

# ---------------------------------------------------------------------------------------------------- #

# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.

telefono = "654798879"
# print(len(telefono)) -> Dos funciones integradas. print() muestra por consola lo que se añada dentro del parentesis y len() muestra la longitud de dicha variable, lista, etc..

# ---------------------------------------------------------------------------------------------------- #

# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
#   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

variableGlobal = "Global"

def funcionVariableLocal():
    variableGlobal = "Convertido en local"
    return variableGlobal

# print(variableGlobal) -> Salida "Global"
# print(funcionVariableLocal()) -> Salida "Convertido en local". En la función, se llama a la variable global y se cambia el valor pero, solamente en la función.

# ---------------------------------------------------------------------------------------------------- #

# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def mostrarNumeros(texto1, texto2) -> int:
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            contador += 1
    return contador

print(mostrarNumeros("fizz", "buzz"))

#
# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.