print('DESAFIO 007')

#Variáveis
n1 = float(input('Digite a primeria nota:'))
n2 = float(input('Digite a segunda nota:'))
média = (n1+n2)/2 #pode usar acento em váriaveis



#corpo
print('\033[4;30m--Notas e Média do Aluno--\033[m')
print("\033[4;36mNota 1:{}\033[m"
      "\n\033[4;36m Nota 2:{}\033[m"
      "\n\033[4;36m Média:{:.1f}\033[m".format(n1, n2, média))
