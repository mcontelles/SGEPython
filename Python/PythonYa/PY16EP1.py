'''Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Mostrar el nombre de persona menor en orden alfabético'''
nombres = [input("Ingrese el nombre de la persona: ") for _ in range(5)]
nombre_menor = min(nombres)

print(f"El nombre de la persona menor en orden alfabético es: {nombre_menor}")