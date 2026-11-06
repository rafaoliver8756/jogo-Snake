import pygame

pygame.init()
tela = pygame.display.set_mode((600,600))


posicao_inicioX = 300
posicao_inicioY = 300
#posição inicial

velocidadeX = 0
#ela vai começar parada
velocidade_padrao = 5

cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)

cabeca_cobra = pygame.image.load("")
#importando imagem inicial da cobra

jogando = True
while jogando:
    for evento in pygame.event.get(): #esse comando guarda o que acontece no computador, se mexeu no mouse ou clicou em uma tecla
        if evento.type == pygame.QUIT: #se o jogador clicar no "X" então a janela do jogo é fechada
            jogando = False #clicando no "X" a variavel jogando virá FALSE

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                velocidadeX = velocidade_padrao
            elif evento.key == pygame.K_RIGHT:
                velocidade_x = velocidade_padrao
            elif evento.key == pygame.K_UP:
                velocidade_y = velocidade_padrao
            elif evento.key == pygame.K_DOWN:
                velocidade_y = velocidade_padrao