
def generar_acronimo(significado):
    palabras = significado.split()
    acronimo = ''.join(word[0].upper() for word in palabras)
    return acronimo
