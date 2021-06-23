import random

#Escolhe um número randômico para ser adivinhado
num = random.randrange(1, 20)

#Uma dessas dicas será escholida sempre que a resposta for incorreta
cond = ['É maior que 5' if num > 5 else 'É menor que 5',
    'É maior que 10' if num > 10 else 'É menor que 10',
    'É maior que 15' if num > 15 else 'É menor que 15',
    'É um número par' if num % 2 == 0 else 'É um número ímpar',
    'É um múltiplo de 2' if range(2, 21, 2).count(num) == 1 else 'Não é um múltiplo de 2',
    'É um múltiplo de 5' if range(5, 21, 5).count(num) == 1 else 'Não é um múltiplo de 5']

global score
score = 1000

print ('''Bem vindo(a) ao Num-guessing!
Eu escolherei um número de 1 a 20
e você tentará adivinhar qual número eu escolhi.
Primeira dica:
''' + cond[random.randint(0, 5)] + '''

Escolha um número:\n''')


def eval(guess = input()):

    try: #Roda um loop caso a resposta for errada. Se o input não for numérico, a função é reiniciada
        global score            
        while int(guess) != num:
            score = score - 150
            print('Incorreto! Aqui vai outra dica: ' + cond[random.randint(0, 5)])
            guess = input('Tente outro número:\n')
        print('\nParabéns! O número ' + str(guess) + ''' é o número correto!
Sua pontuação é de: ''' + str(score) + ' pontos.\n')
    except ValueError:
        eval(guess = input('Insira apenas números naturais (positivos)\n'))
eval()