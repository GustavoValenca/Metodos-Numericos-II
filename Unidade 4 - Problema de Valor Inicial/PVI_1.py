from math import e

# Classe para representar o estado do PVI_3
class S:
    def __init__(self, i, t, y):
        self.i = i
        self.t = t
        self.y = y

class PVI:
    def __init__(self, i, t, y):
        # Estado inicial
        s = S(i, t, y)
        self.s_0 = s

    def F(self, s):
        d_y = (2/3) * s.y

        return d_y
    
    def EstadoExato(PVI, i, t):
        y = PVI.s_0.y * e ** ( (2 / 3) * (t - PVI.s_0.t))

        s_i = S(i, t, y)
        return s_i

