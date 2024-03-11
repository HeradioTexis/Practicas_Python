from ppt import obtener_jugada, determinar_ganador
import random

print("Bienvenido al juego de piedra, papel o tijeras.")
    
while True:
        jugador1 = obtener_jugada()
        jugador2 = random.choice(['piedra', 'papel', 'tijeras'])
        
        print(f"Jugador 1 eligió {jugador1}")
        print(f"Jugador 2 eligió {jugador2}")
        
        ganador = determinar_ganador(jugador1, jugador2)
        print(f"¡{ganador} gana la ronda!\n")
        
        jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra_vez != 's':
            print("¡Gracias por jugar! Hasta luego.")
            break



