palabra = input("Ingresa tu palabrita: ")
vocales = 0

for letra in palabra:
    if letra in "aeiou":
        vocales += 1

print("Tiene",vocales , "vocales")





