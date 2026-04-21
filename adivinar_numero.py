import random

numero_secreto = random.randint(1, 100)

print("Adivina el numero secreto entre 1 y 100, tienes 7 intentos")

intentos = 0
intentos_maximo = 7

while intentos < intentos_maximo:
    try:
        numero = int(input("Ingresa el número que crees es: "))
        intentos = intentos + 1
        if numero > numero_secreto:
            print("Número muy grande")
        elif numero < numero_secreto:
            print("Numero muy chico")
        else:
            print("Le apuntante CTM")
            break
    except ValueError:
        print("Ingresa solo números")
        continue

    if intentos == intentos_maximo:
        print(f"Perdiste, el número secreto era {numero_secreto}")

