import string


def remover_acentos(txt):
    return ''.join(c for c in txt if c not in string.punctuation).translate(str.maketrans('', '', 'áàãâéêíóôõúüçÁÀÃÂÉÊÍÓÔÕÚÜÇ'))


def contar_palavras(texto):
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem


def exibir_ranking(contagem):
    ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    for palavra, cont in ranking:
        print(f'{palavra}: {cont}')


def exibir_menu():
    print('MENU DE OPÇÕES:')
    print('1 - Remover acentos e exibir texto')
    print('2 - Contar palavras e exibir ranking')
    print('3 - Exibir a palavra com mais aparições')
    print('4 - Exibir a palavra com menos aparições')
    print('0 - Encerrar aplicação')


if __name__ == '__main__':
    # Leitura do arquivo
    with open('arquivo.txt', 'r') as f:
        texto = f.read()

    while True:
        exibir_menu()
        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            texto_sem_acentos = remover_acentos(texto)
            print(texto_sem_acentos)

        elif opcao == '2':
            contagem = contar_palavras(texto)
            exibir_ranking(contagem)

        elif opcao == '3':
            contagem = contar_palavras(texto)
            ranking = sorted(contagem.items(),
                             key=lambda x: x[1], reverse=True)
            print(
                f'A palavra com mais aparições é "{ranking[0][0]}" com {ranking[0][1]} aparições.')

        elif opcao == '4':
            contagem = contar_palavras(texto)
            ranking = sorted(contagem.items(), key=lambda x: x[1])
            print(
                f'A palavra com menos aparições é "{ranking[0][0]}" com {ranking[0][1]} aparições.')

        elif opcao == '0':
            break

        else:
            print('Opção inválida. Tente novamente.')
