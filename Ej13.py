class Animal():
    def __init__(self, nom, atributo, edad):
        self.nom = nom
        self.atributo = atributo
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def quien_soy(self):
        print("Soy un animal")


class Caballo(Animal):
    def hablar(self):
        print("iiiiii")

    def moverse(self):
        print("Me muevo al trote")

    def quien_soy(self):
        print("Soy un caballo")


class Delfin(Animal):
    def hablar(self):
        print("ichcich")

    def moverse(self):
        print("Me muevo nadando")

    def quien_soy(self):
        print("Soy un delfín")


class Abeja(Animal):
    def hablar(self):
        print("bzzz")

    def moverse(self):
        print("Me muevo con alasw")

    def quien_soy(self):
        print("Soy una abeja")


class Humano(Animal):
    def __init__(self, nom, atributo, edad):
        self.nom = nom
        self.atributo = atributo
        self.edad = edad

    def hablar(self):
        print("Hola")

    def moverse(self):
        print("Me muevo caminando")

    def quien_soy(self):
        print("Soy un humano")


class Centauro(Humano, Caballo):
    def hablar(self):
        print("Hola, nosotros usamos un idioma para hablar")

    def moverse(self):
        print("Me muevo al trote")

    def quien_soy(self):
        print("Soy un centauro")


class Hijo(Humano):
    def __init__(self, nom, atributo, edad, ll_padres):
        self.nom = nom
        self.atributo = atributo
        self.edad = edad
        self.padres = ll_padres

    def hablar(self):
        print("UeeeU")

    def moverse(self):
        print("Me muevo gateando")

    def quien_soy(self):
        print("Soy un hijo")

    def nompadres(self):
        for e in self.padres:
            print(e.nom)

# Ni idea de qué es Xou.
class Xou():
    def hablar(self):
        print("Xou")

    def moverse(self):
        print("Me muevo como un xou")

    def quien_soy(self):
        print("Soy un xou")


# Programa Principal
a = [Caballo("Negro", "5", "10"), Delfin("Gris con blanco", "7", "8"), Abeja("Negro y amarillo", "0.5", "1"),
    Humano("Ayoub", "Ahmed", "69"), Centauro("Marc", "Marron", "16"),
    Hijo("David", "Albino", "16",["A", "B"]), Xou()]

for e in a:
    e.hablar()
    e.moverse()
    e.quien_soy()