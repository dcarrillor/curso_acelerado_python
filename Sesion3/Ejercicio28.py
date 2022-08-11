
opcion=1
facturas={}
while opcion!=0:
  print("=========      MENU       ===========")
  print("0. Terminar")
  print("1. Añadir Factura")
  print("2. Pagar Factura")
  print("3. Imprimir Facturas Pendientes")
  opcion=int(input("Selecciona una opcion: "))
  if opcion==1:
    num=int(input("Numero de factura: "))
    if facturas.get(num)==None:
      coste=float(input("Coste: $"))
      facturas[num]=coste
    else:
      print("Numero de factura ya existe!")
  elif opcion==2:
    num=int(input("Numero de factura a pagar: "))
    if facturas.get(num)!=None:
      del(facturas[num])
      print("Factura pagada")
    else:
      print("Numero de factura no existe!")
  elif opcion==3:
    print(facturas)
