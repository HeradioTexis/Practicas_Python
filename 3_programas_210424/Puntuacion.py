def calcular_nivel_y_dinero(salario, puntuacion):
    if 0 <= puntuacion <= 3:
        nivel = "Inaceptable"
    elif 4 <= puntuacion <= 6:
        nivel = "Aceptable"
    elif 7 <= puntuacion <= 10:
        nivel = "Meritorio"
    else:
        nivel = "Puntuación fuera de rango"
    
    dinero = salario * (puntuacion / 10)
    return nivel, dinero

def main():
    salario = float(input("Por favor, introduce tu salario mensual: "))
    puntuacion = int(input("Por favor, introduce tu puntuación en la evaluación: "))
    
    nivel, cantidad_dinero = calcular_nivel_y_dinero(salario, puntuacion)
    
    print(f"Nivel de Rendimiento: {nivel}")
    print(f"Cantidad de Dinero Recibido: ${cantidad_dinero:.2f}")##el 2f hace que solo haya 2 ceros en el decimal 

8
main()

