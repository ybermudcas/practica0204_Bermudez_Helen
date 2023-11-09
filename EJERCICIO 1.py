monedas = {"Euro":"€", "Dolar":"$", "Yen":"¥"}
pregunta = input("¿Cuál es tu divisa?")

if pregunta.title() in monedas:
    moneda_edy = monedas[pregunta.title()]
    print("Su simbolo es:", moneda_edy)

else:
    print("Tu divisa no se encuentra disponible")