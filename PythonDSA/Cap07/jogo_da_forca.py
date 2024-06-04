import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls') #windows
    else:
        _ = system('clear') #Linux, Mac

def game():
    limpa_tela()

    print('\nBem-vindo(a) ao jogo da forca!')
    print('Adivinhe a palavra abaixo:\n')

    palavras = ['cachorro','cavalo','macaco','zebra','papagaio','hipopótamo']

    palavra = random.choice(palavras)

    letras_descobertas = ['_' for letra in palavra]

    chances = 7

    letras_erradas = []

    while chances > 0:

        print(' '.join(letras_descobertas))
        print('\nChances restantes: ', chances)
        print('Letras erradas: ', ' '.join(letras_erradas))

        tentativa = input('\nDigite uma letra: ').lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra: #verifica cada letra da palavra selecionada
                if tentativa == letra:
                    letras_descobertas[index] = letra #se a letra estiver na palavra irá substituir a letra na posição
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if '_' not in letras_descobertas: #se toda a palavra estiver descoberta jogador venceu
            print('\nVocê venceu, a palavra era: ', palavra)
            break

    if '_' in letras_descobertas: #se ainda tem espaços vazios e não tem mais chance, o jogador perdeu
        print('\nVocê perdeu, a palavra era: ', palavra)

if __name__ == '__main__': #define que este é um programa python
    game()
    print('\nParabéns. Você está aprendendo programação em Python. \n') 