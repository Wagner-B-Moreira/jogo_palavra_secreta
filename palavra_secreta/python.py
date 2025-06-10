 # Jogo da palavra secreta



import os 
palavra_secreta = 'perfume'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')

    # Verifica se o usuário digitou mais de uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    # Se a letra estiver na palavra, adiciona às letras acertadas
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # Cria a palavra formada com base nas letras acertadas
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)
    os.system('clear') # limpar terminal

    # Verifica se a palavra foi completamente descoberta
    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU, PARABÉNS!')
        break  # Encerra o loop
 