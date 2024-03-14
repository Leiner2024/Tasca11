import os

#Crear directorio
os.mkdir("/home/leiner/AO/Tasca11/Prueba")
os.chdir("/home/leiner/AO/Tasca11/Prueba")

#Crear archivo y escribir un mensaje
with open("Ex12.txt", "w") as f:
    print("¡Archivo creado correctamente!")

#Lista de profesores
profesores = ["Joan", "Fela", "David", "Lluis", "Pep"]

#Añadir profesores al archivo
with open("Ex12.txt", "a+") as f:
    for e in profesores:
        f.write(e + "\n")

#Leer el archivo e imprimir su contenido
a = []
with open("Ex12.txt", "r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])
print(a)