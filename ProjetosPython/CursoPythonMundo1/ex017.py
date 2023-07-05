#DESAFIO 017

#Arca:Importando módulo math
import math
from math import sqrt #Ou import math

#Váriaveis
catetoOposto = float(input('Arca:Informe o cateto oposto do triangulo:'))
catetoAdjacente = float(input('Arca:informe o cateto adjacente do triangulo:'))
hipotenusa = sqrt((pow(catetoOposto, 2) + pow(catetoAdjacente, 2))) #ou math.hypot(catetoOposto,catetoAdjacente)



print('-----------------------------------------------')
print(f'Arca: De acordo com os dados informados,temos:'
      f'\nCateto Oposto:{catetoOposto}'
      f'\nCateto Adjacente:{catetoAdjacente}'
      f'\nHipotenusa:{hipotenusa} ou  {hipotenusa:.2f}'
      f'\nisto é:  a² + b² = c²')
