import random

def juego_adivinanza():
    numero_oculto = random.randint(1, 50)
    intentos = 0

    while intentos < 5:
        try:
            intento_usuario = int(input("Adivina el número entre 1 y 50: "))
            intentos += 1

            if intento_usuario < 1 or intento_usuario > 50:
                print("Error: Por favor, elige un número dentro del rango adecuado (1-50).")
            elif intento_usuario == numero_oculto:
                print(f"¡Enhorabuena! Has adivinado el número oculto ({numero_oculto}) en {intentos} intentos.")
                break
            else:
                if intentos == 3 and 1 <= numero_oculto <= 10:
                    print(f"Pista: El número oculto está entre 1 y 10.")

                if intento_usuario < numero_oculto:
                    print("Intenta con un número más grande.")
                else:
                    print("Intenta con un número más pequeño.")

        except ValueError:
            print("Error: Ingresa un número válido.")

    if intentos == 5 and intento_usuario != numero_oculto:
        print(f"Lo siento, has agotado tus 5 intentos. El número oculto era {numero_oculto}.")







