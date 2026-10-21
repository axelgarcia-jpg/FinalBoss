#iniciar estado de registros
from ast import If


Estado = 0
#Crear archivo con 100 registros iniciales
with open("archivo.txt", "w") as archivo:
    for i in range(0,100):
     archivo.write(f"{Estado},0,Sin Nombre,0\n")
#Preguntar que quiere hacer el usuario
Seleccion = input(str("Desea modificar, Dar de alta, Dar de baja o Consultar un registro? (M/A/B/C) "))
#Por si quiere dar de alta un registro
if Seleccion == "A":
   numero_de_registro = input(str("Número de registro... (0-99) "))
   nombre = input(str("Nombre... "))
   telefono = input(str("Telefon... "))

   with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()
    Estado = 1
    lineas[int(numero_de_registro)] = f"{Estado},{numero_de_registro},{nombre},{telefono}\n"

   with open("archivo.txt", "w") as archivo:
    archivo.writelines(lineas)

#Por si quiere dar de baja un registro
if Seleccion == "B":
    numero_de_registro = input(str("Número de registro... (0-99) "))
    with open("archivo.txt", "r") as archivo:
     lineas = archivo.readlines()
     Estado = 0
     lineas[int(numero_de_registro)] = f"{Estado},0,Sin Nombre,0\n"
    with open("archivo.txt", "w") as archivo:
     archivo.writelines(lineas)

#Por si quiere modificar un registro
if Seleccion == "M":
    numero_de_registro = input(str("Número de registro... (0-99) "))
    nombre = input(str("Nombre... "))
    telefono = input(str("Telefon... "))

    with open("archivo.txt", "r") as archivo:
     lineas = archivo.readlines()
     Estado = 1
     lineas[int(numero_de_registro)] = f"{Estado},{numero_de_registro},{nombre},{telefono}\n"

    with open("archivo.txt", "w") as archivo:
     archivo.writelines(lineas)

#Por si quiere consultar un registro
if Seleccion == "C":
    numero_de_registro = input(str("Número de registro... (0-99) "))
    with open("archivo.txt", "r") as archivo:
     lineas = archivo.readlines()
     if Estado == 1:
      print(lineas[int(numero_de_registro)])
     if Estado == 0:
      print("Registro no dado de alta.")
    
else:
    print("Opción no válida. Por favor, seleccione M, A, B o C.")

