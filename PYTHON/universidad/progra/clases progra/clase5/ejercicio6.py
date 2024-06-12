# Imagina lo siguiente: quieres correr una distancia d. Pero una vez que llegas a la mitad 
# de tu recorrido, te das cuenta que aun te falta la mitad, así que decides incrementar tu 
# velocidad en un 50%. Pero una vez que llegas a la mitad de lo que te faltaba, te das 
# cuenta que aun te falta mucho, así que vuelves a aumentar tu velocidad en un 50%. Y 
# así sucesivamente.
# ¿Cuánto tiempo te demorará recorrer la distancia?
# Todos sabemos que :
# velocidad= 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑖𝑎∕𝑡𝑖𝑒𝑚𝑝𝑜
# por lo que tiempo= 𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑖𝑎∕𝑣𝑒𝑙𝑜𝑐𝑖𝑑𝑎d
        
   
    
def return_time(speed, distance):
    while distance>0.01:
        distance=distance/2
        print(distance/speed)
        print(distance, speed)
        speed=speed+(0.5*speed)
        
        
  

    
return_time(2, 100)
 
    
