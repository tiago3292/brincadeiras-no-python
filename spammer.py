from pynput.keyboard import Key, Controller
import time

frase = 'Insira a frase' #frase que será spammada

x = frase.split() #transforma frase em lista de palavras

keyboard = Controller()

time.sleep(1)#delay antes do programa iniciar. clique na area desejada antes do tempo acabar
for i in x:#aperta enter para cada palavra escrita
	time.sleep(0.8)#intervalo entre palavras
	keyboard.type(str(i))
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)