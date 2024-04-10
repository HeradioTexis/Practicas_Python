#pedir datos
direccion_correo = input("Por favor ingresa tu dirección de correo: ")
nombre = input("Por favor ingresa tu nombre: ")
edad = input("Por favor ingresa tu edad: ")

# Definir códigos de color
color_amarillo = "\033[33m"
color_magenta = "\033[35m"
color_azul = "\033[34m"
reset_color = "\033[0m"

# Imprimir
print("Hola, mi nombre es " + reset_color + color_amarillo + nombre + reset_color + ", mi dirección es " + reset_color + color_magenta + direccion_correo + reset_color + ", y mi edad es " + reset_color + color_azul + edad + reset_color + ".")
