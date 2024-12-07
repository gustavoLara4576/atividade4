from library import *

exibirTitulo()
parar = False
while parar == False:
    sleep(1)
    exibirOpcoes()
    acaoEscolhida = input('').strip()
    if acaoEscolhida == '1':
        listar()
    elif acaoEscolhida == '2':
        consultar()
    elif acaoEscolhida == '3':
        adicionar()
    elif acaoEscolhida == '4':
        editar()
    elif acaoEscolhida == '5':
        remover()
    elif acaoEscolhida == '6':
        consultarTodas()
    elif acaoEscolhida == '0':
        parar = True
        final = ' PROGRAMA ENCERRADO '
        final2 = '  ATÉ A PRÓXIMA  '
        print('{:=^60}'.format(final))
        print('{:=^60}'.format(final2))
        print('\n\n')
    else:
        print('Opcão inválida')
