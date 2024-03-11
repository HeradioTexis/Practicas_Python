

# variable del loop
loop = 1
# condicion y ciclo while se repetira siempre que esta sea menos a 10
while (loop < 10): 

    # Todas las preguntas que se le realiza al usuario para que las conteste
    sustantivo = input("Selecciona un sustantivo: ")
    sustantivo_plural = input("Selecciona un sustantivo en plural: ")
    sustantivo2 = input("Selecciona un sustantivo: ")
    lugar = input("Nombra un lugar: ")
    adjetivo = input("Selecciona un adjetivo (Describe una palabra): ")
    sustantivo3 = input("Selecciona un sustantivo: ")

    # impresion
    print("------------------------------------------")
    print("Sé amable con tu", sustantivo, "- pies", sustantivo_plural)
    print("Porque un pato podría ser el", sustantivo2, "de alguien,")
    print("Sé amable con tus", sustantivo_plural, "en", lugar)
    print("Donde el clima siempre es", adjetivo, ".")
    print()
    print("Puedes pensar que esto es el", sustantivo3, ",")
    print("Bueno, lo es.")
    print("------------------------------------------")


    # Loop back to "loop = 1"
    loop = loop + 1