import random
# -*- coding: utf-8 -*-

def simple_direct_proportion():
	pass

def currency_conversion():
	currency = random.choice([u'\u20AC', u'\u20B9', u'\u20B1', u'\u20AB', u'\u20A4', u'\u20BF'])
	exchange = random.randint(3,10)

	multiplier = random.randint(3,10)

	if random.randint(0,1) == 0:
		question = 'If £1 = ' + currency + str(exchange) + '. How many ' + currency + ' could you buy with £' + str(multiplier) + '?'
		answer = currency + str(exchange * multiplier)
	else:
		question = 'If £1 = ' + currency + str(exchange) + '. How many £ could you buy with ' + currency + str(exchange * multiplier) + '?'

		answer = '£' + str(multiplier)

	return question, answer