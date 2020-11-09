#!/usr/bin/env pythonpy.exe
import urllib.request

urlText = 'https://www.bungie.net/pubassets/blarg/fragment_v2_03cf1423-e8ef-4112-abe1-323f2ecf7f2e.gif'
gifData = urllib.request.urlopen(urlText, )
for i, line in enumerate(gifData):
    print (i, line)
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