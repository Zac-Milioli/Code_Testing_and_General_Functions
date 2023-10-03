# Atividade feita para um amigo, não lembro o que faz

cifra = ''
tab = ['a', 'b', 'c']
p = '00.0'
for i in p:
    if i.isnumeric():
        cifra += tab[int(i)]
    else:
        cifra += i

print(cifra)
