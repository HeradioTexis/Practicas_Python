import random

def obtener_jugada():
    """Obtiene la jugada del jugador."""
    jugada = input("Elige piedra, papel o tijeras: ").lower()
    while jugada not in ['piedra', 'papel', 'tijeras']:
        print("Por favor, elige una opción válida.")
        jugada = input("Elige piedra, papel o tijeras: ").lower()
    return jugada

def determinar_ganador(jugador1, jugador2):
    """Determina el ganador de la ronda."""
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == 'piedra' and jugador2 == 'tijeras') or \
         (jugador1 == 'tijeras' and jugador2 == 'papel') or \
         (jugador1 == 'papel' and jugador2 == 'piedra'):
        return "Jugador 1"
    else:
        return "Jugador 2"
    
