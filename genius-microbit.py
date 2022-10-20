from microbit import *
import random

sequencia = []
movimentos = []

def iniciar_jogo():
    while not (button_a.is_pressed() and button_b.is_pressed()):
        display.show(Image.DIAMOND)
        sleep(1200)
        return

def sortear_jogada():
    possibilidades = ['direita', 'esquerda']
    sequencia.append(random.choice(possibilidades))

def exibir_sequencia():
    for jogada in sequencia:
        if jogada == 'direita':
            display.show(Image.ARROW_E)
        elif jogada == 'esquerda':
            display.show(Image.ARROW_W)
        sleep(500)
        display.clear()
        sleep(100)
    sleep(800)

def salvar_movimentos():
    movimento = ''
    
    while len(movimentos) < len(sequencia):
        if button_a.was_pressed():
            movimento = 'esquerda'
        elif button_b.was_pressed():
            movimento = 'direita'

        if movimento:
            posicao = len(movimentos)
            movimentos.append(movimento)
            if sequencia[posicao] != movimento:
                break
            movimento = ''

def verificar_erros():
    if movimentos != sequencia:
        display.show(Image.SAD)
        sleep(1500)
        sequencia.clear()
        movimentos.clear()
        return True
    display.show(Image.HAPPY)
    sleep(400)
    movimentos.clear()
    return False

iniciar_jogo()
while True:
    sortear_jogada()
    exibir_sequencia()
    salvar_movimentos()
    game_over = verificar_erros()
    if game_over:
        iniciar_jogo()
