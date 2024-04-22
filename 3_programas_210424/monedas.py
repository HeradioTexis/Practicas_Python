def convertir_a_monedas(cantidad):
 
    monedas_20 = 0
    monedas_10 = 0
    monedas_5 = 0
    monedas_1 = 0
    

    monedas_20 = cantidad // 20
   
    cantidad -= monedas_20 * 20
    
   
    monedas_10 = cantidad // 10
    cantidad -= monedas_10 * 10
    
    
    monedas_5 = cantidad // 5
    cantidad -= monedas_5 * 5
    
   
    monedas_1 = cantidad
    
    
    print("Monedas de $20:", monedas_20)
    print("Monedas de $10:", monedas_10)
    print("Monedas de $5:", monedas_5)
    print("Monedas de $1:", monedas_1)


cantidad = int(input("Cantidad a Convertir: "))


convertir_a_monedas(cantidad)
