import string
import tkinter as tk
from tkinter import filedialog

# Atividade 01 - Carregar arquivo
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)



# Atividade 02 - Retire os acentos e exiba o texto reescrito
def remover_acentos(txt):
    return ''.join(c for c in txt if c not in string.punctuation).translate(str.maketrans('', '', 'áàãâéêíóôõúüçÁÀÃÂÉÊÍÓÔÕÚÜÇ'))



# Atividade 03 - Realize a contagem das palavras (que deverão ser ranqueadas em forma decrescente)
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



# Atividade 04 - Permita ao usuário saber qual palavra que ele deseja e quantas aparições.
def escolher_palavras(texto):
    palavras = input("Insira a palavra que deseja saber quantas vezes aparece no texto: ")
    palavras = palavras.split(",")
    ocorrencias = {}

    for palavra in palavras:
        ocorrencias[palavra.strip()] = texto.count(palavra.strip())

    for palavra, num_ocorrencias in ocorrencias.items():
        print(f"A palavra '{palavra}' aparece {num_ocorrencias} vezes no texto.")



# Atividade 06 - Mostre um menu para as escolhas acima e use o 0 para encerrar a aplicação.
def exibir_menu():
    print('-----------------------------------------------')
    print('MENU DE OPÇÕES:')
    print('-----------------------------------------------')
    print('1 - Remover acentos e exibir texto sem acentos')
    print('2 - Contar palavras e exibir ranking')
    print('3 - Escolher palavras para contar')
    print('4 - Exibir a palavra com mais aparições')
    print('5 - Exibir a palavra com menos aparições')
    print('0 - Encerrar aplicação')
    print('-----------------------------------------------')



if __name__ == '__main__':
    with open('Atividade-Cloud-Texto.txt', 'r') as f:
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
            escolher_palavras(texto)

        # Atvidade 05a - Exibir a palavra com mais aparição.
        elif opcao == '4':
            contagem = contar_palavras(texto)
            ranking = sorted(contagem.items(),
                             key=lambda x: x[1], reverse=True)
            print(
                f'A palavra com mais aparições é "{ranking[0][0]}" com {ranking[0][1]} aparições.')
            
        # Atvidade 05b - Exibir a palavra com menos aparição
        elif opcao == '5':
            contagem = contar_palavras(texto)
            ranking = sorted(contagem.items(), key=lambda x: x[1])
            print(
                f'A palavra com menos aparições é "{ranking[0][0]}" com {ranking[0][1]} aparições.')

        elif opcao == '0':
            break

        else:
            print('Opção inválida. Tente novamente.')