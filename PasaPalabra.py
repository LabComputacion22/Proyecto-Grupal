import string
from typing import List
import random

letra = str
# print(string.ascii_uppercase)
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "y", "z"]
# print(f"{abecedario}")
# A CONTINUACION SE DEPOSITAN LAS PREGUNTAS
pregunta_a = "Secuencia de pasos ordenados que describen un proceso"
pregunta_b = "Tipo de dato logico"
pregunta_c = "Número, caracter o cadena de caracteres que se utiliza como un valor y no cambiara al menos en un algoritmo "
# A CONTINUACION SE DEPOSITAN LAS RESPUESTAS
respuesta_a = "algoritmo".lower()
respuesta_b = "booleano".lower()
respuesta_c = "constante".lower()
entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
resp_correctas = 0
resp_incorrectas = 0
while entrada == "0":
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "y", "z"]
    posicion_letra = random.randrange(0, 1)  # Número aleatorio para sacar una letra de la lista abecedario
    letra = abecedario[posicion_letra]
    if letra == "a":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:\n{pregunta_a}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_a:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "b":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_b}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_b:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "c":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "c":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "d":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "d":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "e":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "e":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "f":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "f":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "g":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "g":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "h":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "h":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "i":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "i":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "j":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "j":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "k":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "k":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
    if letra == "l":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "l":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            if sigue_jugando == "5":
                print("Excelente ! Sigamos jugando")
                entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            else:
                if sigue_jugando == "9":
                    print(
                        f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
                    entrada = "1"
