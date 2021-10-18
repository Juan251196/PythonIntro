edad = input  ("Cuál es tu edad?")
edad = int(edad)

credencial = input ("Tienes credencial? (s/n): ")



if edad >= 18 and credencial == "s":
    print ("Puedes votar!")
elif edad == 17 and credencial == "n":
    print("Tramita tu credencial para votar")
else:
    print("No puedes votar")
print ("Adios")