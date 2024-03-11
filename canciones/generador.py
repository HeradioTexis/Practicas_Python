# Importamos el modulo 'lyrics' donde estan las letras de las canciones
import letras

# Diccionario con el título de las canciones como clave y la letra como valor
songs = {
    "OH hellos - Bitter watr": letras.bitter_water,
    "OH hellos - Exeunt": letras.Exeunt,
    "King GNU - Expecialz": letras.specialz,
    "OH hellos - caesar": letras.caesar,
    "OH hellos - this wll end": letras.this_will_end,
    "NSYNC - Better Place": letras.Better_place,
    "OH hellos - Pale white horse": letras.white,
    "OH hellos - where is your rider": letras.rider,
    "OH hellos - soldier,poet,king": letras.SPK,
    "OH hellos - deear warmwood": letras.dear,
    "OH hellos - thus always to tyrant": letras.thus,   
}

# Imprime la lista de canciones
print("Lista de canciones:")
for i, song in enumerate(songs, 1):
    print(f"{i}. {song}")

# Pedir al usuario que elija una canción
option = int(input("Elige una canción (1-11): "))

# Verificar si la opción del usuario es válida
if option < 1 or option > 11:
    print("Opción inválida")
else:
    # Obtener el título de la canción seleccionada
    songTitle = list(songs.keys())[option - 1]
    
    # Obtener la letra de la canción seleccionada
    songLyrics = songs[songTitle]
    
  # Imprimir la letra de la canción seleccionada
    print(f"\nElejiste: '{songTitle}' Aqui tienes. \n --------------- {songTitle}--------------- \n{songLyrics}")