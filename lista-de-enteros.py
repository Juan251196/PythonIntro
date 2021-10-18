n = input ("Tamño de la lista: ")
n = int(n)

m = input("Valor en la lista: ")
m = float (m)

if n < 50e6:
    lista = [m] * n
    print(lista)

else:
    print("La memoria no soporta este tamaño de lista")