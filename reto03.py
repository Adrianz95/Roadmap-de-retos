# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
#   en tu lenguaje.

mylist = ["apple", "banana", "cherry"]
mytuple = ("apple", "banana", "cherry")
myset = {"apple", "banana", "cherry"}
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
# Se hará todo en relación a mylist

mylist.append("orange") # añade un valor a la lista con una posición nueva
mylist.remove("cherry") # elimina el valor dentro del listado, cherry
mylist[1] = "watermelon" # actualiza los datos de la posición 1
mylist.sort() # ordena la lista por orden alfabético

# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización
#   y eliminación de contactos. 
# - Cada contacto debe tener un nombre y un número de teléfono. 
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#   y a continuación los datos necesarios para llevarla a cabo. 
# - El programa no puede dejar introducir números de teléfono no númericos y con más
#   de 11 dígitos (o el número de dígitos que quieras).
# - También se debe proponer una operación de finalización del programa. 

import re

def verTodosContactos(agenda):
    if len(agenda) == 0:
        print("No hay contactos en la agenda")
    else:                                                                                                                   
        for nombre, numero in agenda.items():
            print(nombre + " - " + numero)

def verContacto(agenda):
    nombre = input("Escriba el nombre que quiera buscar: ")

    if len(agenda) == 0:
        print("No hay contactos en la agenda")
    else:                                                                                                                   
        for n, num in agenda.items():
            if n == nombre:
                print(n + " - " + num)
            else:
                print("Este contacto no existe")

def insertarContacto(agenda): 
    nombre = input("Escriba el nombre: ")
    numero = input("Escriba el número: ")
    letras = re.findall(r"\D", numero)

    if len(numero) != 9:                                                                                                    
        print("Tiene que tener 9 dígitos")
    elif len(letras) > 0:
        print("Sólo debe contener dígitos")
    else:
        agenda[nombre] = numero

def actualizarContacto(agenda): # Falta decir que el número no sea 9 dígitos y sólo números.
    nombre = input("Elija el contacto que quiera actualizar: ")
    numero = input("Escriba el número: ")
    letras = re.findall(r"\D", numero)

    if len(numero) != 9:                                                                                                    
        print("Tiene que tener 9 dígitos")
    elif len(letras) > 0:
        print("Sólo debe contener dígitos")
    else:
        for n, j in agenda.items():
            if n == nombre:
                agenda[nombre] = numero


def eliminarContacto(agenda):
    nombre = input("Elija el contacto que quiere eliminar: ")
    
    if len(agenda) == 0:
        print("No hay contactos en la agenda")
                                                                                                                            
    try:
        agenda.pop(nombre)
    except:
        print("El contacto no existe")


def menuOpciones(agenda):
    en_ejecuccion = True

    while en_ejecuccion:
        print("\n Menu de opciones")
        print("1 - Ver todos los contactos")
        print("2 - Búsqueda de un contacto")
        print("3 - Insertar un contacto")
        print("4 - Actualizar un contacto")
        print("5 - Eliminar un contacto")
        print("6 - Salir del menu de opciones")
        opcion = input("Elige una opción (1 - 6): ")

        if opcion == '1':
            verTodosContactos(agenda)
        elif opcion == '2':
            verContacto(agenda)                                                                                             # Función ok
        elif opcion == '3':
            insertarContacto(agenda)
        elif opcion == '4':
            actualizarContacto(agenda)
        elif opcion == '5':
            eliminarContacto(agenda)
        elif opcion == '6':
            en_ejecuccion = False
            print("Salió del menu de opciones")
        else:
            print("Elija una opción correcta del 1 - 6")


agenda = {}

menuOpciones(agenda)