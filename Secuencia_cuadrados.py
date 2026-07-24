#programa para obtener el cuadrado de un numero
N = int(input("Número positivo: "))
i = 1
while True:
    print(i ** 2)
    i += 1
    if i > N:
        break
print("Secuencia de cuadrados hasta", N) 