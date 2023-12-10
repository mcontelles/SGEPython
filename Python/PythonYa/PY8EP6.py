'''De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.'''
sueldo = float(input("Ingrese el sueldo del operario: "))
antiguedad = int(input("Ingrese los años de antigüedad del operario: "))

if sueldo < 500:
    if antiguedad >= 10:
        aumento = 0.20
        sueldo_a_pagar = sueldo * (1 + aumento)
        print(f"Se otorga un aumento del 20%. Sueldo a pagar: {sueldo_a_pagar:.2f}")
    else:
        aumento = 0.05
        sueldo_a_pagar = sueldo * (1 + aumento)
        print(f"Se otorga un aumento del 5%. Sueldo a pagar: {sueldo_a_pagar:.2f}")
else:
    print(f"El sueldo del operario es {sueldo:.2f}. No hay cambios.")
