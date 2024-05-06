def imprimir_triangulo_rectangulo(altura):
    for i in range(1, altura + 1):
        print('*' * i)

try:
    altura = int(input("Altura: "))
    imprimir_triangulo_rectangulo(altura)
except ValueError:
    print("Por favor, introduce un número entero válido.")
