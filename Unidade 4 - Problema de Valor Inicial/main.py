import PVI_1
import PVI_3
import ForwardEuler as FE
import RungeKutta as RK

def main():
    # PVI-3

    pvi3 = PVI_3.PVI(0.5, 0.5, 10, 0, 0, 3, 150)
    # s_i_exato = pvi3.EstadoExato(0, 16.3)
    # print(s_i_exato.v)
    # print(s_i_exato.y)

    ## Forward Euler 

    # s_1 = FE.ForwardEuler_PVI_3(pvi3, pvi3.s_0, 0.1, 1)
    # print(s_1.v)
    # print(s_1.y)

    # s_2 = FE.ForwardEuler_PVI_3(pvi3, s_1, 0.1, 2)
    # print(s_2.v)
    # print(s_2.y)

    # s_i = s_2
    # for j in range(3, 164):
    #     s_j = FE.ForwardEuler_PVI_3(pvi3, s_i, 0.1, j)
    #     s_i = s_j
    
    # print(s_j.v)
    # print(s_j.y)

    ## Runge-Kutta

    # s_1 = RK.RungeKutta_3rd_PVI_3(pvi3, pvi3.s_0, 0.1, 1)

    # print(s_1.v)
    # print(s_1.y)

    # s_i = pvi3.s_0
    # for j in range(163):
    #     s_j = RK.RungeKutta_3rd_PVI_3(pvi3, s_i, 0.1, j)
    #     s_i = s_j

    # print(s_j.v)
    # print(s_j.y)
    # print(s_j.t)

    # PVI-1

    pvi1 = PVI_1.PVI(0, 0, 2)

    ## Teste Forward Euler
    # s_1 = FE.ForwardEuler_PVI_1(pvi1, pvi1.s_0, 0.5, 1)
    # print(s_1.y)

    ## Teste Runge Kutta
    # s_1 = RK.RungeKutta_3rd_PVI_1(pvi1, pvi1.s_0, 0.5, 1)
    # print(s_1.y)

    # Aproximação para tf = 10s usando Runge Kutta
    # s_i = pvi1.s_0
    # for j in range(1000):
    #     s_j = RK.RungeKutta_3rd_PVI_1(pvi1, s_i, 0.01, j)
    #     s_i = s_j

    # print(s_j.y)

    # Tarefa
    pvi3_tarefa = PVI_3.PVI(0.25, 2, 10, 0, 0, 5, 200)

    # print("== Valores Exatos ==")
    # print("Altura máxima da trajetória: 200.4389m")
    # print("Tempo decorrido do início do lançamento até atingir a altura máxima: 0.29s")
    # print("Tempo total até a queda no mar: 7.58s")
    # print("Velocidade no momento do impacto com o mar: -47.82m/s")
    # print()
    
    print("== Valores aproximados ==")

    ## Aproximando altura máxima:
    print("- Altura máxima da trajetória e tempo decorrido -")
    ### Delta t = 0.1
    h = 200
    count = 0
    s_i = pvi3_tarefa.s_0
    while (s_i.y - h >= 0):
        count += 1
        s_count = RK.RungeKutta_3rd_alternative_PVI_3(pvi3_tarefa, s_i, 0.1, count)
        h = s_i.y
        s_i = s_count
    print("delta t = 0.1:")
    print("{}m".format(s_i.y))
    print("{}s".format(s_i.t))
    print()

    ### Delta t = 0.01
    h = 200
    count = 0
    s_i = pvi3_tarefa.s_0
    while (s_i.y - h >= 0):
        count += 1
        s_count = RK.RungeKutta_3rd_alternative_PVI_3(pvi3_tarefa, s_i, 0.01, count)
        h = s_i.y
        s_i = s_count
    print("delta t = 0.01:")
    print("{}m".format(s_i.y))
    print("{}s".format(s_i.t))
    print()

    ### Delta t = 0.001
    h = 200
    count = 0
    s_i = pvi3_tarefa.s_0
    while (s_i.y - h >= 0):
        count += 1
        s_count = RK.RungeKutta_3rd_alternative_PVI_3(pvi3_tarefa, s_i, 0.001, count)
        h = s_i.y
        s_i = s_count
    print("delta t = 0.001:")
    print("{}m".format(s_i.y))
    print("{}s".format(s_i.t))
    print()

    ### Delta t = 0.0001
    h = 200
    count = 0
    s_i = pvi3_tarefa.s_0
    while (s_i.y - h >= 0):
        count += 1
        s_count = RK.RungeKutta_3rd_alternative_PVI_3(pvi3_tarefa, s_i, 0.0001, count)
        h = s_i.y
        s_i = s_count
    print("delta t = 0.0001:")
    print("{}m".format(s_i.y))
    print("{}s".format(s_i.t))
    print()
    print("-> Altura máxima aproximada: 201.2m")
    print("-> Tempo decorrido aproximado: 0.485s")
    print()

    ## Aproximando queda no mar
    print("- Tempo e velocidade até a queda no mar -")
    ### Delta t = 0.1
    count = 0
    s_i = pvi3_tarefa.s_0
    while (s_i.y > 0):
        count += 1
        s_count = RK.RungeKutta_3rd_alternative_PVI_3(pvi3_tarefa, s_i, 0.1, count)
        s_i = s_count
    print("delta t = 0.1:")
    print("{}s".format(s_i.t))
    print("{}m/s".format(s_i.v))
    print()

    ### Delta t = 0.01
    count = 0
    s_i = pvi3_tarefa.s_0
    while (s_i.y > 0):
        count += 1
        s_count = RK.RungeKutta_3rd_alternative_PVI_3(pvi3_tarefa, s_i, 0.01, count)
        s_i = s_count
    print("delta t = 0.01:")
    print("{}s".format(s_i.t))
    print("{}m/s".format(s_i.v))
    print()

    ### Delta t = 0.001
    count = 0
    s_i = pvi3_tarefa.s_0
    while (s_i.y > 0):
        count += 1
        s_count = RK.RungeKutta_3rd_alternative_PVI_3(pvi3_tarefa, s_i, 0.001, count)
        s_i = s_count
    print("delta t = 0.001:")
    print("{}s".format(s_i.t))
    print("{}m/s".format(s_i.v))
    print()

    ### Delta t = 0.0001
    count = 0
    s_i = pvi3_tarefa.s_0
    while (s_i.y > 0):
        count += 1
        s_count = RK.RungeKutta_3rd_alternative_PVI_3(pvi3_tarefa, s_i, 0.0001, count)
        s_i = s_count
    print("delta t = 0.0001:")
    print("{}s".format(s_i.t))
    print("{}m/s".format(s_i.v))
    print()

    print("-> Tempo aproximado até a queda no mar: 7.79s")
    print("-> Velocidade aproximada no momento do impacto: -47.89m/s")    

if __name__ == '__main__':
    main()