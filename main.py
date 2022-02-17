# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:30:24 2022

@author: Tamandua
"""
import csv
import math
import hashlib

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
        lista_numeros_rssi_positivos.append(math.trunc(abs(float(x))))
    
    p = 0
    q = 0
    
    for x in lista_numeros_rssi_positivos:
        if verificaPrimo(x):
            if p==0:
                p=x
            elif q==0 and x!=p:
                q=x
        if p!=0 and q != 0:
            break
    
    if p==0 or q==0:
        for x in lista_numeros_rssi_positivos:
            for y in range (1,x):
                if verificaPrimo(x-y):
                    if p==0:
                        p=x-y
                    elif q==0 and (x-y)!=p:
                        q=x-y
                    break
                if p!=0 and q != 0:
                    break
            if p!=0 and q != 0:
                break
    
    print(p)
    print(q)
    
    funcao_hash(oneway_function(p, q))


def verificaPrimo(numero):
    contador = 0
    for x in range (1,numero+1):
        if numero%x == 0:
            contador = contador+1
        if contador >2:
            return False
        
    return True
        
def oneway_function(p,q):
    n = p * q % 40
    
    #polinômio de Euler
    f = (n*n) - n + 41
    
    return f

def funcao_hash(n):
    hash_object = hashlib.sha256(b'n')
    hex_dig = hash_object.hexdigest()
    print(hex_dig)
    
    
main()
