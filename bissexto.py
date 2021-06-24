print('Insira o ano que deseja conferir:')

def eval(ano = input()):
	
	def repeat(): #repete o programa se a pessoa quiser conferir outro ano
		print('Gostaria de conferir outro ano? (S / N)')
		again = input()
		
		if again.lower() == 's':
			eval(ano = input('Insira o ano que deseja conferir:\n'))
		elif again.lower() == 'n':
			return
		else:
			print('Insira S para SIM e N para NÃO:')
			repeat()
	
	try:
		if int(ano) % 4 == 0 and int(ano) % 100 > 0: #se o ano for múltiplo de 4 mas não de 100
			print('O ano ' + ano + ' é um ano bissexto.')
			repeat()

		elif int(ano) % 4 + int(ano) % 100 + int(ano) % 400 == 0: #se o ano for múltiplo de 4, 100 e 400
			print('O ano ' + ano + ' é um ano bissexto.')
			repeat()

		else:
			print('O ano ' + ano + ' não é um ano bissexto.')
			repeat()

	except ValueError:
		eval(ano = input('Insira apenas números:\n'))
eval()