nom_fitxer = "Prueba.bmp"

# Obrim el fitxer en mode binari de lectura (`rb`)
with open(nom_fitxer, "rb") as f:
    # Saltem els 1078 bytes de capçalera del fitxer BMP
    f.seek(1070)

    # Llegim els 400 bytes de dades de la imatge (20x20 píxels, 3 bytes per píxel)
    dades = f.read(400)

    # Recorrem els bytes utilitzant for in range
    for i in range(len(dades)):
        # i és l'índex (de 0 a 399)
        # dades[i] retorna el valor enter del byte
        print(f"Pixel {i + 1} {dades[i]}")


        


    

