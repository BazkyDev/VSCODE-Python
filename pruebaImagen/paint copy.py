nom_fitxer = "Prueba.bmp"
valor_vermell = 79
# Obrim el fitxer en mode binari de lectura (`rb`)
with open(nom_fitxer, "rb") as f:
    # Saltem els 1078 bytes de capçalera del fitxer BMP
    capcalera = f.read(1078)

    pixels = bytearray(f.read(400))
    
    

    # Recorrem els bytes utilitzant for in range
    for i in range(len(pixels)):
        pixels[i] = valor_vermell






    

