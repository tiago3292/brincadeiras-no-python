#Coleta inputs e adicionam eles em uma lista vazia
x = []
print('Insira um nome:')
x.append(input().capitalize())
print('Agora o nome de algum carro:')
x.append(input())
print('Por último, sua comida favorita:')
x.append(input())

#História com os inputs informados
print(x[0] + ''' Acordou às 6 da manhã para o seu primeiro dia trabalhando
na área de programação. Depois do café da manhã, ''' + x[0] + ''' entrou
em seu ''' + x[1] + ''' e dirigiu até a empresa. Depois de um ótimo dia
de trabalho, ''' + x[0] + ''' se presentou com um pouco de ''' + x[2] + '.')
