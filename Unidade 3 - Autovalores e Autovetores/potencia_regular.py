import numpy as np

def potencia_regular(matriz, v0, e):
    lambda1_novo = 0
    vk_novo = v0
    erro = e + 1

    while erro > e:
        lambda1_velho = lambda1_novo
        vk_velho = vk_novo
        x1_velho = normalizar(vk_velho)
        vk_novo = matriz_x_vetor(matriz, x1_velho)

        lambda1_novo = vetor_x_vetor(x1_velho, vk_novo)

        erro = abs((lambda1_novo - lambda1_velho) / lambda1_novo)

    return lambda1_novo, x1_velho

def normalizar(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i] * vetor[i]
    length = soma ** (0.5)

    for i in range(len(vetor)):
        vetor[i] /= length
    
    return vetor

def matriz_x_vetor(matriz, vetor):
    vetor_resultado = [0 for i in range(len(vetor))]
    tamanho_vetor = len(vetor)

    for i in range(tamanho_vetor):
        for j in range(tamanho_vetor):
            vetor_resultado[i] += matriz[i][j] * vetor[j]

    return vetor_resultado

def vetor_x_vetor(vetor1, vetor2):
    escalar = 0
    tamanho = len(vetor1)

    for i in range(tamanho):
        escalar += vetor1[i] * vetor2[i]

    return escalar

def main():
    A1 = [[5, 2, 1], [2, 3, 1], [1, 1, 2]]
    v0 = normalizar(np.random.rand(3))
    e = 0.000001

    lambda1, x1 = potencia_regular(A1, v0, e)

    print(lambda1, x1)

    print("ok")

    print(matriz_x_vetor(A1, x1))
    

if __name__ == "__main__":
    main()