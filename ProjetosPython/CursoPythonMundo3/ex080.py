"""Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a
lista ordenada na tela."""


print('{:=^40}'.format('Lista ordenada sem o uso do sort()'))


# Esse solução eu achei sozinho depois de vê que o guanabara usou uma variável para receber o valor digitado pelo usuário e não simplesmente jogar o valor direto na lista

valores = list()

for c in range(0,5):
    n = int(input(f'Arca:Informe o {c}° valor:'))

    if c == 0 or n > valores[len(valores)-1]:
        valores.append(n)
        print(valores)
    elif n < valores[0]:
        valores.insert(0,n)
        print(valores)
    elif len(valores) >= 2 :
        if n < valores[1]:
            valores.insert(1,n)
            print(valores)
        elif len(valores) >= 3:
            if n < valores[2]:
                valores.insert(2,n)
                print(valores)
        elif len(valores) >= 4:
            if n < valores[3]:
                valores.insert(3,n)
                print(valores)
        elif len(valores) >= 5:
            if n < valores[4]:
                valores.insert(4,n)
                print(valores)


print('-='*60)
print(valores)





#Primeiro solução que achei antes da de cima! Essa tem alguns erro, que se eu digitar certos numeros ,dependendo da sequencia deles, a solução final sai errado
# valores = novaLista = list()
#
#
# for cont in range(0,5):
#     valores.append(int(input(f'Arca:Informe o {cont}° número:')))
#
#
#     if cont == 0 :
#         print('Arca:Adicionado ao final da lista!')
#
#     if valores[cont] < valores[0]: #Se o número digitado for menor que o valor na posição zero
#         print('Adicionado a posição zero')
#         valores.insert(0, valores[cont])#Ele será adicionado  na posição zero
#         valores.pop() # eu tenho que apagar o valor na ultima posição, pois eu dupliquei esse valor com insert e o
#                       # mandei para a posição zero, logo, tenho que apagar esse valor na ultima posição para não
#                       # ficar dois valores iguais.
#
#
#
#     if [2] in valores: # Condição para vê se existe a posição dois na lista! Se sim, ela entra na condição.
#      if valores[cont] < valores[2]: # Condição para vê se o número digitado é menor que o valor que está na posição 2
#         valores.insert(valores.index(valores[2]),valores[cont]) #inserindo  o valor digitado na posição 2, isto é , valores.insert(2,valores[cont]) ; o index acha a posição está sendo usado para achar a posição 2
#         valores.pop()
#
#     if [1] in valores:
#         if valores[cont] < valores[1]:
#             valores.insert(valores.index(valores[1]),valores[cont])
#             valores.pop()
#     if valores[cont] < valores[valores.index(max(valores))]:
#         valores.insert(valores.index(max(valores)), valores[cont])
#         valores.pop()
#
# print(valores)
#














#Testes falhos em baixo


    # if cont != 0:
    #
    #     for c in range(0,5):
    #         if valores[1] < valores[0]:
    #             valores.insert(valores.index(valores[0]),valores[1])
    #             valores.pop()
    #             print(valores)
    #         if len(valores) == 3:
    #             if valores[2] < valores[0]:
    #                 valores.insert(valores.index(valores[0]), valores[2])
    #                 valores.pop()
    #                 print(valores)
    #         if len(valores) == 4:
    #             if valores[3] < valores[0]:
    #                 valores.insert(valores.index(valores[0]), valores[3])
    #                 valores.pop()
    #                 print(valores)
    #         if len(valores) == 5:
    #             if valores[4] < valores[0]:
    #                 valores.insert(valores.index(valores[0]),valores[4])
    #                 valores.pop()
    #                 print(valores)



# print(novaLista)
#
# if cont == 5:
#     for pos, c in enumerate(valores):
#
#         for conta in range(0, 5):
#             if valores[pos] <= valores[conta]:
#                 novaLista[pos] = valores[pos]
#             else:
#                 novaLista[pos] = valores[conta]
#         if pos == 5:
#             break









