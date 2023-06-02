from math import e

# Classe para representar o estado do PVI_2
class S:
    def __init__(self, i, t, v, y):
        self.i = i
        self.t = t
        self.v = v
        self.y = y

class PVI:
    def __init__(self, k, m, g, i, t, v, y):
        self.k = k
        self.m = m
        self.g = g

        # Estado inicial
        s = S(i, t, v, y)
        self.s_0 = s

    def F(self, s):
        d_v = -self.g - (self.k / self.m) * s.v
        d_y = s.v

        return d_v, d_y
    
    def EstadoExato(self, i, t):
        v = -self.g * (self.m / self.k) + (3 + self.g * (self.m / self.k)) * (e ** (-1 * (self.k / self.m) * t)) 

        y = self.s_0.y - self.g * (self.m / self.k) * t - (3 + self.g * (self.m / self.k)) * (self.m / self.k) * (e ** (-1 * (self.k / self.m) * t) -1)
        
        s_i = S(i, t, v, y)

        return s_i

