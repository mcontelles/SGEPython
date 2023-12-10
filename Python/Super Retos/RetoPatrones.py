def numeroPatrones(texto):
    texto = texto.upper()
    patrones = ["00", "101", "ABC", "HO"]
    contador = 0
    
    for patron in patrones:
        inicio = 0
        while inicio != -1:
            inicio = texto.find(patron, inicio)
            if inicio != -1:
                contador += 1
                inicio += 1
    
    return contador

cadena = "000"
resultado = numeroPatrones(cadena)
print(resultado)
