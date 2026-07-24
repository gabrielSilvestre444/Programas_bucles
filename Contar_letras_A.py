palabra = input("Ingrese una palabra: ").upper()
contador = 0
for letra in palabra:
    if letra == 'A':
        contador += 1
print("La letra 'a' aparece", contador, "veces")
