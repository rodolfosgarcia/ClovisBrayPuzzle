#!/usr/bin/env python
import csv
import requests

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
with open ('../BLARGv2.csv', encoding="utf8") as csvFile:
    spamReader = csv.reader(csvFile, delimiter=',')
    for row in spamReader:
        print (row[3])
        # f = requests.get(row[3])
        # print(f.text)
        # break
    print ('end')