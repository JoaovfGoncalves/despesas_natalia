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
            despesa_removida = int(input('> '))-1
            del despesas[despesa_removida]
            print('Despesa removida com sucesso.')
            break
        except:
            print('Comando inválido. Tente novamente.')


def atualizar_despesa(despesa_atualizada, valor_atualizado, categoria_atualizada):
    despesas[despesa_atualizada] = {
        'valor': valor_atualizado, 'categoria': categoria_atualizada}


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
            print('De quanto foi a despesa?')
            while True:
                try:
                    valor = tratativa_valor(input('>>R$ '))
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Em que categoria se encontra essa despesa?')
            while True:
                try:
                    categoria = tratativa_texto(input('>> ').capitalize())
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Insira o item:')
            while True:
                try:
                    item = tratativa_texto(input('>> ').capitalize())
                    break
                except:
                    print('Comando inválido. Tente novamente.')
            print('Insira a data da compra:')
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
            while True:
                lista_despesas()
                print('Que despesa você gostaria de atualizar, Natalia?')
                try:
                    despesa_atualizada = int(input(
                        'Insira o número ao lado do "#" da despesa que você deseja atualizar.\n> '))-1
                    valor_atualizado = tratativa_valor(
                        input('Qual é o valor atualizado?\n> '))
                    alterar_nome_item = input(
                        'Deseja alterar o nome do item?\n[S]\[N]\n> ').upper()
                    if alterar_nome_item == 'S':
                        categoria_atualizada = tratativa_texto(
                            input('Digite o novo nome do item:\n> '))
                    else:
                        categoria_atualizada = despesas[despesa_atualizada].get(
                            'categoria')
                    atualizar_despesa(despesa_atualizada,
                                      valor_atualizado, categoria_atualizada)
                    break
                except:
                    print('Comando inválido. Tente novamente.')
        elif opcao_escolhida == '4':
            lista_despesas()
        else:
            print('Comando inválido. Tente novamente.')
else:
    print('Não é a Natália.')
