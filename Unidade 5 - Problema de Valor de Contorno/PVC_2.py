import numpy as np

n = int(input("N: "))
fxy = int(input("f(x, y): "))
print(n)
print(fxy)
delta = 1 / n

pontos = []

for x in range(1, n):
    for y in range(1, n):
        pontos.append((x, y))

print(pontos)

borda_inferior = 0
borda_superior = 0
borda_esquerda = 0
borda_direita = 0

celula_esquerda = 1 / (delta ** 2)
celula_direita = 1 / (delta ** 2)
celula_inferior = 1 / (delta ** 2)
celula_superior = 1 / (delta ** 2)
celula_central = - 2 * ( 1 / (delta ** 2) + 1 / (delta ** 2) )

print(celula_esquerda)
print(celula_direita)
print(celula_inferior)
print(celula_superior)
print(celula_central)

matriz = []
tamanho = (n - 1) ** 2
b = []

for i in range(tamanho):
    linha = []

for y in range(1, n):
    for x in range(1, n):
        linha = [] 
        bsum = fxy

        for i in range(tamanho):
            linha.append(0)

        central = (y - 1) * (n - 1) + x
        left = central - 1
        right = central + 1
        top = y * (n - 1) + x
        down = (y - 2) * (n - 1) + x

        if x == 1 and y == 1:
            bsum -= celula_esquerda * borda_esquerda   
            bsum -= celula_inferior * borda_inferior   

            linha[central - 1] = celula_central
            linha[right - 1] = celula_direita
            linha[top - 1] = celula_superior

        elif x == 1 and y == n - 1:
            bsum -= celula_esquerda * borda_esquerda
            bsum -= celula_superior * borda_superior

            linha[central - 1] = celula_central
            linha[down - 1] = celula_inferior
            linha[right - 1] = celula_direita
        elif x == n - 1 and y == 1:
            bsum -= celula_inferior * borda_inferior
            bsum -= celula_direita * borda_direita

            linha[central - 1] = celula_central
            linha[left - 1] = celula_esquerda
            linha[top - 1] = celula_superior
        elif x == n - 1 and y == n - 1:
            bsum -= celula_superior * borda_superior
            bsum -= celula_direita * borda_direita

            linha[central - 1] = celula_central
            linha[left - 1] = celula_esquerda
            linha[down - 1] = celula_inferior
        elif x == 1:
            

            bsum -= celula_esquerda * borda_esquerda

            linha[central - 1] = celula_central
            linha[right - 1] = celula_direita
            linha[top - 1] = celula_superior
            linha[down - 1] = celula_inferior
        elif x == n - 1:
            bsum -= celula_direita * borda_direita

            linha[central - 1] = celula_central
            linha[left - 1] = celula_esquerda
            linha[top - 1] = celula_superior
            linha[down - 1] = celula_inferior


            
        elif y == 1:
            bsum -= celula_inferior * borda_inferior

            linha[central - 1] = celula_central
            linha[left - 1] = celula_esquerda
            linha[right - 1] = celula_direita
            linha[top - 1] = celula_superior
        elif y == n - 1:
            bsum -= celula_superior * borda_superior

            linha[central - 1] = celula_central
            linha[left - 1] = celula_esquerda
            linha[right - 1] = celula_direita
            linha[down - 1] = celula_inferior
        else:

            linha[central - 1] = celula_central
            linha[left - 1] = celula_esquerda
            linha[right - 1] = celula_direita
            linha[top - 1] = celula_superior
            linha[down - 1] = celula_inferior

        matriz.append(linha)
        b.append(bsum)

        
A = np.array(matriz)
y = np.array(b)
x = np.linalg.solve(A, y)
print(x)
    