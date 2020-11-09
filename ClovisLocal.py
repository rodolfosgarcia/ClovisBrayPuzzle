#!/usr/bin/env pythonpy.exe
import os
from PIL import Image

print ('start decoding')

dir = 'C:/Users/ro_rs/Documents/Projetos/Clovis/GIFs/'
testFile = ''
lista = []
listaLetra = []
coord = (20,20)

contaBranco = 0
contaPreto = 0
contaAmarelo = 0
contaNulo = 0

LcontaBranco = []
LcontaPreto = []
LcontaAmarelo = []
LcontaNulo = []

frameSelector = 16

#print (listX)
for filename in os.listdir(dir):
    if filename.endswith(".gif") and (filename == testFile or testFile == ''):
        #print(filename)
        with open (dir+filename, encoding="utf8", errors='ignore') as gifData:
            # for i, line in enumerate(gifData):
            #     #print (i, line)
            #     if i == 0:
            #         if "DOCTYPE html" in line:
            #             break
            #     #if i == 2:
            #         #grid type
            #         #gridType = str(line).split("'")[1][58:63]
            #         #print (gridType)
            #     elif i == 4:
            #         #SEQ!
            #         SeqIDValue = str(line).split(":")[1]
            #         #print (SeqIDValue)
            #         letra = SeqIDValue.split("'")[1]
            #         #print (letra)
            #         if letra not in listaLetra:
            #             listaLetra.append(letra)
            #     elif i >= 9 and i <= 13:
            #         #grid bytes
            #         xy = str(line).split(":")[0].split(' ')[1].split(',')
            #         X = int(xy[0])
            #         Y = int(xy[1])
            #         #print(X, Y)
            #         msg = str(line).split(":")[1].split('(')
            #         message = msg[0][1:]
            #         #print (message)
            #         color = msg[1].split(' ')[1][:-6]
            #         #print (color)
            #         #print(line)
            #     elif i > 13:
            #         break
            # if X == 0:
            #     lista.append(str(Y).zfill(2)+' '+filename+' '+letra)
            
            im = Image.open(dir+filename)
            
            # try:
            #     im.seek(frameSelector)
            #     color = im.getpixel(coord)
            #     if color == 0: contaBranco += 1
            #     elif color == 1: contaPreto += 1
            #     else: contaAmarelo += 1
            # except EOFError:
            #     contaNulo += 1
            
            for frame in range (0, im.n_frames):
                im.seek(frame)
                color = im.getpixel(coord)
                if color == 0:
                    if frame < len(LcontaBranco):
                        LcontaBranco[frame] += 1
                    else:
                        LcontaBranco.append(1)
                elif color == 1:
                    if frame < len(LcontaPreto):
                        LcontaPreto[frame] += 1
                    else:
                        LcontaPreto.append(1)
                else:
                    if frame < len(LcontaAmarelo):
                        LcontaAmarelo[frame] += 1
                    else:
                        LcontaAmarelo.append(1)

#print('frame:'+str(frameSelector), 'A:'+str(contaAmarelo), 'N:'+str(contaNulo), 'B:'+str(contaBranco), 'P:'+str(contaPreto))
print(LcontaPreto)
# lista.sort()
# for rep in lista:
#     print (rep)
# for letra in listaLetra:
#     print (letra)