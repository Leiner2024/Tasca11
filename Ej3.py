def filtrar(lista, c):
    f = list(filter(lambda x:x[0]==c.lower() or x[0]==c.upper(), lista))
    print("De la Lista {}, las  palabras que comienzan por {} son {}".format(lista, c, f))

#La doble P
lista = ["Josep", "Joana", "Jordi", "Maria", "Marc", "Pera", "Paula"]
c = "j"
filtrar(lista, c)