from time import sleep

infoCasas = {
    'Targaryen': {'Lema': 'Fogo e Sangue.', 'Região': 'Pedra do Dragão', 'Figura Lendária' : 'Aegon, o Conquistador', 'Principal Membro' : 'Daenerys Targaryen'},
    'Baratheon': {'Lema' : 'Nossa é a Fúria.', 'Região' : 'Terras da Tempestade', 'Figura Lendária' : 'Orys Baratheon', 'Principal Membro' : 'Robert Baratheon'},
    'Stark': {'Lema': 'O Inverno Está Chegando.', 'Região': 'O Norte', 'Figura Lendária': 'Brandon, o Construtor', 'Principal Membro': 'Eddard Stark'},
    'Lannister': {'Lema': 'Ouça-me Rugir.', 'Região': 'Terras Ocidentais', 'Figura Lendária': 'Lann, o Esperto', 'Principal Membro': 'Tywin Lannister'},
    'Tyrell': {'Lema': 'Crescendo Fortes.', 'Região': 'A Campina', 'Figura Lendária': 'Garth, o Verde', 'Principal Membro': 'Margaery Tayrell'},
    'Arryn': {'Lema': 'Tão Alto Como a Honra.', 'Região': 'Vale de Arryn', 'Figura Lendária': 'Artys Arryn, o Falcão Andante', 'Principal Membro': 'Jon Arryn'},
    'Tully': {'Lema': 'Família, Dever, Honra.', 'Região': 'Terras Fluviais', 'Figura Lendária': 'Edmyn Tully', 'Principal Membro': 'Catelyn Tully'},
    'Martell': {'Lema': 'Incurvados, Não Quebrados.', 'Região': 'Dorne', 'Figura Lendária': 'Princesa Nymeria', 'Principal Membro': 'Doran Martell'},
    'Greyjoy': {'Lema': 'Nós Não Semeamos', 'Região': 'Ilhas de Ferro', 'Figura Lendária':'Greyiron', 'Principal Membro':'Balon Greyjoy'}
    }

def exibirTitulo():
    titulo = ' GERENCIADOR DE CASAS '
    titulo2 = '  GAME OF THRONES  '
    print('\n\n')
    print('{:=^60}'.format(titulo))
    print('{:=^60}'.format(titulo2))

def exibirOpcoes():
    print('\nO QUE DESEJA FAZER?\n')
    print('(1) Listar as casas')
    print('(2) Consultar uma casa')
    print('(3) Adicionar uma casa')
    print('(4) Editar uma casa')
    print('(5) Remover uma casa')
    print('(6) Consultar todas as casas')
    print('(0) Sair')

def listar():
    print('\n{:-^60}'.format(' CASAS REGISTRADAS '))
    for casa in infoCasas:
        print('●', casa)
        sleep(0.5)
    print('-'*60,'\n')
    sleep(4)

def adicionar(casaDefinida=None):
    if casaDefinida is not None:
        print('\n{:-^60}'.format(' ADICIONAR CASA '))
        sleep(1)
        nomeCasa = (casaDefinida.strip().title())
        print(f'\nQual o nome da casa?  {nomeCasa}')
        sleep(1)
        lemaCasa = input('\nQual o lema da casa?  ')
        regiaoCasa = input('\nQual a região da casa?  ')
        lendaCasa = input('\nQual a figura lendária da casa?  ')
        membroCasa = input('\nQual o principal membro da casa?  ')
        infoCasas[nomeCasa] = {'Lema':lemaCasa, 'Região': regiaoCasa, 'Figura Lendária': lendaCasa, 'Principal Membro': membroCasa}
        print('\n'+'-'*60,'\n')
        print('\nCasa adicionada com sucesso!.\n')
        sleep(1.5)
        print('\n{:-^60}'.format(' CASA '+ nomeCasa.upper()+' '))
        sleep(0.5)
        print('\n● LEMA: {}'.format(infoCasas[nomeCasa.strip().title()]['Lema']))
        sleep(0.5)
        print('\n● REGIÃO: {}'.format(infoCasas[nomeCasa.strip().title()]['Região']))
        sleep(0.5)
        print('\n● FIGURA LENDÁRIA: {}'.format(infoCasas[nomeCasa.strip().title()]['Figura Lendária']))
        sleep(0.5)
        print('\n● PRINCIPAL MEMBRO: {}'.format(infoCasas[nomeCasa.strip().title()]['Principal Membro']))
        sleep(0.5)
        print('\n','-'*60,'\n')
        sleep(5)
    else:
        print('\n{:-^60}'.format(' ADICIONAR CASA '))
        nomeCasa = input('\nQual o nome da casa?  ').strip().title()
        lemaCasa = input('\nQual o lema da casa?  ')
        regiaoCasa = input('\nQual a região da casa?  ')
        lendaCasa = input('\nQual a figura lendária da casa?  ')
        membroCasa = input('\nQual o principal membro da casa?  ')
        infoCasas[nomeCasa] = {'Lema':lemaCasa, 'Região': regiaoCasa, 'Figura Lendária': lendaCasa, 'Principal Membro': membroCasa}
        print('\n'+'-'*60,'\n')
        print('\nCasa adicionada com sucesso!.\n')
        sleep(1.5)
        print('\n{:-^60}'.format(' CASA '+ nomeCasa.upper()+' '))
        sleep(0.5)
        print('\n● LEMA: {}'.format(infoCasas[nomeCasa.strip().title()]['Lema']))
        sleep(0.5)
        print('\n● REGIÃO: {}'.format(infoCasas[nomeCasa.strip().title()]['Região']))
        sleep(0.5)
        print('\n● FIGURA LENDÁRIA: {}'.format(infoCasas[nomeCasa.strip().title()]['Figura Lendária']))
        sleep(0.5)
        print('\n● PRINCIPAL MEMBRO: {}'.format(infoCasas[nomeCasa.strip().title()]['Principal Membro']))
        sleep(0.5)
        print('\n','-'*60,'\n')
        sleep(5)

def consultar():
    nomeConsultado = input('\nQUAL CASA DESEJA CONSULTAR?  ')
    if nomeConsultado.strip().capitalize() in infoCasas:
        print('\n{:-^60}'.format(' CASA '+ nomeConsultado.upper()+' '))
        sleep(0.5)
        print('\n● LEMA: {}'.format(infoCasas[nomeConsultado.strip().title()]['Lema']))
        sleep(0.5)
        print('\n● REGIÃO: {}'.format(infoCasas[nomeConsultado.strip().title()]['Região']))
        sleep(0.5)
        print('\n● FIGURA LENDÁRIA: {}'.format(infoCasas[nomeConsultado.strip().title()]['Figura Lendária']))
        sleep(0.5)
        print('\n● PRINCIPAL MEMBRO: {}'.format(infoCasas[nomeConsultado.strip().title()]['Principal Membro']))
        sleep(0.5)
        print('\n','-'*60,'\n')
        sleep(5)
    else:
        print('-'*60)
        print(f'A casa "{nomeConsultado.strip().title()}" não está registrada no gerenciador.')
        print('-'*60)
        sleep(4)
        while True:
            add = input(f'\nQuer adicionar a casa {nomeConsultado.title()} ao gerenciador?   (1) Sim   (0) Não  ').strip()
            if add == '1':
                adicionar(f'{nomeConsultado}')
                break
            if add == '0':
                break

def editar():
    encerrar = False
    while encerrar == False:
        casaEscolhida = input('\nQual casa deseja editar?   (0) para sair  ').strip().capitalize()
        if casaEscolhida in infoCasas:
            while True:
                print(f'\nO QUE DESEJA EDITAR DA CASA {casaEscolhida.upper()}?\n')
                print('(1) Nome da casa')
                print('(2) Lema')
                print('(3) Região')
                print('(4) Figura Lendária da Casa')
                print('(5) Principal Membro')
                opcaoEscolhida = input('').strip()
                if opcaoEscolhida.strip() == '1':
                    novoNome = (input('\nQual o novo nome da casa?  '))
                    infoCasas[novoNome] = infoCasas.pop(casaEscolhida)
                    print('\nNome atualizado com sucesso!')
                    sleep(2)
                    encerrar = True
                    break
                if opcaoEscolhida.strip() == '2':
                    novoLema = (input('\nQual o novo lema da casa?  '))
                    infoCasas[casaEscolhida]['Lema'] = f'{novoLema}'
                    print('\nLema atualizado com sucesso!')
                    sleep(2)
                    encerrar = True
                    break
                if opcaoEscolhida.strip() == '3':
                    novaRegiao = (input('\nQual a nova região da casa?  '))
                    infoCasas[casaEscolhida]['Região'] = f'{novaRegiao}'
                    print('\nRegião atualizada com sucesso!')
                    sleep(2)
                    encerrar = True
                    break
                if opcaoEscolhida.strip() == '4':
                    novaLenda = (input('\nQual a nova figura lendária da casa?  '))
                    infoCasas[casaEscolhida]['Figura Lendária'] = f'{novaLenda}'
                    print('\nFigura lendária atualizada com sucesso!')
                    sleep(2)
                    encerrar = True
                    break
                if opcaoEscolhida.strip() == '5':
                    novoMembro = (input('\nQual o novo membro principal da casa?  '))
                    infoCasas[casaEscolhida]['Principal Membro'] = f'{novoMembro}'
                    print('\nPrincipal membro da casa atualizado com sucesso!')
                    sleep(2)
                    encerrar = True
                    break
                else:
                    print('\nOpção inválida.')
        elif casaEscolhida == '0':
            encerrar = True
        else:
            print('\n','-'*60,'')
            print('A casa', casaEscolhida.capitalize(), 'não está registrada no gerenciador.')
            print('','-'*60,'\n')
            sleep(2)

def remover():
 encerrar = False
 while encerrar == False:
        casaEscolhida = input('\nQual casa você quer remover?   (0) para sair  ').strip().capitalize()
        if casaEscolhida in infoCasas:
            infoCasas.pop(casaEscolhida)
            print('\nCasa removida com sucesso!')
            sleep(1)
            listar()
            encerrar = True
        elif casaEscolhida == '0':
            encerrar = True
        else:
            print('\nA casa', casaEscolhida.capitalize(), 'não está registrada no gerenciador.')

def consultarTodas():
    for casa in infoCasas:
        print('\n{:-^60}'.format(' CASA '+ casa.upper()+' '))
        print('\n● LEMA: {}'.format(infoCasas[casa.strip().title()]['Lema']))
        print('\n● REGIÃO: {}'.format(infoCasas[casa.strip().title()]['Região']))
        print('\n● FIGURA LENDÁRIA: {}'.format(infoCasas[casa.strip().title()]['Figura Lendária']))
        print('\n● PRINCIPAL MEMBRO: {}'.format(infoCasas[casa.strip().title()]['Principal Membro']))
        print('\n','-'*60,'\n')
        sleep(1)
        