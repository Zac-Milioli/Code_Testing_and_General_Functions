import os

codigos = []
open('programa.py', 'w+').write('placeholdertext')
os.remove('programa.py')
while True:
    print('='*50)
    print('Bem vindo a IDE do Zac!\n\nEscolha o que fazer:\n[0] Escrever códigos\n[1] Excluir códigos\n[2] Executar\n[3] Ver códigos\n[4] Sair')
    print('='*50)
    opt = input('...')
    match opt:
        case '0':
            print('\n'*50)
            sair = True
            print('\n'*50)
            print('Digite seu código. Digite apenas 0 e pressione ENTER para voltar.\n','='*50)
            while sair:
                new_line = input('/ ')
                if new_line != '0':
                    codigos.append(new_line)
                else:
                    break 
            print('\n'*50)
        case '1':
            print('\n'*50)
            codigos = []
            print('Códigos excluídos\n\n')
        case '2':
            print('\n'*50)
            print('EXECUTANDO programa.py')
            print('='*50)
            print('\n')
            with open('programa.py', 'a+', encoding='latin-1') as programa:
                for i in codigos:
                    programa.write('\n')
                    programa.write(i)
            os.system('python programa.py')
            print('\n')
            print('='*50)
            input('\nPressione ENTER para voltar ao menu\n')
            print('\n'*50)
        case '3':
            print('\n'*50)
            print('\n')
            if len(codigos) == 0:
                print('Sem códigos')
            else:
                for i in codigos:
                    print(i)
            input('\nPressione ENTER para voltar\n')
            print('\n'*50)
        case '4':
            print('\n'*50)
            print('Obrigado por usar!\n\nFeito por Zac Milioli\n\n')
            input()
            break   