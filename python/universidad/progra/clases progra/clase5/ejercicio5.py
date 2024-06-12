# La empresa ABCDEN de Coquimbo está realizando un remate de los últimos productos que le están 
# quedando debido al quiebre de la empresa, por lo cual se requiere construir un programa para 
# obtener información de las ganancias posibles que se pueden obtener.
# Para esto, se cuenta con los siguientes archivos:
# • artículos.txt: Contiene el nombre del producto y la cantidad disponible (Kgs)
# • precios.txt: Contiene el precio de cada producto ($/Kgs)
# Con dicha información usted debe realizar lo siguiente:
# Crear una función que permita obtener el total de dinero que se obtendrá del remate. Además, 
# deberá recibir como parámetro el porcentaje de descuento que se le brindará al potencial cliente. El 
# programa debe informar el valor final a cancelar por parte del cliente.
# El programa además deberá informar el producto con mayor precio (nombre y valor), para ello 
# deberá crear una función de nombre MAYOR que tenga como funcionalidad obtener el precio 
# mayor

def saltar_lineas(n):
    print("\n"*int(n))
    
def remate(porcentaje):

    arch1=open("precios.txt", "r", encoding="utf-8")
    linea1=arch1.readline()
    total=0
    precio_mayor=0
    articulo_caro=""
    while linea1!="":
         arch2=open("articulos.txt", "r", encoding="utf-8")
         articulo=linea1.split(",")[0]
         cantidad=linea1.split(",")[1]
         linea2=arch2.readline()
         while linea2.split(",")[0]!=articulo:
             linea2=arch2.readline()
        
         precio=float(linea2.split(",")[1])
         if  precio > precio_mayor:
             precio_mayor=precio
             articulo_caro=articulo
         descuento=float(precio)-(float(precio)*(porcentaje/100))
         total+=descuento*float(cantidad)
         arch2.close()
         linea1=arch1.readline()
    print("TOTAL DE TU COMPRA ES", str(total)+"$")
    print("el producto más caro es", articulo_caro, "con un precio de", str(precio_mayor),"$")
    
    
n=0
while int(n)!=-1:
    n=input("Ingresa el porcentaje: ")
    while not n.isdigit():
        saltar_lineas(100)
        print("debes de introducir un numero")
        n=input("ingresa el porcentaje: ")
        
 
    saltar_lineas(100)
    remate(int(n))
        
        
   
    
    

    

 
    
