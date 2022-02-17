# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:30:24 2022

@author: Tamandua
"""
import csv

def main():
    rssi = 1
    pos_rssi = rssi + 4
    lista_numeros_rssi = []
    with open('arquivos/combined_hourly_data.csv', newline='') as file:
        reader = csv.reader(file, delimiter=';', quoting=csv.QUOTE_ALL)
        for row in reader:
            lista_numeros_rssi.append(row[pos_rssi])
            
    for x in lista_numeros_rssi:
        print(x)
    
    a = verificaPrimo(4)


def verificaPrimo(numero):
    contador = 0
    for x in range (1,numero+1):
        if numero%x == 0:
            contador = contador+1
        if contador >2:
            return False
        
    if contador >2:
        return False
    else:
        return True
        
    

     
        
main()
