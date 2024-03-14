def lenp(frase):
    b = frase.split(" ")
    c = list(map(len, b))
    print("La frase {} tiene la siguiente longitud {}".format(frase, c))

a = "Eso es una frase donde trabajaremos"
lenp(a)