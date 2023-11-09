diccionario = {"Pan":1.40, "Huevos": 2.30, "Cebollas": 0.85, "Aceite": 4.35}
artículo = input("¿Qué artículo quieres?")
unidades = int(input("¿Cuántas unidades quieres?"))


if artículo.title() in diccionario:
    precio_artículo = diccionario[artículo.title()]
    precio_unidades = precio_artículo * unidades

    print("El precio de", artículo.title(), "al llevar", unidades, "unidades es de", precio_unidades)

else:
    print("El artículo que ingresaste no se encuentra disponible")