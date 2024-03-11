

import string

translator = str.maketrans('', '', string.punctuation)

print("-jefe quisiera una palabra!!!")
print("-Que tal largo ?")
print("-dos palabras Largo chico o diciseis?")

word_count = {}

text = "Fuera de mi oficina en dos coma tres segundos o te enganchare a un hasta bandera"
print(text)


words = text.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

total_words = sum(word_count.values())
print("")
print(f"El ultimo texto  contiene un total de {total_words} palabras.")
