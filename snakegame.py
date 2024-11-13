import pygame
import random


# Começo
pygame.init()
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption('for_snake')



# Cores do jogo
cor_fundo = (0x1e, 0x16, 0x47)
cor_botao = (0xFF, 0xFF, 0x00)
cor_cobra = (0x61, 0x4a, 0xd3)
cor_comida = (0xFF, 0xFF, 0xFF)
fonte = pygame.font.SysFont('Arial', 48)

# Imagem
imagem_titulo = pygame.image.load('titulo.png')


# Processo para fechar a janela
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Verificando Cliques
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if botao.collidepoint(x,Y):
                running = False