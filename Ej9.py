def pot(p):
    r = [x**p for x in range(1,10)]
    print("Las Potencias elevadas a {} de los 10 primeros números es {}".format(p,r))

#PPPP
p = int(input("Introduce un número a cualquiera elevar el resto: "))
pot(p)