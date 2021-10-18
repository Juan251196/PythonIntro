oreo = 19
fresas = 22
mandm = 25
brownie = 28
oreo =str(oreo)
fresas =str(fresas)
mandm =str(mandm)
brownie =str(brownie)

orden = input("Que sabor de helado quieres? (oreo, fresas, mandm o brownie)")
orden = orden.lower()

if orden == "oreo":
    print ("Son " + oreo + " pesos por el helado de Oreo")
    
elif orden == "fresas":
    print ("Son  " + fresas + " pesos por el helado de fresas")

elif orden == "mandm":
    print ("Son  " + mandm + " pesos por el helado de mandm")

elif orden == "brownie":
    print ("Son  " + brownie + " pesos por el helado de brownie")

else:
    print("Ese helado no lo tenemos")



