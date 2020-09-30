#Crear menu con tres opciones:
#1. opcion 1: temperaturas
#2. opcion 2: datos de personas
#3 opcion 3: salir
import os

def Temperaturas():
    print("***temperaturas***")
    #Ingresar n temperaturas donde n es un numero ingresado por teclado
    #mostrar el promerdio de las temperaturas ingresadas
    veces=int(input("Cuantas temperaturas necesita ingresar?: "))
    for x in range(veces):
        tempe=float(input("Digite una temperatura: "))
        suma=suma+tempe
    print ("El promedio de las temperaturas ingresadas es : " , round((suma/veces),2))

    pausa=input("Preione una tecla para continuar")

def Personas():
    print("*** datos de personas***")

    pausa=input("Presione una tecla paracontinuar")


seguir=True
while(seguir):
    os.system('cls')
    print("1.Temperaturas")
    print("2. datos de personas")
    print("3. salir")
    op=int(input("Ingrese opcion 1,2,3: "))
    if(op==1):
        Temperaturas()
    elif(op ==2):
        Personas()
    else:
        print("Finalizar")
        break