# basics.py
x = input('Input a command: ')
print('You entered {}.'.format(x)) # this puts x in the bracket with a certain format
if x == 'a':
	print('Add')
	a = 1
	b = 2
	c = a + b
	print('{} + {} = {}'.format(a, b, c))
elif x == 's':
	print('Subtract')
	a = 1
	b = 2
	c = a - b
	print('{} - {} = {}'.format(a, b, c))
else:
	print('{} not recognized'.format(x))
	print('Enter a new command: ')
print('Done')
