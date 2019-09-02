# first_module.py
def add(x, y):
	print('Add')
	print('x = {}'.format(x))
	c = x + y
	print('{} + {} = {}'.format(x, y, c))
	return

def subtract():
	print('Subtract')
	a = 1
	b = 2
	c = a - b
	print('{} - {} = {}'.format(a, b, c))
	return

def addsubtract(x, y, symbol):
	if symbol == '+':
		c = x + y
	elif symbol == '-':
		c = x - y
	else:
		c = 'Unrecognized'
	return c

if __name__ == "__main__":
	x = input('Input a command: ')
	print('You entered {}.'.format(x)) # this puts x in the bracket with a certain format
	a = input('a = ')
	b = input('b = ')
	if x == 'add' or x == 'a':
		symbol = '+'
		answer = addsubtract(int(a), int(b), symbol)
	elif x == 's':
		symbol = '-'
		answer = addsubtract(int(a), int(b), symbol)
	else:
		print('{} not recognized'.format(x))
		print('Enter a new command: ')
	print('c = {}'.format(answer))
	print('Done')
