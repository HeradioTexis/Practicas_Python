import random

# Definir la lista vacía
mi_lista = []

# Generar 10 valores aleatorios y agregarlos a la lista
for i in range(10):
# Inserta un número aleatorio entre 1 y 100 en la posición i    
    mi_lista[i:i] = [random.randint(1, 100)] 
# Imprime
print("mi_lista:", mi_lista)
# Copiar los valores de mi_lista 
otra_lista = mi_lista.copy()
# Inicializar una lista para almacenar los elementos de otra_lista en orden aleatorio
lista_aleatoria = []
# Obtener los elementos de otra_lista en un orden aleatorio sin usar shuffle
while otra_lista:
    indice_aleatorio = random.randint(0, len(otra_lista) - 1)  # Generar un índice aleatorio
    elemento_aleatorio = otra_lista.pop(indice_aleatorio)  # Eliminar y obtener el elemento seleccionado aleatoriamente
    lista_aleatoria.append(elemento_aleatorio)  # Agregar el elemento a la nueva lista

# Imprimir la nueva lista con los elementos en orden aleatorio
print("lista_aleatoria:", lista_aleatoria)
