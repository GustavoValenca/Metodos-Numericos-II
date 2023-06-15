import numpy as np

n = int(input("N: "))
print(n)
deltax = 1 / n

pontos = []

for i in range(1, n):
    pontos.append(0 + i * deltax)

celula_esquerda = 1 / (deltax **2)
celula_direita = 1 / (deltax ** 2)
celula_central = -(2 / (deltax ** 2) + 1)

matriz = []
b = []

for i in range(1, n):
    bsum = 0

    linha = []
    for j in range(n - 1):
        linha.append(0)
    len(linha)

    if i == 1:
        bsum += celula_esquerda * 0
        linha[i - 1] = celula_central
        linha[i] = celula_direita

    elif i == n - 1:
        bsum += - (celula_direita * 1)
        linha[i - 2] = celula_esquerda        
        linha[i - 1] = celula_central
    else:
        linha[i - 2] = celula_esquerda
        linha[i - 1] = celula_central
        linha[i] = celula_direita

    matriz.append(linha)
    b.append(bsum)

print(matriz)
print(b)
    
A = np.array(matriz)
y = np.array(b)
x = np.linalg.solve(A, y)
print(x)