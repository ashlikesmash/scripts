import time, console

number = int(input('number: '))
amount = 0
highest = number
original = number

while number:
	if number % 2 == 0:
		number = number / 2
	else: number = number * 3 + 1
	if number > highest:
		highest = number
	amount = amount + 1
	numberstr = str(number)
	print(numberstr.replace('.0', ''))
	if number == 1:
		number = int(input(f'''4,2,1 etc. | {original} went on for {amount} numbers | highest number: {highest}
'''))
		print(' ')
		original = number
		
	time.sleep(0.1)
