# Construya un programa que lea el archivo e indique, de las personas con un IMC
# entre 18.50 y 24.99, el
# nombre de la persona de mayor estatura.

def obtener_mayorIMC():
    arch=open("14.txt","r",encoding="utf-8")
    line=arch.readline().strip()
    highest_imc=0
    highest_name=""
    while line!="":
        peso=float(line.split(",")[2])
        altura=float(line.split(",")[1])
        imc=peso/altura
        name=line.split(",")[0]
        if imc>highest_imc:
            
            highest_imc=imc
            highest_name=name
            
        line=arch.readline().strip()
    print(highest_imc,highest_name)
    

    
obtener_mayorIMC()   
    
    
        
    
    
        




    
        
    
    

    
    
        