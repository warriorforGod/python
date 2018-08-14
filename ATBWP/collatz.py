def collatz(number):
  if number % 2 == 0:
	#print(str(number) + ' // 2')
   	numEven = number // 2
	return int(numEven)
  if number % 2 == 1:
	#print('3 * ' + str(number) + ' + 1')
	numOdd = 3 * number + 1   
	return int(numOdd)

while True:
	print('Enter number: ')
	parameter=int(input())
	if parameter == 1:
		break
	else:
		print parameter
