#DESAFIO 026

#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

from unidecode import unidecode

frase = str(input('Descreva algum animal detalhadamente:')).strip().upper()
fraseSemAcent = unidecode(frase)

print(f'Arca: A descrição informada retem em si cerca de {fraseSemAcent.count("A")} letras A'
      f'\nEcontra-se na posição {fraseSemAcent.find("A")+1} a primeira letra A encontrada'# o mais um é para escolher a posição correta,levando em conta que so o find escollhe sempre uma posição a menos da correta
      f'\nEcontra-se na posição {fraseSemAcent.rfind("A")+1} a última letra A encontrada'
      f'\n{frase}')
