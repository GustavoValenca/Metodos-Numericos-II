import PVI_1
import PVI_3
import ForwardEuler as FE

def RungeKutta_3rd_PVI_1(PVI, s_i, delta_t, f):
    s_i_0_5 = FE.ForwardEuler_PVI_1(PVI, s_i, delta_t / 2, s_i.i)
    s_barra_f = FE.ForwardEuler_PVI_1(PVI, s_i, delta_t, s_i.i)

    s_i_d_y = PVI.F(s_i)
    s_i_0_5_d_y = PVI.F(s_i_0_5)
    s_barra_f_d_y = PVI.F(s_barra_f)

    # Calculando a posição do novo estado
    d_y = s_i.y + delta_t * ( (1/6) * s_i_d_y + (4/6) * s_i_0_5_d_y + (1/6) * s_barra_f_d_y) 

    s_f = PVI_1.S(f, s_i.t + delta_t, d_y)
    return s_f

def RungeKutta_3rd_PVI_3(PVI, s_i, delta_t, f):
    s_i_0_5 = FE.ForwardEuler_PVI_3(PVI, s_i, delta_t / 2, s_i.i)
    s_barra_f = FE.ForwardEuler_PVI_3(PVI, s_i, delta_t, s_i.i)
    
    s_i_d_v, s_i_d_y = PVI.F(s_i)
    s_i_0_5_d_v, s_i_0_5_d_y = PVI.F(s_i_0_5)
    s_barra_f_d_v, s_barra_f_d_y = PVI.F(s_barra_f)

    # Calculando a velocidade do novo estado
    d_v = s_i.v + delta_t * ( (1/6) * s_i_d_v + (4/6) * s_i_0_5_d_v + (1/6) * s_barra_f_d_v)

    # Calculando a posição do novo estado
    d_y = s_i.y + delta_t * ( (1/6) * s_i_d_y + (4/6) * s_i_0_5_d_y + (1/6) * s_barra_f_d_y)

    s_f = PVI_3.S(f, s_i.t + delta_t, d_v, d_y)
    return s_f

def RungeKutta_3rd_alternative_PVI_3(PVI, s_i, delta_t, f):
    f1_d_v, f1_d_y = PVI.F(s_i) 

    s_barra_i_0_5 = FE.ForwardEuler_PVI_3(PVI, s_i, delta_t / 2, s_i.i + 0.5)

    f2_d_v, f2_d_y = PVI.F(s_barra_i_0_5)

    # s barra f
    d_v_barra = s_i.v + delta_t * (-f1_d_v + 2 * f2_d_v)
    d_y_barra = s_i.y + delta_t * (-f1_d_y + 2 * f2_d_y)

    s_barra_f = PVI_3.S(f, s_i.t + delta_t, d_v_barra, d_y_barra)

    f3_d_v, f3_d_y = PVI.F(s_barra_f)

    d_v = s_i.v + delta_t * ( (1/6) * f1_d_v + (4/6) * f2_d_v + (1/6) * f3_d_v)

    d_y = s_i.y + delta_t * ( (1/6) * f1_d_y + (4/6) * f2_d_y + (1/6) * f3_d_y)

    s_f = PVI_3.S(f, s_i.t + delta_t, d_v, d_y)
    return s_f

def RungeKutta_4th_alternative_PVI_3(PVI, s_i, delta_t, f):
    f1_dv, f1_dy = PVI.F(s_i)

    s_2 = FE.ForwardEuler_PVI_3(PVI, s_i, delta_t / 2, 2)

    f2_dv, f2_dy = PVI.F(s_2)

    s_3 = FE.ForwardEuler_alternative_PVI_3(PVI, s_i, delta_t / 2, 3, f2_dv, f2_dy)

    f3_dv, f3_dy = PVI.F(s_3)

    s_4 = FE.ForwardEuler_alternative_PVI_3(PVI, s_i, delta_t, f, f3_dv, f3_dy)

    f4_dv, f4_dy = PVI.F(s_4)

    dv_f = s_i.v + (delta_t / 6) * (f1_dv + 2 * f2_dv + 2 * f3_dv + f4_dv)
    dy_f = s_i.y + (delta_t / 6) * (f1_dy + 2 * f2_dy + 2 * f3_dy + f4_dy)

    s_f = PVI_3.S(f, s_i.t + delta_t, dv_f, dy_f)
    return s_f