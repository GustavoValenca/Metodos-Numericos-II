import PVI_2

def ForwardEuler_PVI_2(PVI, s_i, delta_t, f):
    s_i_d_v, s_i_d_y = PVI.F(s_i)
    d_v = s_i.v + delta_t * s_i_d_v
    d_y = s_i.y + delta_t * s_i_d_y
    s_f = PVI_2.S(f, s_i.t + f, d_v, d_y)
    return s_f