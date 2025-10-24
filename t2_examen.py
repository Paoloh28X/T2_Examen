import random

# Función para generar una palabra de 4 letras al azar (minúsculas)
def palabra_al_azar():
    palabra = ""
    for i in range(4):
        palabra += chr(random.randint(97, 122))  
    return palabra

# Función para generar la matriz
def generar_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(palabra_al_azar())
        matriz.append(fila)
    return matriz

# divide y vencerás para contar palabras con vocales
def contar_vocal_matriz(matriz):
    n = len(matriz)
    
   # matriz 1x1
    if n == 1:
        palabra = matriz[0][0]
        for letra in palabra:
            if letra in "aeiou":
                return 1
        return 0

    # Dividir la matriz en 4 submatrices
    mitad = n // 2
    parte1 = [fila[:mitad] for fila in matriz[:mitad]]
    parte2 = [fila[mitad:] for fila in matriz[:mitad]]
    parte3 = [fila[:mitad] for fila in matriz[mitad:]]
    parte4 = [fila[mitad:] for fila in matriz[mitad:]]

    # Combinar resultados (divide y vencerás)
    return (contar_vocal_matriz(parte1) +
            contar_vocal_matriz(parte2) +
            contar_vocal_matriz(parte3) +
            contar_vocal_matriz(parte4))


n = int(input("Ingresar tamaño de la mAtriz cuadrada:\n"))
matriz = generar_matriz(n)

print("\nMatriz generada:")
for fila in matriz:
    print(fila)

total_vocales = contar_vocal_matriz(matriz)

print(f"\nCantidad de palabras con una vocal: {total_vocales}")
