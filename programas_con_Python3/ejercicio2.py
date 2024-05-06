def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

def imprimir_triangulo_primos(numero):
    for i in range(numero, 0, -1):
        for j in range(i, 0, -1):
            if es_primo(j):
                print(j, end=' ')
        print()

try:
    numero = int(input("Número: "))
    if es_primo(numero):
        imprimir_triangulo_primos(numero)
    else:
        print("Por favor, introduce un número entero primo.")
except ValueError:
    print("Por favor, introduce un número entero válido.")
