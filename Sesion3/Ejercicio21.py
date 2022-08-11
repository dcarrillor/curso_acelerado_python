'''
Fecha:10-08-2022
****Descripción: Almacena materias en una lista****
Realizado por: Yo
'''
otro=1
ganadores=[]
while otro == 1:
  numero= int(input ("Teclea numero ganador"))
  ganadores.append(numero)
  otro=int(input("Desea ingresar otro numero? 0=no   1=si "))
ganadores.sort()
print (ganadores)
  