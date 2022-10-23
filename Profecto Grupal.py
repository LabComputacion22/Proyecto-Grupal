import random

operadores = ["<", ">", "!=", "=="]
valor = random.randrange(0, 100)
print(f"{valor}")
valor2 = random.randrange(0, 100)
valorOperador = random.randrange(0, 4)
print(f"{valor2}")
operador = operadores[valorOperador]
print(f"{operador}")
comienzo = 0

print("Bienvenidos a Jugar Aprendiendo\nEl juego consiste en resolver las operaciones logicas")
comienzo = int(input("Ingrese \"1\" para comenzar: "))

if comienzo == 1:
    print("El juego a comenzado".upper(), "\nSu ecuacion es la siguiente: ")
    # print(f"{valor} {operador} {valor2} = ")
