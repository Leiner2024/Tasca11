
#agfiasngo9asngoasfa
def Imprimir_Fichero(m):
    a =  []
    with open(m, "r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

def Pegar_Fichero(m,lista):
    with open(m,"a+") as f:
        for e in lista:
            f.writelines(e)


#Program pricipal 
Fichero = "/home/leiner/AO/Tasca11/ex11.txt"
lista= ["David, Joan, Jordi, Ayoub, Oscar"]
Imprimir_Fichero(Fichero)
Pegar_Fichero(Fichero, lista)