reservacion = "RESERVACIÓN"
precio = "PRECIO"
total ="Total"
habitacion = "Habitación doble"
transporte = "Transporte"
evento = "Reservación de evento"
tour = "Tour en lancha"
alimentobebida = "Alimentos y bebidas"
precio1 = 15000.00
precio2 = 3000.00
precio3 = 3999.99
precio4 = 21750.00
precio5 = 5000.00




print("-"*25)
print(f'{reservacion:30}|{precio:>10}')
print("-"*25)
print(f'{habitacion:30}|{precio1:10}')
print(f'{transporte:30}|{precio2:10}')
print(f'{evento:30}|{precio3:10}')
print(f'{tour:30}|{precio4:10}')
print(f'{alimentobebida:30}|{precio5:10}')

print("-"*25)
print(f'{total:>30}|{precio1+precio2+precio3+precio4+precio5:10}')