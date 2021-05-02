def saludo(func):
	func()
def llegada():
	print('¡Hola!')
def despedida():
	print('¡Chao!')
saludo(llegada)
saludo(despedida)