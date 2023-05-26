def IPclass(ip):
    ip = ip.split('.')
    ip = ip[0]
    ip = int(ip)
    if 0 <= ip <= 127:
        return 'A'
    if 127 < ip <= 191:
        return 'B'
    if 191 < ip <= 255:
        return 'C'
    else:
        return 'ERRO'


endereco = input()
print(IPclass(endereco))
