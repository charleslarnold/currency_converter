import requests
from prettytable import from_csv

page = requests.get('https://api.exchangeratesapi.io/latest?base=USD')

with open("curr_codes.csv", "r") as fp: 
    x = from_csv(fp)
x.sortby =  "Currency"
print(x)

base = input('\nBase Currency Code: ')
exchange = input('Exchange Currency Code: ')

page = requests.get('https://api.exchangeratesapi.io/latest?base={}&symbols={}'.format(base.upper(), exchange.upper()))

if page.status_code == 200:
	rates = page.json()['rates']
	c = input('Amount to convert: ')
	try:
		for i in rates:
			ex = float(c) * rates[i]
			e = '{0:.2f}'.format(ex)
			print('\n{} {} = {} {}'.format(c, base.upper(), e, exchange.upper()))
			input()
	except ValueError:
		print('Invalid Exchange')
		input()
else:
	print('Invalid Exchange')
	input()
