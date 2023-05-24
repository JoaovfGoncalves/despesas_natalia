if visualizar_categoria == 'S':
                    categorias_existentes()
                    try:
                        categoria_indicada = int(input('Insira a categoria da qual você deseja visualizar os gastos\n'
                                                       '>> ')) - 1
                    except IndexError:
                        print(
                            '//ERRO//\n\nCertifique-se de que o número digitado consta na lista.\n\n//ERRO//')
                    except ValueError:
                        print(
                            '//ERRO//\n\nCertifique-se de que você digitou um número.\n\n//ERRO//')
                    visualizar_categoria(categorias[categoria_indicada])