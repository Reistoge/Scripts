# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:50:33 2023

@author: Ferran Rojas
"""
def formatear_hora(minutos):
    horas=minutos//60
    dias=horas//24
    minutos=minutos%60
    horas-=dias*24
    print(dias,horas,minutos)
formatear_hora(3000)        