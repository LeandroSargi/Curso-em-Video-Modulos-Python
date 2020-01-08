#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar()
#diminuir(), dobro() a metade(). Faça também um programa que importe esse
#módulo e use algumas destas funções.
import moeda

#Programa Principal
din = float(input('Digite o valor do produto:  '))
moeda.resumo(din, 80, 35)
#print(f'O valor de R${din} com acréscimo de 10% é {moeda.aumentar(din, 10, formata=True)}')
#print(f'O valor de R${din} com desconto de 20% é {moeda.diminuir(din, 20)}')
#print(f'O dobro do valor R${din} é {moeda.dobro(din)}')
#print(f'A metade do valor R${din} é {moeda.metade(din, formata=True)}')

