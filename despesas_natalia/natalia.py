def mostrar_menu():
    print('Escolha uma das seguintes opções:')
    print('[1] Adicionar despesa\n[2] Remover despesa\n[3] Atualizar despesa\n[4] Listar despesas')


def adicionar_despesa(valor, categoria, item, data):
    despesa = {'valor': valor, 'categoria': categoria,
               'item': item, 'data': data}
    despesas.append(despesa)


def lista_despesas():
    print('\nAqui estão suas despesas listadas:')
    print('----------------------------------')
    contador = 0
    for despesa in despesas:
        print(
            f'# {contador+1} - {despesa["data"]:^10} - {despesa["categoria"]:^10} - '
            f'{despesa["item"]:^10} - R$ {despesa["valor"]:.2f}')
        contador += 1
    print('\n\n')


def remover_despesa():
    while True:
        lista_despesas()
        print('Que despesa você gostaria de remover, Natalia?')
        try:
            print('Insira o número ao lado do "#" da despesa que você deseja remover.')
            despesa_removida = int(input('>> '))-1
            del despesas[despesa_removida]
            print('Despesa removida com sucesso.')
            break
        except:
            print('Comando inválido. Tente novamente.')


def atualizar_despesa(despesa_atualizada, valor_atualizado, categoria_atualizada, item_atualizado, data_atualizada):
    despesas[despesa_atualizada] = {
        'valor': valor_atualizado, 'categoria': categoria_atualizada, 'item': item_atualizado, 'data': data_atualizada}


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
        texto[texto.index(',')] = '/'
        texto = ''.join(texto)
    else:
        texto = ''.join(texto)
    return texto


despesas = []

login = input('Insira seu Login:\n')
senha = input('Insira sua senha:\n')

if login == 'a' and senha == 'b':
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
            print('Transação adicionada com sucesso.\n')
        elif opcao_escolhida == '2':
            remover_despesa()
        elif opcao_escolhida == '3':
            lista_despesas()
            print('Que despesa você gostaria de atualizar, Natalia?')
            while True:
                try:
                    despesa_atualizada = int(input(
                        'Insira o número ao lado do "#" da despesa que você deseja atualizar.\n>> '))-1
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Qual é o valor atualizado?')
            while True:
                try:
                    valor_atualizado = tratativa_valor(
                        input('>>R$ '))
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Deseja alterar o nome da categoria?\n[S]/[N]')
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
            print('Deseja alterar o nome dessa despesa?\n[S]/[N]')
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
            print('Deseja alterar a data dessa despesa?\n[S]/[N]')
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
            print('Despesa atualizada com sucesso.\n')
        elif opcao_escolhida == '4':
            lista_despesas()
        else:
            print('Comando inválido. Tente novamente.')
else:
    print('Não é a Natália.')
