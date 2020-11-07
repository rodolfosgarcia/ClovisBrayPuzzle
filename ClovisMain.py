#!/usr/bin/env pythonpy.exe
import csv
import urllib.request

"""
1. ler excel/csv com os dados
2. abrir URL (gif) como texto
3. ler as informacoes como texto
4. adicionar em uma tabela os ID
    4.1 verificar duplicados e incoerencias
5. adicionar em uma tabela os pixels
    5.1 verificar duplicados
    5.2 verificar inconsistencias (mesmo localidade com info diferente)
    5.3 verificar quando nao vazio
"""


print ('hello!')
with open ('../BLARGv2.csv', encoding='utf8') as csvFile:
    i = []
    spamReader = csv.reader(csvFile, delimiter=',')
    for row in spamReader:
        #print (row[3])
        # with open (row[3], encoding='utf8') as gifFile:
        #     for line in gifFile:
        #         print (line)
        gifData = urllib.request.urlopen(row[3], )
        for i, line in enumerate(gifData):
            #print (i, line)
            if i == 0:
                #gif ID??
                GifID = str(line).split("'")[1].split("\\")[0]
                #print (GifID)
            elif i == 2:
                #grid type
                gridType = str(line).split("'")[1][58:63]
                #print (gridType)
            elif i == 4:
                #SEQ!
                SeqIDValue = str(line).split(":")[1][1:-5]
                #print (SeqIDValue)
                letra = SeqIDValue.split("'")[1]
                #print (letra)
            elif i >= 9 and i <= 13:
                #grid bytes
                xy = str(line).split(":")[0].split(' ')[1].split(',')
                X = xy[0] 
                Y = xy[1]
                #print(X)
                #print(Y)

                msg = str(line).split(":")[1].split('(')
                message = msg[0][1:]
                #print (message)
                color = msg[1].split(' ')[1][:-6]
                #print (color)
                #print(line)
            elif i > 13:
                break
            
        if Y == '0':
            #i[int(X)] = letra
            #print (letra + ' ' + X + ' ' + row[3])
            
        #break
    #print (i)
    print ('end')