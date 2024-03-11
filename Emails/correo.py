# Pedimos un correo al usuario
email = input("ingresa tu correo elecatronico:  ").strip()

username= email[:email.index('@')]

domain = email[email.index('@')+1:]

if domain == "gmail.com":
    annex = "tu dominio es de google genial!!!"
elif domain == "outlook.com":
    annex = "tu dominio es de microsoft genial!!!"
elif domain == "hotmail.com":
    annex = "tu dominio es de microsoft genial!!!"
else:
    annex = "tu dominio es genial!!!"

result = "Tu nombre de ususario es: "+username+"\nTu dominio es: "+domain+" "+annex
print(result)