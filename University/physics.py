# Código para selecionar uma fórmula física, passar os valores e retornar o resultado

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
    e = (m*(v^2))/2
    return e

def energia_mecanica(m, g, h, v):
    e = energia_potencial(m, g, h) + energia_cinetica(m, v)
    return e

def menu(execute):
    opt = int(input(interface))
    if opt == 1:
        x0 = float(input('\nInsira a posição inicial: '))
        v = float(input('\nInsira a velocidade: '))
        t = float(input('\nInsira o a variação do tempo: '))
        result = mru(x0, v, t)
    elif opt == 2:
        v0 = float(input('\nInsira a velocidade inicial: '))
        a = float(input('\nInsira a aceleração: '))
        t = float(input('\nInsira a variação do tempo: '))
        result = muv(v0, a, t)
    elif opt == 3:
        v0 = float(input('\nInsira a velocidade inicial: '))
        a = float(input('\nInsira a aceleração: '))
        delta_x = float(input('\nInsira a variação da posição: '))
        result = torricelli(v0, a, delta_x)
    elif opt == 4:
        m = float(input('\nInsira a massa: '))
        g = float(input('\nInsira um valor para a gravidade: '))
        h = float(input('\nInsira a altura: '))
        result = energia_potencial(m, g, h)
    elif opt == 5:
        m = float(input('\nInsira a massa'))
        v = float(input('\nInsira a velocidade'))
        result = energia_cinetica(m, v)
    elif opt == 6:
        m = float(input('\nInsira a massa: '))
        g = float(input('\nInsira um valor para a gravidade: '))
        h = float(input('\nInsira a altura: '))
        v = float(input('\nInsira a velocidade'))
        result = energia_mecanica(m, g, h, v)
    else:
        execute = False
        return '\nObrigado por usar o programa de cálculos físicos automáticos!'
    return f'\n-> {result}'

interface = '''\nBem vindo ao programa de cálculos físicos automáticos!
Escolha uma opção de fórmula:
    [1] Movimento Retilíneo Uniforme
    [2] Movimento Uniformemente Variado
    [3] Torriceli
    [4] Energia Potencial
    [5] Energia Cinética
    [6] Energia Mecânica Total
    [ENTER] Encerrar o programa\n\n...'''
execute = True
while execute:
    print(menu(execute))
