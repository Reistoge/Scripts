# def dibujarLinea(p1):
 
#     for i in range(p1,0,-1):
#         s="*"*i
#         print(s)
#     for i in range(0,p1,+1):
#         s="*"*i
#         print(s)
    
# dibujarLinea(20)
def dias_en_el_mes(mes,año):
    if año%4==0  and mes==2 and str(año)[-1]!="0" and str(año)[-2]!="0":
        return 29
    if año%400==0 and str(año)[-1]=="0" and str(año)[-2]=="0" and mes==2:
        return 29
    
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        return 31
    if mes==2:
        return 28
    else:
        return 30
        
assert dias_en_el_mes(1, 2018)==31
assert dias_en_el_mes(2, 2018)==28
assert dias_en_el_mes(2, 2016)==29
assert dias_en_el_mes(2, 2000)==29
assert dias_en_el_mes(2, 1900)==28
assert dias_en_el_mes(5, 2018)==31
assert dias_en_el_mes(11, 2018)==30
 
def nombre_del_mes(mes):
    meses=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
    for i in range(0,12):
        if i==mes-1:
            return meses[i]
    
assert nombre_del_mes(1)=="Ene"
assert nombre_del_mes(7)=="Jul"
assert nombre_del_mes(6)=="Jun"


def escribir_calendario(año):
    print("Calendario",año)
    for mes in range(1,13):
        s=""
        s=s+nombre_del_mes(mes)
        s=s+": "
        dias=dias_en_el_mes(mes,año)
        for dia in range(1,dias +1):
            s=s+str(dia)+" "
            
        print(s)
        
    
for a in range(2015,2017):
    escribir_calendario(a)      

