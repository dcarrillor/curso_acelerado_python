'''
**** Realizada por : yo***
Fecha:10-08-2022
Descripción: Lista de menor a mayor
'''
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
 if price < min:
 min = price
 elif price > max:
 max = price
print("El mínimo es " + str(min))
print("El máximo es " + str(max))
