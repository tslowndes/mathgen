import random
from polls.question_generators.tools import *
# -*- coding: utf-8 -*-

def simple_direct_proportion():
	pass

def gen_currency_conversion(a1,a2,a3,a4,a5,a6):
	questions = []
	answers = []
	count = [i for i in range(0,10)]

	for n in range(0,10):
		q, a = currency_conversion(a1)
		questions.append(q)
		answers.append(a)

	return {'questions':questions, 'answers':answers, 'count':count}



def currency_conversion(int_or_dec):
	currency = random.choice([u'\u20AC', u'\u20B9', u'\u20B1', u'\u20AB', u'\u20A4', u'\u20BF'])
	if int_or_dec == 0:
	    exchange = random.randint(3,10)
	else:
	    exchange = round(1 + round(random.random(),2),2)

	multiplier = random.randint(3,10)

	a = strip_0(str(exchange))
	if '.' in a:
	    if len(a) == 3:
	        a = a + '0'
	else:
	    a = a + '.00'

	b = str(multiplier) + '.00'

	c = strip_0(str(round(exchange * multiplier,2)))
	if '.' in c:
	    if len(c.split('.')[1]) == 1:
	        c = c + '0'
	else:
	    c = c + '.00'

	if random.randint(0,1) == 0:
		question = '£1 = ' + currency + a + '.\n How many ' + currency + ' could you buy with £' + b + '?'
		answer = currency + c
	else:
		question = '£1 = ' + currency + a + '.\n How many £ could you buy with ' + currency + c + '?'

		answer = '£' + b

	return question, answer