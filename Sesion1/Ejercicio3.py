'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio3.py
Autor: yo
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
extra = float(input("Teclea Horas Extras"))
paga = (horas + extra)*coste

print("Tu paga es", paga)
