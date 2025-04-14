import math 

tabuleiro =[
    ['0', '1', '2'],
    ['3', '4', '5'],
    ['6', '7', '8']
    ]
terminou = False
numero_da_rodada = 0

#print(f"{tabuleiro[0]}\n{tabuleiro[1]}\n{tabuleiro[2]}")
print()
print('Bem-vindo ao jogo da velha')
print('Etapa 0 : definir jogadores.')
print('Digite o nome do primeiro jogador')
nome_jogador1 = str(input())
print('Digite o nome do segundo jogador')
nome_jogador2 = str(input())
print('Começa o jogo')
while(terminou == False):
    jogador_da_vez = ''
    simbolo = ''

    if numero_da_rodada%2 == 0:
        jogador_da_vez = nome_jogador1
        simbolo = 'X'
    else:
        jogador_da_vez = nome_jogador2
        simbolo = 'O'

    print(f'Etapa {numero_da_rodada+1}: Vez do {jogador_da_vez}')
    print(f"{tabuleiro[0]}\n{tabuleiro[1]}\n{tabuleiro[2]}")
    print('Escolha uma casa numerada nesse tabuleiro')
    casa_do_tabuleiro = int(input())
    linha_do_tabuleiro = math.floor(casa_do_tabuleiro / 3)     
    coluna_do_tabuleiro = (casa_do_tabuleiro % 3)
    tabuleiro[linha_do_tabuleiro][coluna_do_tabuleiro] = simbolo
    numero_da_rodada += 1
    

