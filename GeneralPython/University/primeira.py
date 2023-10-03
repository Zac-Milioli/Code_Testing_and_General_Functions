# Isto era é a primeira questão de uma atividade de programação que fiz para um amigo, mas não tenho ideia do que faz esse código agora

def minhaCifra(p, c):
    cifra = ''
    tab = []
    for i in c:
        tab.append(i)
    p = str(p)
    for i in p:
        if i.isnumeric():
            cifra += tab[int(i)]
        else:
            cifra += i
    return cifra


chave = input()
preco = input()
print(minhaCifra(preco, chave))
