#DESAFIO 021


import pygame # Arca:Importando módulo pygame( que serve para criar jogos, e jogos tem músicas e consequentemente consegue  rodar audios .mp3 e .wav(e outros provavelmente))
pygame.init() # primeira coisa a ser feita é iniciar o pygame

pygame.mixer.music.load('Desacostumar.mp3') #Aqui ele vai puxar a música
pygame.mixer.music.play() #Aqui ele vai dar play na música
input()
pygame.event.wait() # Aqui ele vai esperar o evento(event) acabar para terminar o programa, isto é, parar de tocar música


