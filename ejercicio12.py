numerosecreto = 7
intento= int(input("Di un número del (1 al 10): "))

while intento != numerosecreto:
    if intento < numerosecreto:
        print("no pequeño saltamontes, esta muy bajo ese número eh")
    else: 
        print("Ese número esta muy alto chavalin")
    intento = int(input("Intenta de nuevo: "))

print("¡Omg acertaste!, eres un(a) crack en esto de adivinar números")