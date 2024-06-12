def obtener_tiempo(minutos):
    if minutos>=1440:
        dias=minutos//(60*24)
        horas_no_formateadas=minutos%(60*24)
        horas=horas_no_formateadas//60
        minutos=horas_no_formateadas%60
        
        
        print(dias,horas,round(minutos))
    
    elif minutos<1440:
        horas=minutos//60
        minutos=(minutos%60)
        print(horas, minutos)
obtener_tiempo(1438)