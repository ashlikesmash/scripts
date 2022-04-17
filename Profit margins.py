go = 'go'
while go != 'kill':
	num1 = float(input('num1: '))
	num2 = float(input('num2: '))
	difference = num2 - num1
	percent = difference / num1 
	percent = percent * 100
	percent = round(percent, 4)
	difference = round(difference, 2)
	if difference > 0:
		print(f'{percent}% profit | gain ${difference}')
	else: print(f'{percent}% profit | loss ${difference}')
	go = input(' ')


