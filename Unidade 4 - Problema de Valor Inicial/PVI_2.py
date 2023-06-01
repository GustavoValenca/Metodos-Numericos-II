# Classe para representar o estado do PVI_2
class S:
    def __init__(self, i, t, v, y):
        self.i = i
        self.t = t
        self.v = v
        self.y = y

class PVI:
    k = 0.5
    m = 0.5
    g = 10

    # Estado inicial
    s_0 = S(0, 0, 3, 150)

    def F(self, s):
        d_v = -self.g - (self.k / self.m) * s.v
        d_y = s.v

        return d_v, d_y

