#!/usr/bin/env pythonpy.exe
import os

print ('start decoding')

dir = 'C:/Users/ro_rs/Documents/Projetos/Clovis/GIFs/'
listX = []
for i in range(48):
    listX.append([])

#print (listX)
for filename in os.listdir(dir):
    if filename.endswith(".gif"):
        #print(filename)
        with open (dir+filename, encoding="utf8", errors='ignore') as gifData:
            for i, line in enumerate(gifData):
                #print (i, line)
                if i == 0:
                    if line == "<!DOCTYPE html>":
                        break
                #if i == 2:
                    #grid type
                    #gridType = str(line).split("'")[1][58:63]
                    #print (gridType)
                elif i == 4:
                    #SEQ!
                    SeqIDValue = str(line).split(":")[1]
                    #print (SeqIDValue)
                    letra = SeqIDValue.split("'")[1]
                    #print (letra)
                elif i >= 9 and i <= 13:
                    #grid bytes
                    xy = str(line).split(":")[0].split(' ')[1].split(',')
                    X = int(xy[0])
                    Y = int(xy[1])
                    #print(X, Y)
                    msg = str(line).split(":")[1].split('(')
                    message = msg[0][1:]
                    #print (message)
                    color = msg[1].split(' ')[1][:-6]
                    #print (color)
                    #print(line)
                elif i > 13:
                    break
            listX[X].insert(Y, letra)
print (listX)