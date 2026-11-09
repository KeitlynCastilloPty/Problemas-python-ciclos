opcion = ""

while opcion != "salir": 
    opcion = input("Escribe 'holi' o 'salir': ")
    if opcion == "holi":
        print("¡Holi, mucho gusto!")
    elif opcion != "salir":
        print("Opción no válida")

print("Hasta luego")