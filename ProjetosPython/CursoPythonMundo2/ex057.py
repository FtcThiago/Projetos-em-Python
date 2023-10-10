'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.'''


sexo = str

while sexo != 'M' and 'F' : # enquanto o usuário não digitar entre as duas opções, ele vai ficar em um loop infinito
    sexo = input('Arca:Informe seu sexo:'
                 '\n[M] Masculino'
                 '\n[F] Feminino'
                 '\nDigite:').strip().upper()[0] #O strip() retira os espaços digitados no inicio(importante, para caso o usuário digite um espaço sem querer no inicio,o espaço será desconsiderado e não ira atrapalhar) o upper deixa a string em maiúsculo;esse [0], está dizendo que vai pegar somente a primeira letra, ou seja, se eu escrever masculino, o programa vai considerar certo,pois a primeira letra é m....sem esse comando, o programa não consideraria certo ;
    if sexo != 'M' and 'F': # caso o usuário digite errado, esse comando de if vai avisa-lo
        print('Arca:Digitação inválida')
        print('---------------------')
print('Arca:Obrigado pela informação!')