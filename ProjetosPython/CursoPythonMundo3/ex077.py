"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""


print('{:=^40}'.format('As vogais Das Palavras'))


palavras = ('Computador'.upper(), ' Python'.upper(), 'Camiseta'.upper(), 'Video Game'.upper(), 'Cordao'.upper(),
             'Vendedor', 'Camaro'.upper(), 'Filmes'.upper(), 'Animes'.upper(),' Paralelepipedo'.upper())






for c in palavras:
    a = c.count('A')
    e = c.count('E')
    i = c.count('I')
    o = c.count('O')
    u = c.count('U')


    print(f'\nArca: Na palavra {c} temos as vogais: ', end='')

    if a > 0:
        print('a '*a, end='')
    if e > 0:
        print('e '*e, end='')
    if i > 0:
        print('i '*i, end='')
    if o > 0:
        print('o '*o, end='')
    if u > 0:
        print('u '*u, end='')




#Modo do professor guanabara:
print('\n')
print('='*40)
print('{:=^40}'.format('Modo do Guanabara'))
print('='*40)

for p in palavras:#com essa condição conseguiremos passar por todos os valores da tupla.
    print(f'\nArca: Na palavra {p} temos as vogais:', end='')
    for letra in p:# com essa condição, vamos analisar cada letra referente as valores dentro da tupla.
        if letra.lower() in 'aeiou':# com essa condição, vamos analisar se essas letras são vogais; o lower() é para deixar as letras minusculas.
            print(f' {letra.lower()} ', end='')



