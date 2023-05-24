from datetime import datetime


import matplotlib.pyplot as plt


def mostrar_menu():
    print('Escolha uma das seguintes opções:')
    print('[1] Adicionar Despesa\n[2] Excluir Despesa\n[3] Atualizar Despesa\n[4] Listar Despesas\n'
          '[5] Consultar Saldo\n[6] Adicionar Saldo\n[7] Ver gráfico de categorias\n[0] Sair')


def adicionar_despesa(valor, categoria, item, data):
    despesa = {'valor': valor, 'categoria': categoria,
               'item': item, 'data': data}
    despesas.append(despesa)
    arquivo = open('despesas.csv', 'a', encoding='utf8')
    arquivo.write(str(despesa)+'\n')
    arquivo.close()


def excluir_despesa(despesa_excluida):
    del despesas[despesa_excluida]
    exportar_despesas()


def atualizar_despesa(despesa_atualizada, valor_atualizado, categoria_atualizada, item_atualizado, data_atualizada):
    despesas[despesa_atualizada] = {
        'valor': valor_atualizado, 'categoria': categoria_atualizada, 'item': item_atualizado, 'data': data_atualizada}
    exportar_despesas()


def lista_despesas():
    print('\nAqui estão suas despesas listadas:')
    print('----------------------------------')
    total = 0
    print(
        f'# nº - {"Data":^25} - {"Categoria":^25} - {"Item":^25} - {"Valor (R$)":^25}')
    for indice, despesa in enumerate(despesas):
        print(
            f'# {indice+1} - {despesa["data"]:^25} - {despesa["categoria"]:^25} - '
            f'{despesa["item"]:^25} - {despesa["valor"]:^25.2f}')
        total += despesa['valor']
    print(
        f'\nTotal.............................................................................R${total:.2f}')
    print('\n\n')


def importar_despesas():
    arquivo = open('despesas.csv', 'r', encoding='utf8')
    dicionarios = arquivo.readlines()
    if dicionarios == []:
        pass
    else:
        for dicionario in dicionarios:
            despesas.append(eval(dicionario))
    arquivo.close()


def exportar_despesas():
    arquivo = open('despesas.csv', 'w', encoding='utf8')
    for despesa in despesas:
        arquivo.write(str(despesa)+'\n')
    arquivo.close()


def exibir_categoria(categoria_desejada):
    total = 0
    print(
        f'\n# nº - {"Data":^20} - {"Categoria":^20} - {"Item":^20} - {"Valor (R$)":^20}')
    for indice, despesa in enumerate(despesas):
        if despesa.get('categoria') == categoria_desejada:
            print(
                f'# {indice+1} - {despesa["data"]:^20} - {despesa["categoria"]:^20} - '
                f'{despesa["item"]:^20} - {despesa["valor"]:^20.2f}')
            total += despesa['valor']
    print(
        f'\nTotal..........................................................................R${total:.2f}')
    print('\n\n')


def categorias_existentes():
    for categoria in despesas:
        if categoria['categoria'] not in categorias:
            categorias.append(categoria['categoria'])
    print('Categorias:\n')
    for indice, categoria in enumerate(categorias):
        print(f'[{indice+1}] {categoria}')


def importar_saldo():
    arquivo = open('saldo.csv', 'r+')
    quantia_saldo = arquivo.read().strip()
    if quantia_saldo:
        quantia_saldo = float(quantia_saldo)
    else:
        quantia_saldo = 0.0
        arquivo.write(str(quantia_saldo))
    arquivo.close()
    return quantia_saldo


def subtrair_saldo(debito):
    arquivo = open('saldo.csv', 'r+')
    quantia_saldo = arquivo.read().strip()
    novo_saldo = float(quantia_saldo) - debito
    arquivo.seek(0)
    arquivo.write(str(novo_saldo))
    arquivo.close()


def adicionar_saldo(credito):
    arquivo = open('saldo.csv', 'r+')
    quantia_saldo = arquivo.read().strip()
    novo_saldo = float(quantia_saldo) + credito
    arquivo.seek(0)
    arquivo.write(str(novo_saldo))
    arquivo.close()


def exibir_grafico_categoria():
    categorias = []
    valores = []

    for despesa in despesas:
        categoria = despesa.get('categoria')
        valor = despesa.get('valor')
        if categoria in categorias:
            index = categorias.index(categoria)
            valores[index] += valor
        else:
            categorias.append(categoria)
            valores.append(valor)

    plt.figure(figsize=(8, 6))
    plt.pie(valores, labels=categorias, autopct='%1.1f%%')
    plt.title('Despesas por Categoria')
    plt.axis('equal')
    plt.show()


def tratativa_valor(valor):
    valor = [str(caracter) for caracter in valor]
    if ',' in valor:
        valor[valor.index(',')] = '.'
        valor = ''.join(valor)
    else:
        valor = ''.join(valor)
    valor = float(valor)
    return valor


def tratativa_texto(texto):
    texto = [str(caracter) for caracter in texto]
    if ',' in texto:
        texto[texto.index(',')] = '—'
        texto = ''.join(texto)
    else:
        texto = ''.join(texto)
    return texto


def verificar_validade_data(data_inserida):
    try:
        datetime.strptime(data_inserida, "%d/%m/%Y")

        dia, mes, ano = map(int, data_inserida.split('/'))
        datetime(ano, mes, dia)

        return True
    except ValueError:
        return False


login = input('Insira seu login:\n')
senha = input('Insira sua senha:\n')

if login == 'a' and senha == 'b':
    categorias = []
    despesas = []
    importar_despesas()
    while True:
        mostrar_menu()
        opcao_escolhida = input('>> ')
        if opcao_escolhida == '1':
            print('Insira o valor da despesa:')
            while True:
                try:
                    valor = tratativa_valor(input('>>R$ '))
                    break
                except ValueError:
                    print(
                        '//ERRO//\n\nCertifique-se de que está inserindo o valor corretamente (Modelo R$ NN.nn).\n\n//ERRO//')
            print(
                '\nEssa despesa se encaixa em uma categoria já cadastrada? [S/N]\n\nConfira na lista:\n')
            while True:
                categorias_existentes()
                try:
                    categoria_repetitiva = input('>> ').upper()
                    if categoria_repetitiva not in ['S', 'N']:
                        raise ValueError
                    break
                except ValueError:
                    print(
                        '//ERRO//\n\nCertifique-se de que você digitou apenas S ou N.\n\n//ERRO//')
            if categoria_repetitiva == 'S':
                while True:
                    print('\nIndique a categoria que deseja repetir:\n')
                    categorias_existentes()
                    try:
                        categoria = int(input('>> ')) - 1
                        if categoria < 0:
                            raise IndexError
                        categoria = categorias[categoria]
                        break
                    except ValueError:
                        print('//ERRO//\n\nCertifique-se de que você digitou apenas o número dentro dos "[]" '
                              'da categoria que deseja excluir e tente novamente.\n\n//ERRO//')
                    except IndexError:
                        print(
                            '//ERRO//\n\nCertifique-se de que o número digitado consta na lista.\n\n//ERRO//')
            elif categoria_repetitiva == 'N':
                while True:
                    print('\nInsira a categoria da despesa:')
                    try:
                        categoria = tratativa_texto(
                            input('>> ').capitalize())
                        break
                    except EOFError:
                        print('Comando inválido. Tente novamente.')
            print('Insira o item da despesa:')
            while True:
                try:
                    item = tratativa_texto(input('>> ').capitalize())
                    break
                except EOFError:
                    print('Comando inválido. Tente novamente.')
            adicionar_despesa(valor, categoria, item,
                              datetime.now().strftime("%d/%m/%Y"))
            subtrair_saldo(despesas[-1].get('valor'))
            print('\nTransação adicionada com sucesso.\n')
        elif opcao_escolhida == '2':
            while True:
                lista_despesas()
                print('Que despesa você gostaria de excluir, Nathália?')
                print(
                    'Insira o número ao lado do "#" da despesa que você deseja excluir.')
                try:
                    despesa_excluida = int(input('>> ')) - 1
                    if despesa_excluida < 0:
                        raise IndexError
                    adicionar_saldo(despesas[despesa_excluida].get('valor'))
                    excluir_despesa(despesa_excluida)
                    break
                except ValueError:
                    print('//ERRO//\n\nCertifique-se de que você digitou apenas o número ao lado do "#" da despesa que deseja excluir'
                          'e tente novamente.\n\n//ERRO//')
                except IndexError:
                    print(
                        '//ERRO//\n\nCertifique-se de que o número digitado consta na lista.\n\n//ERRO//')
            print('\nDespesa excluída com sucesso.\n')
        elif opcao_escolhida == '3':
            lista_despesas()
            print('Que despesa você gostaria de atualizar, Nathália?')
            while True:
                try:
                    despesa_atualizada = int(input(
                        'Insira o número ao lado do "#" da despesa que você deseja atualizar.\n>> '))-1
                    if despesa_atualizada < 0:
                        raise IndexError
                    break
                except IndexError:
                    print('//ERRO//\n\nCertifique-se de que você digitou apenas o número ao lado do "#" da despesa que deseja excluir'
                          'e tente novamente.\n\n//ERRO//')
                except ValueError:
                    print('//ERRO//\n\nCertifique-se de que você digitou apenas o número ao lado do "#" da despesa que deseja excluir'
                          'e tente novamente.\n\n//ERRO//')
            print('Deseja atualizar o valor?\n[S/N]')
            while True:
                try:
                    alterar_valor = input('>> ').upper()
                    if alterar_valor not in ['S', 'N']:
                        raise ValueError
                    break
                except ValueError:
                    print(
                        '//ERRO//\n\nCertifique-se de que você digitou apenas S ou N.\n\n//ERRO//')
            while True:
                if alterar_valor == 'S':
                    try:
                        valor_atualizado = tratativa_valor(
                            input('Digite o novo valor:\n>>R$ '))
                        break
                    except ValueError:
                        print(
                            '\n//Certifique-se de que está inserindo o valor corretamente (Modelo R$ NN.nn).//\n')
                elif alterar_valor == 'N':
                    valor_atualizado = despesas[despesa_atualizada].get(
                        'valor')
                    break
            print('Deseja alterar o nome da categoria?\n[S/N]')
            while True:
                try:
                    alterar_categoria = input('>> ').upper()
                    if alterar_categoria not in ['S', 'N']:
                        raise ValueError
                    break
                except ValueError:
                    print(
                        '//ERRO//\n\nCertifique-se de que você digitou apenas S ou N.\n\n//ERRO//')
            while True:
                if alterar_categoria == 'S':
                    categoria_atualizada = tratativa_texto(
                        input('Digite o novo nome da categoria:\n>> '))
                    break
                if alterar_categoria == 'N':
                    categoria_atualizada = despesas[despesa_atualizada].get(
                        'categoria')
                    break
            print('Deseja alterar o nome do item dessa despesa?\n[S/N]')
            while True:
                try:
                    alterar_item = input('>> ').upper()
                    if alterar_item not in ['S', 'N']:
                        raise ValueError
                    break
                except ValueError:
                    print(
                        '//ERRO//\n\nCertifique-se de que você digitou apenas S ou N.\n\n//ERRO//')
            while True:
                if alterar_item == 'S':
                    item_atualizado = tratativa_texto(
                        input('Digite o novo nome do item:\n>> '))
                    break
                if alterar_item == 'N':
                    item_atualizado = despesas[despesa_atualizada].get(
                        'item')
                    break
            print('Deseja alterar a data dessa despesa?\n[S/N]')
            while True:
                try:
                    alterar_data = input('>> ').upper()
                    if alterar_data not in ['S', 'N']:
                        raise ValueError
                    break
                except ValueError:
                    print(
                        '//ERRO//\n\nCertifique-se de que você digitou apenas S ou N.\n\n//ERRO//')
            while True:
                if alterar_data == 'S':
                    data_inserida = input(
                        'Digite a data atualizada dessa despesa (formato: dd/mm/aa):\n>> ')
                    if verificar_validade_data(data_inserida):
                        data_atualizada = data_inserida
                        break
                    else:
                        print(
                            '//ERRO//\n\nCertifique-se de que você digitou uma data válida no formato correto (dd/mm/aa).\n\n//ERRO//')
                elif alterar_data == 'N':
                    data_atualizada = despesas[despesa_atualizada].get(
                        'data')
                    break
            adicionar_saldo(despesas[despesa_atualizada].get('valor'))
            atualizar_despesa(despesa_atualizada,
                              valor_atualizado, categoria_atualizada, item_atualizado, data_atualizada)
            subtrair_saldo(despesas[despesa_atualizada].get('valor'))
            print('\nDespesa atualizada com sucesso.\n')
        elif opcao_escolhida == '4':
            lista_despesas()
            print(
                'Deseja visualizar os gastos de uma categoria específica?\n[S/N]')
            while True:
                try:
                    visualizar_categoria = input('>> ').upper()
                    if visualizar_categoria not in ['S', 'N']:
                        raise ValueError
                    break
                except ValueError:
                    print(
                        '//ERRO//\n\nCertifique-se de que você digitou apenas S ou N.\n\n//ERRO//')
            while True:
                if visualizar_categoria == 'S':
                    categorias_existentes()
                    try:
                        categoria_indicada = int(
                            input('Insira a categoria da qual você deseja visualizar os gastos\n>> ')) - 1
                        if categoria_indicada < 0:
                            raise IndexError
                    except IndexError:
                        print(
                            '//ERRO//\n\nCertifique-se de que o número digitado consta na lista.\n\n//ERRO//')
                    except ValueError:
                        print(
                            '//ERRO//\n\nCertifique-se de que você digitou um número.\n\n//ERRO//')
                    exibir_categoria(categorias[categoria_indicada])
                    break
                elif visualizar_categoria == 'N':
                    break
        elif opcao_escolhida == '5':
            saldo = importar_saldo()
            print(f'\n\nSeu saldo está em R${saldo:.2f}\n\n')
        elif opcao_escolhida == '6':
            print('Insira quanto será adicionado ao seu saldo:')
            while True:
                try:
                    credito = tratativa_valor(input('>>R$ '))
                    if credito < 0:
                        raise ValueError
                    break
                except ValueError:
                    print(
                        'Certifique-se que um valor válido foi inserido.\n(modelo:R$ NN.nn)')
            adicionar_saldo(credito)
            print('\nSaldo adicionado com sucesso.\n')
        elif opcao_escolhida == '7':
            exibir_grafico_categoria()
        elif opcao_escolhida == '0':
            break
        else:
            print('Opção inválida.')
else:
    print('Não é a Nathália.')
