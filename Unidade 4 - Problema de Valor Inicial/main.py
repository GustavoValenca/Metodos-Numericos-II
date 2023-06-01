import PVI_2
import ForwardEuler as FE

def main():
    problema = PVI_2.PVI()

    s_1 = FE.ForwardEuler_PVI_2(problema, problema.s_0, 0.1, 1)
    print(s_1.v)
    print(s_1.y)

    s_2 = FE.ForwardEuler_PVI_2(problema, s_1, 0.1, 2)
    print(s_2.v)
    print(s_2.y)

    s_i = s_2
    for j in range(3, 164):
        s_j = FE.ForwardEuler_PVI_2(problema, s_i, 0.1, j)
        s_i = s_j
    
    print(s_j.v)
    print(s_j.y)


if __name__ == '__main__':
    main()