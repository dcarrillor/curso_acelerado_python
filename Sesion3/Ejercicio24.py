otro=1
monedas = {'Euro': 'E', 'Dolar': '$$','Peso': '$'}

while otro ==1:
  seleccion= input("escriba el nombre de la moneda: Dollar,Euro o Peso ")
  #print(monedas [seleccion])
  print (monedas.get(seleccion.title(), "la divisa no esta"))
  otro=int(input("1=si 0 =no"))
  
#print (seleccion.values)  