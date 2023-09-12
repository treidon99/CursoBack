import math

#Deficinión de clases y funciones

class triangulo ():
    def area (self):
        a = (b*h)/2
        print ("El area del triangulo es: " + str(a))


class cuadrado ():
    def area (self):
        a = b*h
        print ("El area del cuadrado es: " + str(a))

class circulo ():
    def area (self):
        a = math.pi*r*r
        print ("El area del circulo es: " + str(a))

#Logica del codigo

print("Elija entre triangulo, cuadrado o circulo")

e = input ("Dijite 1 para triangulo, 2 para cuadrado o 3 para circulo:")

if e == "1":

    b_str = input ("Dijite la base del triangulo:")
    b = int(b_str)
    h_str = input ("Dijite la altura del triangulo:")
    h = int(h_str)
    triangulo = triangulo()
    triangulo.area()

elif e == "2":

    b_str = input ("Dijite el lado del cuadrado:")
    b = int(b_str)
    h = b
    cuadrado = cuadrado()
    cuadrado.area()

elif e == "3":

    r_str = input ("Dijite el radio del circulo:")
    r = int(r_str)
    circulo = circulo()
    circulo.area()

else:

    print("Dato incorrecto")

#CODIGO FUNCIONAL