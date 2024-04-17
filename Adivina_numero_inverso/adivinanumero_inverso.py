import random

limite_inferior = 1
limite_superior = 50
respuesta = None
intentos = 0

print("Piensa en un número del 1 al 100 y yo trataré de adivinarlo.")

while respuesta != "correcto":
    intento = random.randint(limite_inferior, limite_superior)
    print(f"¿Es {intento} tu número, o es demasiado alto (alto), demasiado bajo (bajo) o correcto?")
    respuesta = input().lower()
    intentos += 1

    if respuesta == "bajo":
        limite_superior = intento - 1
    elif respuesta == "alto":
        limite_inferior = intento + 1
    elif respuesta != "correcto":
        print("Por favor, ingresa 'alto', 'bajo' o 'correcto'.")

    if limite_inferior > limite_superior:
        print("¡Hey, no hagas trampa! Tu número no puede estar en ese rango.")
        break

print(f"¡Genial! ¡Adiviné tu número en {intentos} intentos!")
