while True:
    letra = input("Ingrese letra (espacio termina): ")
    letra = letra.lower()
    if letra in "aeiou":
        print("Vocal")
    else:
        print("Consonante")
    if letra == " ":
            break
print("Programa finalizado")