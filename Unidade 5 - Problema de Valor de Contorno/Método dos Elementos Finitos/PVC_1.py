import numpy as np
import math

n = int(input("N: "))
deltax = 1 / n

pontos = []

for i in range(1, n):
    pontos.append(0 + i * deltax)

# Condições:
# y(0) = 0
# y(1) = 1

Li = deltax
N1_in = -1/2
N1_fin = 1/2

Ki = []

for i in range(2):
    linha = [0, 0]
    Ki.append(linha)

Ki[0][0] = (N1_in * (2 / Li) * N1_in * (2 / Li) * (Li / 2)) * 2 + ( (8 / 3) * (Li / 8))
Ki[0][1] = (N1_in * (2 / Li) * N1_fin * (2 / Li) * (Li / 2)) * 2 + ( (4 / 3) * (Li / 8))
Ki[1][0] = (N1_fin * (2 / Li) * N1_in * (2 / Li) * (Li / 2)) * 2 + ( (4 / 3) * (Li / 8))
Ki[1][1] = (N1_fin * (2 / Li) * N1_fin * (2 / Li) * (Li / 2)) * 2 + ( (8 / 3) * (Li / 8))

# print(Ki)

# print("Matriz:")
K = []
for i in range(0, n-1):
    linha = []
    for j in range(0, n-1):
        linha.append(0)
    K.append(linha)

for i in range(0, n-2):
    for j in range(0, n-2):
        if i == j:
            K[i][i] += Ki[0][0]
            K[i][i + 1] += Ki[0][1]
            K[i + 1][i] += Ki[1][0]
            K[i + 1][i + 1] += Ki[1][1]
K[0][0] += Ki[1][1]
K[n-2][n-2] += Ki[0][0]

# for i in range(n-2):
    # print(K[i])


b = []

for i in range(0, n - 1):
    b.append(0)

    if (i == n - 2):
        b[i] = Ki[0][1] * (-1)

# print(b)

# print("FIM:")
A = np.array(K)
y = np.array(b)
x = np.linalg.solve(A, y)
# print(x)


def solucao_exata(x):
    result = ((math.e ** (-x)) - (math.e ** x)) / ((math.e ** -1)  -math.e)
    return result 

pdf_4 = [0.21511475, 0.44367418, 0.69996324]
elementos_finitos_4 = [0.214788, 0.443141, 0.699481]

print(f"|   x   | Elementos Finitos (N={n}) |  Valor Exato  | Diferenças Finitas (N=4) | Elementos Finitos (N=4) |    Erro    |")
print("-" * 117)
for i in range(0, len(pontos)):
    print(f"| {pontos[i]:.3f} |   {x[i]:.17f}   |   {solucao_exata(pontos[i]):.8f}  |", end='')
    if (pontos[i] == 0.25):
        print(f"{pdf_4[0]:^26}|", end='')
        print(f"{elementos_finitos_4[0]:^25}|", end='')
    elif (pontos[i] == 0.5):
        print(f"{pdf_4[1]:^26}|", end='')
        print(f"{elementos_finitos_4[1]:^25}|", end='')
    elif (pontos[i] == 0.75):
        print(f"{pdf_4[2]:^26}|", end='')   
        print(f"{elementos_finitos_4[2]:^25}|", end='')
    else:
        print(" " * 26 + "|", end='')
        print(" " * 25 + "|", end='')
    erro = (x[i] - solucao_exata(pontos[i])) / solucao_exata(pontos[i])
    print(f"{erro:^12.6f}|")
