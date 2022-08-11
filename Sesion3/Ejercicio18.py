'''
Realizado por: Yo
***Detecta Personas uatorizadas utilizando arreglos****
'''
personas_autorizadas = ["Alberto", "Carmen","Diana","Collado","Zea"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
 print("Está autorizado")
else:
 print("No está autorizado")