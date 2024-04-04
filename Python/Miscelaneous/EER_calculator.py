import time

execute = True
clear_screen = '\n'*50
sep = '-='*15
table = '-'*10
idade = 0
idades = ['anos', 'meses']
altura = 0
peso = 0
age_type = None
sexo = None
cond = None
eer = 0

while execute:
    print(clear_screen, sep)
    print(f'\n\tValores:\n\n\t{table}\n\tPeso: {peso} kg\n\t{table}\n\tAltura: {altura} cm\n\t{table}\n\tIdade: {idade} {age_type}\n\t{table}\n\tSexo: {sexo}\n\t{table}\n\tCondição: {cond}\n\t{table}')
    print('\n\n\tEscolha uma opção')
    print('\n\t[0] Alterar valores\n\t[1] Calcular EER\n\n\t[ENTER] Sair\n\n')
    print(sep)
    opt = input('\n...')
    if opt == '':
        print(clear_screen)
        execute = False
    elif opt == '0':
        selection = True
        while selection:
            print(clear_screen, sep)
            print(f'\n\tValores:\n\n\t{table}\n\tPeso: {peso} kg\n\t{table}\n\tAltura: {altura} cm\n\t{table}\n\tIdade: {idade} {age_type}\n\t{table}\n\tSexo: {sexo}\n\t{table}\n\tCondição: {cond}\n\t{table}')
            print('\n\tEscolha alguma opção para alterar:\n\n\t[0] Peso\n\t[1] Altura\n\t[2] Idade\n\t[3] Tipo de idade\n\t[4] Sexo\n\t[5] Condição\n\n\t[ENTER] Sair\n\n')
            print(sep)
            choosen = input('...')
            if choosen == '':
                if age_type not in idades:
                    age_type = None
                    print(clear_screen, sep)
                    print('\nINSIRA UMA OPÇÃO VÁLIDA DE IDADE\n')
                    print(sep)
                    time.sleep(2)
                else:
                    selection = False
            elif choosen == '0':
                print(clear_screen, sep)
                peso = input(f'\tPeso: {peso}\n\n\tInsira um novo peso:\n{sep}\n...')
            elif choosen == '1':
                print(clear_screen, sep)
                altura = input(f'\tAltura: {altura}\n\n\tInsira uma nova altura:\n{sep}\n...')
            elif choosen == '2':
                print(clear_screen, sep)
                idade = input(f'\tIdade: {idade}\n\n\tInsira uma nova idade:\n{sep}\n...')
            elif choosen == '3':
                print(clear_screen, sep)
                age_type = input(f'\tTipo de idade: {age_type}\n\n\tInsira um novo tipo de idade (meses ou anos):\n{sep}\n...')
            elif choosen == '4':
                print(clear_screen, sep)
                sexo = input(f'\tSexo: {sexo}\n\n\tInsert a new sex (M or F):\n{sep}\n...')
            elif choosen == '5':
                print(clear_screen, sep)
                cond = input(f'\tCondição: {cond}\n\n\tInsira uma nova condição (s: sedentario, p: pouco ativo, a: ativo, m: muito ativo):\n{sep}\n...')
    elif opt == '1':
        if age_type == 'meses':
            if float(idade) < 2.99:
                if sexo == "M":
                    eer = -716.45-(1.00 * float(idade)) + (17.82 * float(altura)) + (15.06 * float(peso)) + 200
                elif sexo == 'F':
                    eer = -69.15-(80.00 * float(idade)) + (2.65 * float(altura)) + (56.15 * float(peso)) + 180
            elif float(idade) < 6:
                if sexo == "M":
                    eer = -716.45-(1.00 * float(idade)) + (17.82 * float(altura)) + (15.06 * float(peso)) + 50
                elif sexo == 'F':
                    eer = -69.15-(80.00 * float(idade)) + (2.65 * float(altura)) + (54.15 * float(peso)) + 60
            elif float(idade) > 36:
                if sexo == "M":
                    eer = -716.45-(1.00 * float(idade)) + (17.82 * float(altura)) + (15.06 * float(peso)) + 20
                elif sexo == 'F':
                    if float(idade) < 12:
                        eer = -69.15-(80.00 * float(idade)) + (2.65 * float(altura)) + (54.15 * float(peso)) + 20
                    if float(idade) >= 12:
                        eer = -69.15-(80.00 * float(idade)) + (2.65 * float(altura)) + (54.15 * float(peso)) + 15
        elif age_type == 'anos':
            if float(idade) < 19:
                if sexo == 'M':
                    if float(idade) > 3:
                        if cond == 's':
                            eer = -447.51 + (3.68 * float(idade)) + (13.01 * float(altura)) + (13.15 * float(peso)) + 20
                        elif cond == 'p':
                            eer = 19.12 + (3.68 * float(idade)) + (8.62 * float(altura)) + (20.28 * float(peso)) + 20
                        elif cond == 'a':
                            eer = -388.19 + (3.68 * float(idade)) + (12.66 * float(altura)) + (20.46 * float(peso)) + 20
                        elif cond == 'm':
                            eer = -671.75 + (3.68 * float(idade)) + (15.38 * float(altura)) + (23.25 * float(peso)) + 20
                    if float(idade) > 8:
                        if cond == 's':
                            eer = -447.51 + (3.68 * float(idade)) + (13.01 * float(altura)) + (13.15 * float(peso)) + 15
                        elif cond == 'p':
                            eer = 19.12 + (3.68 * float(idade)) + (8.62 * float(altura)) + (20.28 * float(peso)) + 15
                        elif cond == 'a':
                            eer = -388.19 + (3.68 * float(idade)) + (12.66 * float(altura)) + (20.46 * float(peso)) + 15
                        elif cond == 'm':
                            eer = -671.75 + (3.68 * float(idade)) + (15.38 * float(altura)) + (23.25 * float(peso)) + 15
                    if float(idade) > 13:
                        if cond == 's':
                            eer = -447.51 + (3.68 * float(idade)) + (13.01 * float(altura)) + (13.15 * float(peso)) + 25
                        elif cond == 'p':
                            eer = 19.12 + (3.68 * float(idade)) + (8.62 * float(altura)) + (20.28 * float(peso)) + 25
                        elif cond == 'a':
                            eer = -388.19 + (3.68 * float(idade)) + (12.66 * float(altura)) + (20.46 * float(peso)) + 25
                        elif cond == 'm':
                            eer = -671.75 + (3.68 * float(idade)) + (15.38 * float(altura)) + (23.25 * float(peso)) + 25
                    else:
                        if cond == 's':
                            eer = -447.51 + (3.68 * float(idade)) + (13.01 * float(altura)) + (13.15 * float(peso)) + 20
                        elif cond == 'p':
                            eer = 19.12 + (3.68 * float(idade)) + (8.62 * float(altura)) + (20.28 * float(peso)) + 20
                        elif cond == 'a':
                            eer = -388.19 + (3.68 * float(idade)) + (12.66 * float(altura)) + (20.46 * float(peso)) + 20
                        elif cond == 'm':
                            eer = -671.75 + (3.68 * float(idade)) + (15.38 * float(altura)) + (23.25 * float(peso)) + 20
                elif sexo == "F":
                    if float(idade) > 8:
                        if cond == 's':
                            eer = 55.59 - (22.25 * float(idade)) + (8.43 * float(altura)) + (17.07 * float(peso)) + 15
                        elif cond == 'p':
                            eer = -297.54 - (22.25 * float(idade)) + (12.77 * float(altura)) + (14.73 * float(peso)) + 15
                        elif cond == 'a':
                            eer = -189.55 - (22.25 * float(idade)) + (11.74 * float(altura)) + (18.34 * float(peso)) + 15
                        elif cond == 'm':
                            eer = -709.59 - (22.25 * float(idade)) + (18.22 * float(altura)) + (14.25 * float(peso)) + 15
                    elif float(idade) > 13:
                        if cond == 's':
                            eer = 55.59 - (22.25 * float(idade)) + (8.43 * float(altura)) + (17.07 * float(peso)) + 30
                        elif cond == 'p':
                            eer = -297.54 - (22.25 * float(idade)) + (12.77 * float(altura)) + (14.73 * float(peso)) + 30
                        elif cond == 'a':
                            eer = -189.55 - (22.25 * float(idade)) + (11.74 * float(altura)) + (18.34 * float(peso)) + 30
                        elif cond == 'm':
                            eer = -709.59 - (22.25 * float(idade)) + (18.22 * float(altura)) + (14.25 * float(peso)) + 30
                    else:
                        if cond == 's':
                            eer = 55.59 - (22.25 * float(idade)) + (8.43 * float(altura)) + (17.07 * float(peso)) + 20
                        elif cond == 'p':
                            eer = -297.54 - (22.25 * float(idade)) + (12.77 * float(altura)) + (14.73 * float(peso)) + 20
                        elif cond == 'a':
                            eer = -189.55 - (22.25 * float(idade)) + (11.74 * float(altura)) + (18.34 * float(peso)) + 20
                        elif cond == 'm':
                            eer = -709.59 - (22.25 * float(idade)) + (18.22 * float(altura)) + (14.25 * float(peso)) + 20
            elif float(idade) >= 19:
                if sexo == 'M':
                    if cond == 's':
                        eer =  753.07 - (10.83 * float(idade)) + (6.50 * float(altura)) + (14.10 * float(peso))
                    elif cond == 'p':
                        eer = 581.47 - (10.83 * float(idade)) + (8.30 * float(altura)) + (14.94 * float(peso))
                    elif cond == 'a':
                        eer = 1004.82 - (10.83 * float(idade)) + (6.52 * float(altura)) + (15.91 * float(peso))
                    elif cond == 'm':
                        eer = -517.88 - (10.83 * float(idade)) + (15.61 * float(altura)) + (19.11 * float(peso))
                elif sexo == "F":
                    if cond == 's':
                        eer = 584.90 - (7.01 * float(idade)) + (5.72 * float(altura)) + (11.71 * float(peso))
                    elif cond == 'p':
                        eer = 575.77 - (7.01 * float(idade)) + (6.60 * float(altura)) + (12.14 * float(peso))
                    elif cond == 'a':
                        eer = 710.25 - (7.01 * float(idade)) + (6.54 * float(altura)) + (12.34 * float(peso))
                    elif cond == 'm':
                        eer = 511.83 - (7.01 * float(idade)) + (9.07 * float(altura)) + (12.56 * float(peso))

        print(clear_screen, sep)
        print(f'\n\tSeu EER:\n\t{round(eer, 2)} kcal/dia\n')
        print(sep)
        option = input('\n\nAperte ENTER para voltar ao menu')
