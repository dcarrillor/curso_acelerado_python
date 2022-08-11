
nom= input("ingrese nombre ")
ed= input ("Ingresa su edad ")
dir= input("Ingresa su dirección ")
tel=input ("Escribe tu telefono ")
datos = { 
  'nombre': nom,  'edad': ed,  'direccion':dir,   'telefono':tel
}
print("Su nombre es:",datos['nombre'],"tiene",datos['edad'],"años","vive en",datos['direccion'],"y su numero de telefono es",datos["telefono"])