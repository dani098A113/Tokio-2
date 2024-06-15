def mezclar_colores():
    print("Los colores son: rojo, azul y amarillo")
    color1 = input("Elige el primer color: ")
    color2 = input("Elige el segundo color: ")
    if (color1 == 'rojo' and color2 == 'azul') or (color1 == 'azul' and color2 == 'rojo'):
        print("Ritual del vacio: púrpura.")
    elif (color1 == 'amarillo' and color2 == 'azul') or (color1 == 'azul' and color2 == 'amarillo'):
        print("Tenemos verde.")
    elif (color1 == 'rojo' and color2 == 'amarillo') or (color1 == 'amarillo' and color2 == 'rojo'):
        print("Tenemos anaranjado.")
    else:
        print("Esto esta solo por si no elegiste los colores disponibles y poque sino el programa no funciona, gracias por su comprensión.")
mezclar_colores()
