def Crear_Diccionario(lista):
    dic = {}
    for i,e in enumerate(lista):
        dic[e]=i
    print("De la Lista {} hemos creado el diccionario {}".format(lista, dic))

#PPPPPPP
lista = ["Coche", "Casa","Vaixell","Colom","Ca","Mussol","Clara"]
Crear_Diccionario(lista)