

def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas para hacer la comparación sin importar mayúsculas o minúsculas
    palabra = palabra.replace(" ", "")  # Eliminar espacios en blanco
    return palabra == palabra[::-1]  # Verificar si la palabra es igual a su inversa

# Solicitar entrada al usuario
entrada_usuario = input("Ingrese una palabra: ")

# Verificar si la palabra ingresada es un palíndromo
if es_palindromo(entrada_usuario):
    print(f"{entrada_usuario} es un palíndromo.")
else:
    print(f"{entrada_usuario} no es un palíndromo.")
