def div(a,b):
    try:
        c= a/b
        print("La divisio {} entre {} es {}".format(a,b,c))
    except ZeroDivisionError:
        print("El seegon parametre no pot ser zero")

#P
a= int(input("Escriu el numero: "))
b= int(input("Escriu el denominador: "))
div(a,b)