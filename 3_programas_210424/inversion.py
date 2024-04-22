def calcular_capital(cantidad, interes, años):
    capital = cantidad
    for i in range(1, años + 1):
        capital += capital * (interes / 100)
        print(f"Capital tras {i} año(s): {capital:.2f}")


cantidad = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interés porcentual anual?: "))
años = int(input("¿Años?: "))


calcular_capital(cantidad, interes, años)
