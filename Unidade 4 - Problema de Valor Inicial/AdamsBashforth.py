import PVI_3

def AdamsBashforth_4th_PVI_3(PVI, s_i, s_neg1, s_neg2, s_neg3, delta_t, f):
    # Fase de predição
    dv_i, dy_i = PVI.F(s_i)
    dv_neg1, dy_neg1 = PVI.F(s_neg1)
    dv_neg2, dy_neg2 = PVI.F(s_neg2)
    dv_neg3, dy_neg3 = PVI.F(s_neg3)

    dv_f = s_i.v + (delta_t / 24) * (55 * dv_i - 59 * dv_neg1 + 37 * dv_neg2 - 9 * dv_neg3)
    dy_f = s_i.y + (delta_t / 24) * (55 * dy_i - 59 * dy_neg1 + 37 * dy_neg2 - 9 * dy_neg3)

    s_barra_f = PVI_3.S(f, s_i.t + delta_t, dv_f, dy_f)
    dv_barra_f, dy_barra_f = PVI.F(s_barra_f)

    # Fase de correção 

    dv_f = s_i.v + (delta_t / 24) * (9 * dv_barra_f + 19 * dv_i - 5 * dv_neg1 + dv_neg2)
    dy_f = s_i.y + (delta_t / 24) * (9 * dy_barra_f + 19 * dy_i - 5 * dy_neg1 + dy_neg2)

    s_f = PVI_3.S(f, s_i.t + delta_t, dv_f, dy_f)
    return s_f