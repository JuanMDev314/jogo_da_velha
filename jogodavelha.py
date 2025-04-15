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
print(f"{tabuleiro[0]}\n{tabuleiro[1]}\n{tabuleiro[2]}")

def Jogo_Da_Velha():
     
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]:
        terminou = True
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]:
        terminou = True
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]:
        terminou = True
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
        terminou = True
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
        terminou = True
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
        terminou = True
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        terminou = True
    elif tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2]:
        terminou = True


while(terminou == False):
    numero_da_rodada += 1
    if numero_da_rodada == 10:
        print('Fim de jogo. Empate')
        break

    jogador_da_vez = ''
    simbolo = ''


    if (numero_da_rodada+1)%2 == 0:
        jogador_da_vez = nome_jogador1
        simbolo = 'x'
    else:
        jogador_da_vez = nome_jogador2
        simbolo = 'O'

    print(f'Etapa {numero_da_rodada}: Vez do {jogador_da_vez}')
    print('Escolha uma casa numerada nesse tabuleiro')
    casa_do_tabuleiro = int(input())
    if casa_do_tabuleiro > [2][2]:
        if (numero_da_rodada+1)%2 == 0:
            jogador_da_vez = nome_jogador1
            simbolo = 'x'
        else:
            jogador_da_vez = nome_jogador2
            simbolo = 'O'
        print('Jogue novamente. Movimento inválido')
    else: pass
    linha_do_tabuleiro = math.floor(casa_do_tabuleiro / 3)     
    coluna_do_tabuleiro = (casa_do_tabuleiro % 3)
    tabuleiro[linha_do_tabuleiro][coluna_do_tabuleiro] = simbolo
   


    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]:
        terminou = True
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]:
        terminou = True
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]:
        terminou = True
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
        terminou = True
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
        terminou = True
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
        terminou = True
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        terminou = True
    elif tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2]:
        terminou = True
    if terminou == True:
        print(f'Fim de Jogo!{jogador_da_vez} Venceu!')

    print(f"{tabuleiro[0]}\n{tabuleiro[1]}\n{tabuleiro[2]}")


