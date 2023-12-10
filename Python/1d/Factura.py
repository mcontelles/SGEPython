cont = 1
precioTotal = float(0)
precio = float(input(f"Precio del producto Nº{cont}: "))
while precio!=0:
    cont+=1
    precioTotal+=precio
    precio = float(input(f"Precio del producto Nº{cont}: "))
print(f"Precio total: {precioTotal:.2f}")