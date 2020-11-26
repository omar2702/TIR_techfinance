import numpy as npf


def Tir(periodo, inversion, flujo):
    TIR = round(npf.irr(flujo), 8)
    print("Tasa interna de retorno:", TIR * 100, "%")


def Input_Dates():
    periodo = int(input("Ingrese cantidad de periodos: "))

    while periodo < 0:
        print("Error -> Debería ser un numero positivo")
        periodo = int(input("Ingrese cantidad de periodos: "))

    inversion = int(input("Ingrese monto de la inversion incial: "))

    while inversion < 0:
        print("Error -> Debería ser un numero positivo")
        inversion = int(input("Ingrese cantidad de la inversión incial: "))

    flujo = []
    flujo.append(-inversion)

    for x in range(periodo):
        flujo.append(int(input('{} {}{}'.format("Ingrese flujo del periodo", x + 1, ": "))))
    Tir(periodo, inversion, flujo)


Input_Dates()
input()
