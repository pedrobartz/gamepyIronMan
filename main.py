import pygame, random
from sys import exit


pygame.init()
tela = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Iron man do pedro")
branco = (255,255,255)
preto = (0,0,0)
iron = pygame.image.load("assets/iron.png")
fundo = pygame.image.load("assets/fundo.png")
missel = pygame.image.load("assets/missile.png")
posicaoXPersona = 400
posicaoYPersona = 300
movimentoXpersona = 0
movimentoYpersona = 0
posicaoXMissel = 400
posicaoYMissel = -300
velocidadeMissel = 2
pontos = 0
larguraPersona = 250
alturaPersona = 127 
larguraMissel= 50
alturaMissel = 250
dificuldade = 10

fonte = pygame.font.SysFont("comicsans",14)
fontemorte = pygame.font.SysFont('arial', 20)

misselsound= pygame.mixer.Sound("assets/missile.wav")
pygame.mixer.Sound.play(misselsound)

pygame.mixer.music.load("assets/ironsound.mp3")
pygame.mixer.music.play(+1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            movimentoXpersona = 3
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            movimentoXpersona = -3
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            movimentoXpersona = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            movimentoXpersona = 0
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            movimentoYpersona = -3
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            movimentoYpersona = 3
        elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
            movimentoYpersona = 0
        elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            movimentoYpersona = 0

    posicaoYPersona = posicaoYPersona + movimentoYpersona
    posicaoXPersona = posicaoXPersona + movimentoXpersona

    if posicaoXPersona < 0:
        posicaoXPersona = 0
    elif posicaoXPersona > 550:
        posicaoXPersona = 550
    
    if posicaoYPersona < 0:
        posicaoYPersona = 0
    elif posicaoYPersona > 473:
        posicaoYPersona = 473

    
    ##missel
    posicaoYMissel = posicaoYMissel +velocidadeMissel
    if posicaoYMissel > 600:
        posicaoYMissel = -200
        pontos = pontos =pontos +1
        velocidadeMissel =velocidadeMissel+1
        posicaoXMissel = random.randint(0,800)
        pygame.mixer.Sound.play(misselsound)


  
    tela.fill(branco)
    tela.blit(fundo,(0,0))
    tela.blit (missel, (posicaoXMissel,posicaoYMissel))
    tela.blit(iron, (posicaoXPersona, posicaoYPersona))
    pontosmostrar = fonte.render(('pontos: ')+str(pontos),True,branco)
    tela.blit(pontosmostrar, (10,10))
    texto = fonte.render(str(posicaoXPersona)+"-"+str(posicaoYPersona), True, preto)
    tela.blit(texto, (posicaoXPersona+95,posicaoYPersona-15))


    pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
    pixelsPersonaY = list(range(posicaoYPersona,posicaoYPersona+alturaPersona))

    pixelsMisselX = list(range(posicaoXMissel, posicaoXMissel+larguraMissel))
    pixelsMisselY = list(range(posicaoYMissel, posicaoYMissel+alturaMissel))

    if len (list(set(pixelsMisselY).intersection(set(pixelsPersonaY)))) > dificuldade:
        if len (list(set(pixelsMisselX).intersection(set(pixelsPersonaX)))) > dificuldade:
            textomorte = fontemorte.render(("MORREU"),True,preto)
            tela.blit(textomorte,(200,200))
             






    pygame.display.update()
    clock.tick(60)