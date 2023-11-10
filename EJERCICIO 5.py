diccionario = {}

entrada = input("Introduce las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, escribe <terminar> para finalizar con el diccionario")
entrada = entrada.split(',')

print("")  #(entrada)

for i in range(len(entrada)):
    if entrada[i] != 'terminar':
        
        print("")  #(entrada[i].split(':'))
        
        clave,  valor = entrada[i].split(':')
        diccionario[clave] = valor

print("")    #(diccionario)

pregunta = input("Escribe una frase en español")
palabras = pregunta.split(" ")

for i in palabras:
    if i in diccionario:
        print(diccionario[i], end=" ")
    else:
        print("sin traducir", end=" ")
