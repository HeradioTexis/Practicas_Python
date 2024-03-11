from acronimo import generar_acronimo


print("Bienvenido al generador de acrónimos.")
significado = input("Ingresa el significado completo: ")
acronimo = generar_acronimo(significado)
print(f"El acrónimo para '{significado}' es: {acronimo}")
