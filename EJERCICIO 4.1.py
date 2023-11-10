diccionario = {}

while True:
    información = input("Escribe que tipo de información quieres introducir (nombre, edad, sexo, color) y escribe terminapara salir")
    respuesta = input("Escribe lo que quieres de aportar de información y escribe terminar para salir")

    if información + respuesta == "terminar":
        break 
    
    diccionario[información]= respuesta

    print(diccionario)
    





        
