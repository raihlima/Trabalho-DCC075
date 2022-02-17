# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:30:24 2022

@author: Tamandua
"""
import csv
import math


def main():
    rssi = 2
    pos_rssi = rssi + 4
    lista_numeros_rssi = []
    lista_numeros_rssi_positivos = []
    
    with open('arquivos/combined_hourly_data.csv', newline='') as file:
        reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_ALL)
        for row in reader:
            lista_numeros_rssi.append(row[pos_rssi])
    
    with open('arquivos/csv_filtrado.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';', quoting=csv.QUOTE_NONE)
        
        for x in lista_numeros_rssi:
            writer.writerow(x)
    
    lista_numeros_rssi.pop(0)
    
    for x in lista_numeros_rssi:
        print(x)
        lista_numeros_rssi_positivos.append(math.trunc(abs(float(x))))
        
    for x in lista_numeros_rssi_positivos:
        print(x)
    
    a = verificaPrimo(4)


def verificaPrimo(numero):
    contador = 0
    for x in range (1,numero+1):
        if numero%x == 0:
            contador = contador+1
        if contador >2:
            return False
        
    return True
        
    

     
        
main()
