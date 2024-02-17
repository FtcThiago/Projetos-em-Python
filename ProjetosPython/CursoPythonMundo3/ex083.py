""" Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
fechados na ordem correta"""

#Esse e não consegui fazer sem o olhar antes o do professor

exres = str(input('Arca:Digite a expressão:'))
pilha = []

for simb in exres:

    if simb == '(': #Se ele encotrar um parentêses ele vai colocar na lista
        pilha.append(simb)
    elif simb == ')': # Se ele encontrar um parentêses fechando ele vai tirar o que foi colocado, e assim saberemos que temos dois parentêses que se completam
        if len(pilha) > 0:# Condição para saber se tem algo na lista, ou seja, se colocaram o primeiro parentesês ele foi colocado na lista, então se digitaram o outro parentêses de fechamento o programa manda para essa condição e ai com o pop() nós zeramosa lista
            pilha.pop()
        else:
            pilha.append(')')#Se não houver o fechamento do parentêses, vai ficar sonbrando algo dentro da lista, e esse vai ser o que nos mostrará que a expressão está errada

print('-='*60)
if len(pilha) > 0: #Se a algo dentro da lista, então em algum momento o usuário esqueceu algum parentêses
    print('Arca:Sua expressão está errada!')
else:# Senão, ou seja, se a lista está vazia, significa que o usuário não esqueceu nenhum parentêses
    print('Arca:Sua expressão está Correta!')
