import sys

while True:
	response = input('Type exit to exit: ')
	if response == 'exit':
		sys.exit()
	print('You typed ' + response + '.')
