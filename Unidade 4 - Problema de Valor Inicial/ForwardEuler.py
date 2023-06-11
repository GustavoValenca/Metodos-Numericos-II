import PVI_1
import PVI_3

def ForwardEuler_PVI_1(PVI, s_i, delta_t, f):
    s_i_d_y = PVI.F(s_i)

    # Calculando a posição do novo estado
    d_y = s_i.y + delta_t * s_i_d_y

    s_f = PVI_1.S(f, s_i.t + delta_t, d_y)
    return s_f

def ForwardEuler_PVI_3(PVI, s_i, delta_t, f):
    s_i_d_v, s_i_d_y = PVI.F(s_i)

    # Calculando a velocidade do novo estado
    d_v = s_i.v + delta_t * s_i_d_v

    # Calculando a posição do novo estado
    d_y = s_i.y + delta_t * s_i_d_y

    s_f = PVI_3.S(f, s_i.t + delta_t, d_v, d_y)
    return s_f

def ForwardEuler_alternative_PVI_3(PVI, s_i, delta_t, f, s_dv, s_dy):
    dv = s_i.v + delta_t * s_dv
    dy = s_i.y + delta_t * s_dy

    s_f = PVI_3.S(f, s_i.t + delta_t, dv, dy)
    return s_f
