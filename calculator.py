def addition():
	first= int(input('I will add two numbers. Enter the first number \n'))
	second= int(input('Now enter the second number. \n'))
	print(first + second)
    
def subtraction():
	first= int(input('I will subtract two numbers. Enter the first number \n'))
	second= int(input('Now enter the second number. \n'))
	print(first - second)

def multiplication():
	first= int(input('I will multiply two numbers. Enter the first number \n'))
	second= int(input('Now enter the second number. \n'))
	print(first * second)
	
def division():
	first= int(input('I will divide two numbers. Enter the first number \n'))
	second= int(input('Now enter the second number. \n'))
	print(first / second)
    
def modulo():
	first= int(input('I will modulo two numbers. Enter the first number \n'))
	second= int(input('Now enter the second number. \n'))
	print(first % second)


def calc_run():
	op = input('add, subtract, multiply, divide, or modulo? \n')
	if op =='add':
		addition()
	elif op == 'subtract':
		subtraction()
	elif op == 'multiply':
		multiplication()
	elif op == 'divide':
		division()
	elif op == 'modulo':
		modulo()
calc_run()