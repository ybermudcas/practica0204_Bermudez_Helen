lista = []

while True:
    print("\nMenú:")
    print("1. Añadir alumno")
    print("2. Eliminar alumno")
    print("3. Mostrar alumno")
    print("4. Listado de todo el alumnado")
    print("5. Listado alumnado aprobado")
    print("6. Terminar")
    
    opción = input("Seleccione una opción del 1 al 6")
    if opción == '1':
        nif = input("Introduce el NIF del alumno")
        nombre = input("Introduce el nombre del alumno")
        apellidos = input("Introduce los apellidos del alumno")
        móvil = input("Introduce el móvil del alumno")
        email = input("Introduce el correo del alumno")
        aprobado = input("¿Ha aprobado el módulo? (True/False)").lower() == 'true'

        diccionario = {"NIF": nif, "Nombre": nombre, "Apellidos": apellidos, "Móvil": móvil, "Email": email, "Aprobado": aprobado}

        diccionario.append(lista)
        print("Alumno añadido")

