
count=True
while count== True:
    #Solicitamos el nombre del usuario
    nombre = input("Ingresa tu nombre:  ")
    opcion= input("Tu nombre es correcto?(y/n):  ")
    if(opcion=="y"):
        count = False


count=True
while count== True:
    nacimiento = input("Ingresa tu fecha de nacimiento:  ")
    opcion = input("Tu fecha de nacimiento es correcta?(y/n):  ")
    if(opcion=="y"):
        count = False


#Se repiten los mismos pasos que con el nombre 
count=True
while count== True:
    direccion = input("Ingresa tu direccion:  ")
    opcion = input("Tu direccion es correcta?(y/n):  ")
    if(opcion=="y"):
        count = False


#Se repiten los mismos pasos que con el nombre 
count=True
while count== True:
    meta = input("Ingresa una meta personas:  ")
    opcion = input("Tu meta es correcta?(y/n):  ")
    if(opcion=="y"):
        count = False

#Cuando es usuario confirma todos los datos se imprime el siguiente formato
#con los datos del usuario 
print("- Nombre: ",nombre)
print("- Dia de nacimiento: ",nacimiento)
print("- direccion: ",direccion)
print("- Meta personal: ",meta)