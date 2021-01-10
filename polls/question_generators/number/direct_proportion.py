import random
# -*- coding: utf-8 -*-

def simple_direct_proportion():
	pass

def gen_currency_conversion(a1,a2,a3,a4,a5,a6):
	questions = []
	answers = []
	count = [i for i in range(0,10)]

	for n in range(0,10):
		q, a = currency_conversion()
		questions.append(q)
		answers.append(a)

	return {'questions':questions, 'answers':answers, 'count':count}



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