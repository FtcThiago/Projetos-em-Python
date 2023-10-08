"""Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

#Corrigido com ajuda do professor guanabara

frase = str(input('Arca:Escreva a frase:')).upper().replace(' ', '') # upper deixa todas as letras em maiscúlos e replace neste caso troca os espaços por nada dentro
palavras = frase.split() # separa a frase em pedaços
inverso = ''

#inverso = frase[::-1] ---->Aqui é outra forma mais simples de fazer! substituindo o for por essa linha!

for letra in range(len(frase) -1,-1,-1): # o len(frase) conta a quantidade de caracteres da frase, e o -1 é para ele começar pela ultima letra, por exemplo, se a frase tem 25 caracteres a ultima letra é o 24, já que o numero 0 na contagem é considerado, nessa ideia, temos 25 - 1 que é 24, então vamos começar do ultimo caractere, nesse caso o 24; o segundo -1 é até onde ele tem que ir, e já que ele começa do ultima caractere,ele tem que ir voltando até o primeiro caractere, que seria o zero, mas como o numero colocado é sempre desconsiderado, temos que colocar um antes do zero, nesse caso o -1; e por fim, o ultimo -1, que será como ele vai andar, nesse caso, andar de ré, sendo assim, ele vai andando de 24 até -1!
     inverso += frase[letra]
print(f'O inverso da frase {frase} é --> {inverso}')

if frase == inverso: # Se os caracteres da variável frase forem os mesmos que da variável inverso será um palíndromo , se não forem, não será!
     print('Essa frase é um Palíndromo ')
else:
     print('Esta frase não é um Palíndromo')


# for c in range(1, len(frase)+1):










