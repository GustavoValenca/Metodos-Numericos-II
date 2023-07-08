import numpy as np
import math

n = int(input("N: "))
# print(n)
deltax = 1 / n

pontos = []

for i in range(1, n):
    pontos.append(0 + i * deltax)

# print(pontos)

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

# print(matriz)
# print(b)
    
A = np.array(matriz)
y = np.array(b)
x = np.linalg.solve(A, y)
# print(x)

def solucao_exata(x):
    result = ((math.e ** (-x)) - (math.e ** x)) / ((math.e ** -1)  -math.e)
    return result 

pdf_4 = [0.21511475, 0.44367418, 0.69996324]

print("|   x   |  Valor Obtido  |  Valor Exato  | Valor Obtido com N=4 |    Erro    |")
print("------------------------------------------------------------------------------")
for i in range(0, len(pontos)):
    print(f"| {pontos[i]:.3f} |   {x[i]:.8f}   |   {solucao_exata(pontos[i]):.8f}  |", end='')
    if (pontos[i] == 0.25):
        print(f"{pdf_4[0]:^22}|", end='')
    elif (pontos[i] == 0.5):
        print(f"{pdf_4[1]:^22}|", end='')
    elif (pontos[i] == 0.75):
        print(f"{pdf_4[2]:^22}|", end='')   
    else:
        print(" " * 22 + "|", end='')
    erro = (x[i] - solucao_exata(pontos[i])) / solucao_exata(pontos[i])
    print(f"{erro:^12.6f}|")

