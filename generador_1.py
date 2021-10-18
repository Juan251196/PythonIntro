import random

letras = "qwertyuiopasdfghjklzxcvbnm"
numeros = "0123456789"
caracter="!#$%&()=?¡"
mayusculas = letras.upper()
contrasena = []

while len(contrasena) < 11:
    
    s = random.choice(letras + numeros + mayusculas) 
    contrasena.append(s)

c = random.choice(caracter)
contrasena.append(c)
random.shuffle(contrasena)

print("".join(contrasena))

## RETO

## 1. La contraseña debe ser de 12 caracteres
## 2. La contraseña debe tener letras en mayúscula
## 3.- Debe contener 1 sólo caracter especial
