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
