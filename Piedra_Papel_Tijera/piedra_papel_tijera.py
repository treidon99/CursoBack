import random

print("Bienvenido a piedra papel o tijera")

puntaje_pc = 0
puntaje_jugador = 0
while puntaje_pc<3 and puntaje_jugador<3:

    eleccion_valida = 1
    while eleccion_valida == 1:

        f = input("Elija entre Papel, Piedra o Tijera, escribiendo tu eleccion: ")

        if f == "Tijera" or f == "tijera":

            e = 1
            eleccion_valida = 0

        elif f == "Papel" or f == "papel":

            e = 2
            eleccion_valida = 0

        elif f == "Piedra" or f == "piedra":

            e = 3
            eleccion_valida = 0

        else:

            print("Eleccion invalida")

    eleccion = [1,2,3]
    pc = random.choice(eleccion)

    if pc == e:
        print("Empate")
        print ("Puntaje jugador: "+str(puntaje_jugador))
        print ("Puntaje PC: "+str(puntaje_pc))
    elif pc == 1 and e == 2:
        puntaje_pc += 1
        print ("Punto para el pc")
        print ("Puntaje jugador: "+str(puntaje_jugador))
        print ("Puntaje PC: "+str(puntaje_pc))
    elif pc == 1 and e == 3:
        puntaje_jugador += 1
        print ("Punto para el jugador")
        print ("Puntaje jugador: "+str(puntaje_jugador))
        print ("Puntaje PC: "+str(puntaje_pc))    
    elif pc == 2 and e == 1:
        puntaje_jugador += 1
        print ("Punto para el jugador")
        print ("Puntaje jugador: "+str(puntaje_jugador))
        print ("Puntaje PC: "+str(puntaje_pc))
    elif pc == 2 and e == 3:
        puntaje_pc += 1
        print ("Punto para el pc")
        print ("Puntaje jugador: "+str(puntaje_jugador))
        print ("Puntaje PC: "+str(puntaje_pc))
    elif pc == 3 and e == 1:
        puntaje_pc += 1
        print ("Punto para el pc")
        print ("Puntaje jugador: "+str(puntaje_jugador))
        print ("Puntaje PC: "+str(puntaje_pc))
    elif pc == 3 and e == 2:
        puntaje_jugador += 1
        print ("Punto para el jugador")
        print ("Puntaje jugador: "+str(puntaje_jugador))
        print ("Puntaje PC: "+str(puntaje_pc))

if puntaje_jugador == 3:
    print("Gana jugador")
    print ("Puntaje jugador: "+str(puntaje_jugador))
    print ("Puntaje PC: "+str(puntaje_pc))
if puntaje_pc == 3:
    print("Gana PC")
    print ("Puntaje jugador: "+str(puntaje_jugador))
    print ("Puntaje PC: "+str(puntaje_pc))


#LOWERCASE AND UPERCASE, MOSTAR LA OPCION DEL PC Y ELEGIR LA OPCION POR MEDIO DE UN ARREGLO