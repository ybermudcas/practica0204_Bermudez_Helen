nombre = input("¿Cuál es tú nombre?")
edad = int(input("¿Cuál es tú edad?"))
dirección = input("¿Cuál es tú dirección?")
móvil = input("¿Cuál es tú número de móvil?")
diccionario = {"Nombre": nombre, "Edad": edad, "Dirección": dirección, "Móvil": móvil}

print(diccionario["Nombre"], "tiene", diccionario["Edad"], "años,", "vive en", diccionario["Dirección"], "y su número de móvil es", diccionario["Móvil"])
