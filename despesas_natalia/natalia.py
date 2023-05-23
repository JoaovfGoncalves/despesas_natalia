import msvcrt
def mostrar_menu():
    print('Escolha uma das seguintes opções:')
    print('[1] Adicionar Despesa\n[2] Remover Despesa\n[3] Atualizar Despesa\n[4] Exibir Despesas\n'
          '[6] Consultar Saldo\n[7] Adicionar Saldo\n[Esc] Sair')


def adicionar_despesa(valor, categoria, item, data):
    arq = open('despesas.csv', 'a', encoding='utf8')
    despesa = {'valor': valor, 'categoria': categoria,
               'item': item, 'data': data}
    despesas.append(despesa)
    arq.write(str(despesa)+'\n')
    arq.close()


def lista_despesas():
    print('\nAqui estão suas despesas listadas:')
    print('----------------------------------')
    contador = 0
    total = 0
    print(
        f'# nº - {"Data":^20} - {"Categoria":^20} - {"Item":^20} - {"Valor (R$)":^20}')
    for despesa in despesas:
        print(
            f'# {contador+1} - {despesa["data"]:^20} - {despesa["categoria"]:^20} - '
            f'{despesa["item"]:^20} - {despesa["valor"]:^20.2f}')
        total += despesa['valor']
        contador += 1
    print(
        f'\nTotal..........................................................................R${total:.2f}')
    print('\n\n')


def remover_despesa():
    while True:
        lista_despesas()
        print('Que despesa você gostaria de remover, Nathália?')
        try:
            print('Insira o número ao lado do "#" da despesa que você deseja remover.')
            despesa_removida = int(input('>> ')) - 1
            del despesas[despesa_removida]
            exportar_despesas()
            print('\nDespesa removida com sucesso.')
            break
        except:
            print('Comando inválido. Tente novamente.')


def atualizar_despesa(despesa_atualizada, valor_atualizado, categoria_atualizada, item_atualizado, data_atualizada):
    despesas[despesa_atualizada] = {
        'valor': valor_atualizado, 'categoria': categoria_atualizada, 'item': item_atualizado, 'data': data_atualizada}
    exportar_despesas()


def importar_despesas():
    arq = open('despesas.csv', 'r', encoding='utf8')
    dicionarios = arq.readlines()
    for dicionario in dicionarios:
        despesas.append(eval(dicionario))
    arq.close()


def exportar_despesas():
    arq = open('despesas.csv', 'w', encoding='utf8')
    for despesa in despesas:
        arq.write(str(despesa)+'\n')
    arq.close()


def despesas_categoria(categoria_desejada):
    contador = 0
    total = 0
    print(
        f'# nº - {"Data":^20} - {"Categoria":^20} - {"Item":^20} - {"Valor (R$)":^20}')
    for despesa in despesas:
        if despesa.get('categoria') == categoria_desejada:
            print(
                f'# {contador+1} - {despesa["data"]:^20} - {despesa["categoria"]:^20} - '
                f'{despesa["item"]:^20} - {despesa["valor"]:^20.2f}')
            total += despesa['valor']
            contador += 1
    print(
        f'\nTotal..........................................................................R${total:.2f}')
    print('\n\n')


def tratativa_valor(valor):
    valor = [str(a) for a in valor]
    if ',' in valor:
        valor[valor.index(',')] = '.'
        valor = ''.join(valor)
    else:
        valor = ''.join(valor)
    valor = float(valor)
    return valor


def tratativa_texto(texto):
    texto = [str(a) for a in texto]
    if ',' in texto:
        texto[texto.index(',')] = '—'
        texto = ''.join(texto)
    else:
        texto = ''.join(texto)
    return texto


login = input('Insira seu login:\n')
senha = input('Insira sua senha:\n')

if login == 'a' and senha == 'b':
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
                except:
                    print('Comando inválido. Tente novamente.')
            print('Insira a categoria da despesa:')
            while True:
                try:
                    categoria = tratativa_texto(input('>> ').capitalize())
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Insira o item da despesa:')
            while True:
                try:
                    item = tratativa_texto(input('>> ').capitalize())
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Insira a data da despesa:')
            while True:
                try:
                    data = tratativa_texto(input('>> '))
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            adicionar_despesa(valor, categoria, item, data)
            print('\nTransação adicionada com sucesso.\n')
        elif opcao_escolhida == '2':
            remover_despesa()
        elif opcao_escolhida == '3':
            lista_despesas()
            print('Que despesa você gostaria de atualizar, Nathália?')
            while True:
                try:
                    despesa_atualizada = int(input(
                        'Insira o número ao lado do "#" da despesa que você deseja atualizar.\n>> '))-1
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Deseja atualizar o valor?\n[S/N]')
            while True:
                try:
                    alterar_valor = input('>> ').upper()
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            while True:
                try:
                    if alterar_valor == 'S':
                        valor_atualizado = tratativa_valor(
                            input('Digite o novo valor:\n>>R$ '))
                        break
                    elif alterar_valor == 'N':
                        valor_atualizado = despesas[despesa_atualizada].get(
                            'valor')
                        break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Deseja alterar o nome da categoria?\n[S/N]')
            while True:
                try:
                    alterar_categoria = input('>> ').upper()
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            while True:
                try:
                    if alterar_categoria == 'S':
                        categoria_atualizada = tratativa_texto(
                            input('Digite o novo nome da categoria:\n>> '))
                        break
                    elif alterar_categoria == 'N':
                        categoria_atualizada = despesas[despesa_atualizada].get(
                            'categoria')
                        break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Deseja alterar o nome do item dessa despesa?\n[S/N]')
            while True:
                try:
                    alterar_item = input('>> ').upper()
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            while True:
                if alterar_item == 'S':
                    item_atualizado = tratativa_texto(
                        input('Digite o novo nome do item:\n>> '))
                    break
                elif alterar_item == 'N':
                    item_atualizado = despesas[despesa_atualizada].get(
                        'item')
                    break
                else:
                    print('Comando inválido. Tente novamente.')
            print('Deseja alterar a data dessa despesa?\n[S/N]')
            while True:
                try:
                    alterar_data = input('>> ').upper()
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            while True:
                if alterar_data == 'S':
                    data_atualizada = tratativa_texto(
                        input('Digite a data atualizada dessa despesa:\n>> '))
                    break
                elif alterar_data == 'N':
                    data_atualizada = despesas[despesa_atualizada].get(
                        'data')
                    break
                else:
                    print('Comando inválido. Tente novamente.')
            atualizar_despesa(despesa_atualizada,
                              valor_atualizado, categoria_atualizada, item_atualizado, data_atualizada)
            print('\nDespesa atualizada com sucesso.\n')
        elif opcao_escolhida == '4':
            lista_despesas()
            print(
                'Deseja visualizar os gastos de uma categoria específica?\n[S/N]')
            while True:
                try:
                    visualizar_categoria = input('>> ').upper()
                    break
                except:
                    print('Comando inválido. Tente Novamente')
            while True:
                try:
                    if visualizar_categoria == 'S':
                        categoria_desejada = input('Insira a categoria da qual você deseja visualizar os gastos\n'
                                                   '>> ').capitalize()
                        despesas_categoria(categoria_desejada)
                        break
                    elif visualizar_categoria == 'N':
                        break
                except:
                    print('Comando inválido. Tente Novamente')
        else:
            print('Comando inválido. Tente novamente.')
else:
    print('Não é a Nathália.')
