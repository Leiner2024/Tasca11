def Coincidencia(lista):
    l = []
    for i,e in enumerate(lista):
        if e == i:
            l.append(e)
            print("Los elementos de la lista {}\nque coinciden en su posición son {}".format(lista,l))

#pPPPPPPPPPppepepe
l = [3,7,2,3,4,5,6,7,8,9,10,1]
Coincidencia(l)