#!/usr/bin/env pythonpy.exe
import os
import csv
import requests

print ('iniciando download dos GIFs!')

arqLidos = 0
arqEscritos = 0
arqIgnorados = 0

with open ('../BLARGv2.csv', encoding='utf8') as csvFile:
    spamReader = csv.reader(csvFile, delimiter=',')
    for row in spamReader:
        arqLidos += 1
        gifURL = row[3]
        gifName = gifURL.split('/')[5]
        if not os.path.isfile('../GIFs/'+gifName):
            img_data = requests.get(gifURL).content
            with open('../GIFs/'+gifName, 'wb') as handler:
                handler.write(img_data)
                arqEscritos += 1
        else:
            arqIgnorados += 1
            print ('arquivo repetido (' + gifName + '), ignorando')
        
        if arqLidos % 40:
                print ('Arquivos lidos: ' + arqLidos)

print ('processo finalizado, total de ' + arqEscritos + ' arquivos baixados de ' + arqLidos + ' arquivos lidos')
print ('arquivos duplicados: ' + arqIgnorados)