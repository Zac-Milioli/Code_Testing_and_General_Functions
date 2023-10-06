# Feita em atividade, não lembro o que faz

n = int(input())
cima = 1
baixo = 1
serie = 0
for i in range(0, n):
    serie += cima / baixo
    baixo += 1
    cima = -1 * cima

print(f'{serie:.5f}')
