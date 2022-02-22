# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:30:24 2022

@author: Tamandua
"""
import csv
import math
import hashlib
import pandas as pd

def main():
    #escolha do rssi
    rssi = 2
    pos_rssi = rssi + 4
    lista_numeros_rssi = []
    lista_numeros_rssi_positivos = []
    
    #leitura do arquivo
    with open('arquivos/combined_hourly_data.csv', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            lista_numeros_rssi.append(row[pos_rssi])
    
    coluna = lista_numeros_rssi[0]
    #df = pd.read_csv('arquivos/combined_hourly_data.csv', delimiter=';')

    # with open('arquivos/csv_filtrado.csv', 'w', newline='') as file:
    #     writer = csv.writer(file, delimiter=';')#, quoting=csv.QUOTE_NONE)
        
    #     for x in lista_numeros_rssi:
    #         writer.writerow(x)
  
    lista_numeros_rssi.pop(0)
    
    for x in lista_numeros_rssi:
        if x != float('NaN'): 
            lista_numeros_rssi_positivos.append(math.trunc(abs(float(x))))
    
    p = 0
    q = 0
    
    #Tenta encontrar um número primo da lista de rssi
    for x in lista_numeros_rssi_positivos:
        if verificaPrimo(x):
            if p==0:
                p=x
            elif q==0 and x!=p:
                q=x
            if p!=0 and q != 0:
                break
    
    #Se não for encontrado um número primo, verifica um próximo da lista
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
    
    #print(p)
    #print(q)
    
    n_euler = oneway_function(p, q)
    
    hash_hex = funcao_hash(n_euler)
    valor_binario = converter_hex_binario(hash_hex)
    
    lista_numeros_rssi.insert(0, coluna)
    df = pd.DataFrame(lista_numeros_rssi)
    df.to_csv('arquivos/csv_filtrado.csv', index = False, header = False)
    
    resultado = []
    
    resultado.append('Numero p: ' + str(p))
    resultado.append('Numero q: ' + str(q))
    resultado.append('Numero n gerador pelo Polinomio de Euler: ' + str(n_euler))
    resultado.append('Hash: ' + str(hash_hex))
    resultado.append('Valor Binario: ' + str(valor_binario))
    
    df = pd.DataFrame(resultado)
    df.to_csv('arquivos/resultado.txt', index = False, header = False)
    

#função para verificar se o número é primo
def verificaPrimo(numero):
    contador = 0
    for x in range (1,numero+1):
        if numero%x == 0:
            contador = contador+1
        if contador >2:
            return False
        
    return True

#função para o polinomio de euler
def oneway_function(p,q):
    n = p * q % 40
    
    #polinômio de Euler
    f = (n*n) - n + 41
    
    return f

#função para criar hash
def funcao_hash(n):
    hash_object = hashlib.sha256(str(n).encode('ASCII'))
    hex_dig = hash_object.hexdigest()
    #print(hex_dig)
    return hex_dig
    
def converter_hex_binario(valor):     
    #Valor inicial
    #print ("Valor inicial", valor)
      
    #Código para converter
    n = int(valor, 16) 
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1    
    resultado = bStr
    
    # Imprime o valor em binário
    #print ("String em binário", str(resultado))
    
    return resultado
    
main()
