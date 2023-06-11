import PVI_3
import RungeKutta as RK
import AdamsBashforth as AB

def main():
    pvi3tarefa = PVI_3.PVI(0.25, 2, 10, 0, 0, 5, 200)

    # Aproximando altura máxima:
    print("- Altura máxima da trajetória e tempo decorrido -")

    ABheight(pvi3tarefa, 0.1)
    ABheight(pvi3tarefa, 0.01)
    ABheight(pvi3tarefa, 0.001)
    ABheight(pvi3tarefa, 0.0001)
    
    print("-> Altura máxima aproximada: 201.2m")
    print("-> Tempo decorrido aproximado: 0.485s")
    print()

    # Aroximando queda no mar
    print("- Tempo e velocidade até a queda no mar -")

    ABSea(pvi3tarefa, 0.1)
    ABSea(pvi3tarefa, 0.01)
    ABSea(pvi3tarefa, 0.001)
    ABSea(pvi3tarefa, 0.0001)

    print("-> Tempo aproximado até a queda no mar: 7.79s")
    print("-> Velocidade aproximada no momento do impacto: -47.89m/s")
    print()    

def ABheight(PVI, delta_t):
    # Fase de Inicialização
    s_0 = PVI.s_0
    s_1 = RK.RungeKutta_4th_alternative_PVI_3(PVI, s_0, delta_t, 1)
    s_2 = RK.RungeKutta_4th_alternative_PVI_3(PVI, s_1, delta_t, 2)
    s_3 = RK.RungeKutta_4th_alternative_PVI_3(PVI, s_2, delta_t, 3)
    s_4 = AB.AdamsBashforth_4th_PVI_3(PVI, s_3, s_2, s_1, s_0, delta_t, 4)

    # Aproximando

    h = 200
    count = 3
    s_i = s_3
    s_neg1 = s_2
    s_neg2 = s_1
    s_neg3 = s_0
    while (s_i.y - h >= 0):
        count += 1
        s_count = AB.AdamsBashforth_4th_PVI_3(PVI, s_i, s_neg1, s_neg2, s_neg3, delta_t, count)
        
        h = s_i.y

        s_neg3 = s_neg2
        s_neg2 = s_neg1
        s_neg1 = s_i
        s_i = s_count
    
    print(f"delta t = {delta_t}:")
    print("{}m".format(s_i.y))
    print("{}s".format(s_i.t))
    print()

def ABSea(PVI, delta_t):
    ### Fase de Inicialização
    s_0 = PVI.s_0
    s_1 = RK.RungeKutta_4th_alternative_PVI_3(PVI, s_0, delta_t, 1)
    s_2 = RK.RungeKutta_4th_alternative_PVI_3(PVI, s_1, delta_t, 2)
    s_3 = RK.RungeKutta_4th_alternative_PVI_3(PVI, s_2, delta_t, 3)
    s_4 = AB.AdamsBashforth_4th_PVI_3(PVI, s_3, s_2, s_1, s_0, delta_t, 4)

    # Aproximando

    count = 3
    s_i = s_3
    s_neg1 = s_2
    s_neg2 = s_1
    s_neg3 = s_0
    while (s_i.y > 0):
        count += 1
        s_count = AB.AdamsBashforth_4th_PVI_3(PVI, s_i, s_neg1, s_neg2, s_neg3, delta_t, count)
        
        s_neg3 = s_neg2
        s_neg2 = s_neg1
        s_neg1 = s_i
        s_i = s_count

    print(f"delta t = {delta_t}:")
    print("{}s".format(s_i.t))
    print("{}m/s".format(s_i.v))
    print()

if __name__ == '__main__':
    main()