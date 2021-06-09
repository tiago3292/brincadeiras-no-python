import random

#Função 'rolarDados' avalia se input foi numérico e imprime uma quantidade
#de números randomicos de 1 a 6 de acordo com o input.

def rolarDados(x):    
    if x.isdecimal():
        val = [random.randrange(1,6) for i in range(int(x))]
        print(val)
    else:
        rolarDados(x=input('Você precisa inserir um número:\n'))

#Função interna 'deNovo' pergunta se a pessoa que rolar os dados novamente.
#Se sim, reexecuta rolarDados. Se não, encerra o programa.
#Se a resposta foi inválida (nem 'y', nem 'n') ela pede uma nova resposta.

    y = input('Rolar dados novamente? (y/n):\n')
    def deNovo(y):
        if y.lower() == 'y':
            rolarDados(x)
        elif y.lower() == 'n':
            return
        else:
            deNovo(y = input('Resposta precisa ser (y)sim ou (n)não:\n'))
    deNovo(y)

print('Insira o número de dados que quer rolar: ')
rolarDados(x = input())
