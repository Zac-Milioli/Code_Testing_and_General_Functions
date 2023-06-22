# MRU   x = x0 + v*t
# MUV   x = v0 + a*t
# Torricelli v² = v0² + 2*a*Deltax
# Energia Pot   Ep = m*g*h
# Energia Cin   Ec = (m*v²)/2
# Energia Mec   Et = Ec + Ep
#
# -> Menu de opções
# -> Quando selecionada, pedir as variáveis
# -> Mostrar resultado
import math

def mru(x0, v, t):
    x = x0 + (v*t)
    return x

def muv(v0, a, t):
    x = v0 + (a*t)
    return x

def torricelli(v0, a, delta_x):
    v = math.sqrt(v0^2 + (2*a*delta_x))
    return v

def energia_potencial(m, g, h):
    e = m*g*h
    return e

def energia_cinetica(m, v):
    e = (m*v^2)/2
    return e

def energia_mecanica(m, g, h, v):
    e = energia_potencial(m, g, h) + energia_cinetica(m, v)
    return e
