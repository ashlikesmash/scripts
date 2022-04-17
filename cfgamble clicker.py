import random, time, console, math, Image

cash = 0
multiplier = 1
autobuy = 'false'
arg = input(' ')

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quantrillion'][magnitude])
  
while arg != 'clear':
	if autobuy == 'true':
		if cash > 999:
			price = math.floor(cash / 1000) * 1000
			amount = price / 1000
			multiplier = multiplier + amount
			cash = cash - price
		
			
			
	if arg == '':
		cash = cash + multiplier
	print(f'''cash: {human_format(cash)}   
multiplier: {multiplier}    autobuy: {autobuy}''')
	arg = input(' ')
	console.clear()
	
	if arg == 'cf':
		print(f'cash: {cash}')
		amount = int(input('amount: '))
		if amount < (cash + 1):
			headstails = input('heads or tails (h/t)')
			cf = random.randint(1, 2)
			if cf == 2:
				if headstails[0] == 'h':
					print('it landed on heads')
				else: print('it landed on tails')
				cash = cash + amount
				print(f'you won {amount} dollars')
			else: 
				if headstails[0] == 'h':
					print('it landed on tails')
				else: print('it landed on heads')
				cash = cash - amount
				print(f'you lost {amount} dollars')
		else: print('not enough cash')
	
	if 'mult' in arg:
		print(f'you have {cash} dollars')
		multiamount = int(input('how many multipliers? '))
		multiprice = multiamount * 1000
		yesno = input(f'buy {multiamount} multipliers for {multiprice} dollars? (y/n)')
		if yesno == 'y':
			if cash > multiprice:
				multiplier = multiplier + multiamount
				cash = cash - multiprice
			else: print('not enough cash')
		else: print('cancelled')

	if arg == 'admintesting':
		admintest = int(input('amount: '))
		cash = cash + admintest
	if arg == 'adminmul':
		multiplier = int(input('amount: '))
	
	if arg == 'autobuy':
		autobuy = 'true'
	
	if arg == 'autobuydisable':
		autobuy = 'false'
		
	if arg == 'cmds':
		print(
'''
- autobuy: automatically buys multipliers when you have more than 1k
- autobuydisable: disables autobuy
- cf: (coinflip), choose how much cash, choose heads or tails, 50/50 chance of winning
- multiplier: choose how many multipliers you want to buy
- admintesting/adminmul: cheats
''')
