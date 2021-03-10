import random
from polls.question_generators.tools import *
from math import gcd

def lcm(a, b):
	return abs(a * b) // gcd(a, b)

def adding_fractions(same_denom=0, unit=0, negative = 0):

	subtract = random.randint(0,1)

	if same_denom == 0:
		d1 = random.randint(2,8)
		d2 = random.randint(d1,10)
		while d1 == d2:
			d2 = random.randint(d1, 10)
	else:
		d1 = random.randint(3,10)
		d2 = d1

	if unit == 0:
		n1 = random.randint(1, d1-1)
		n2 = random.randint(1, d2-1)
		if n1 == n2:
			if n2 - 1 > 0:
				n2 = n2 - 1
			elif n1 + 1 < d1:
				n1 = n1 + 1
	else:
		n1, n2 = 1,1

	if negative == 0:
		if n2/d2 > n1/d1:
			n1,n2 = n2,n1
			d1,d2 = d2,d1



	if subtract == 0:
		question = r'$\frac{' + str(n1) + '}{' + str(d1) + r'} + \frac{' + str(n2) + '}{' + str(d2) + '}$'
	else:
		question = r'$\frac{' + str(n1) + '}{' + str(d1) + r'} - \frac{' + str(n2) + '}{' + str(d2) + '}$'

	com_d = lcm(d1,d2)

	d3 = com_d
	if subtract == 0:
		n3 = int(n1 * (com_d/d1)) + int(n2 * (com_d/d2))
	else:
		n3 = int(n1 * (com_d / d1)) - int(n2 * (com_d / d2))

	n4, d4 = simplify_frac(abs(n3), d3)

	n4, d4 = str(n4), str(d4)
	if str(n4)[0] != '0':
		n4 = str(n4).strip('0')
		d4 = str(d4).strip('0')
	else:
		n4 = n4[:-2]
		d4 = d4[:-2]

	print(n4)

	if n4[-1] == '.':
		n4 = n4[:-1]
	if d4[-1] == '.':
		d4 = d4[:-1]
	n3 = int(n3)
	n4 = int(n4)
	if n3 == d3:
		answer = r'$\frac{' + str(n3) + '}{' + str(d3) + r'} = 1 $'
	else:
		if n3 == n4:
			if n3 > 0:
				answer = r'$\frac{' + str(n3) + '}{' + str(d3) + '}$'
			elif n3 == 0:
				answer = r'$0$'
			else:
				answer = r'$-\frac{' + str(abs(n3)) + '}{' + str(d3) + '}$'
		else:
			if n3 > 0:
				answer = r'$\frac{' + str(n3) + '}{' + str(d3) + r'} = \frac{' + str(n4) + '}{' + str(d4) + '}$'
			else:
				answer = r'$-\frac{' + str(abs(n3)) + '}{' + str(d3) + r'} = -\frac{' + str(abs(n4)) + '}{' + str(d4) + '}$'

	return question, answer

def gen_adding_fractions(n=10,same_denom=0,unit=0,d=0,e=0,f=0):
	qs = []
	ans = []
	for i in range(n):
		q, a = adding_fractions(same_denom, unit)

		qs.append(q)
		ans.append(a)

	return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': ans}

def multiplying_fractions():
	d1 = random.randint(2,8)
	d2 = random.randint(2,8)
	n1 = random.randint(1,d1-1)
	n2 = random.randint(1,d2-1)

	d3 = d1 * d2
	n3 = n1 * n2

	n4, d4 = simplify_frac(n3, d3)
	n4 = str(n4).strip('0')
	d4 = str(d4).strip('0')
	if n4[-1] == '.':
		n4 = n4[:-1]
	if d4[-1] == '.':
		d4 = d4[:-1]
	n3 = int(n3)
	n4 = int(n4)

	question = r'$\frac{' + str(n1) + '}{' + str(d1) + r'}\times\frac{' + str(n2) + '}{' + str(d2) + '}$'
	if n3 == n4:
		answer = r'$\frac{' + str(n3) + '}{' + str(d3) + '}$'
	else:
		answer = r'$\frac{' + str(n3) + '}{' + str(d3) + r'} = \frac{' + str(n4) + '}{' + str(d4) + '}$'

	return question, answer

def multiplying_fraction_by_integer():
	d1 = 1
	d2 = random.randint(2,8)
	n1 = random.randint(2,5)
	n2 = random.randint(1,d2-1)

	d3 = d1 * d2
	n3 = n1 * n2

	n4, d4 = simplify_frac(n3, d3)
	n4 = str(n4).strip('0')
	d4 = str(d4).strip('0')

	if n4[-1] == '.':
		n4 = n4[:-1]
	if d4[-1] == '.':
		d4 = d4[:-1]
		
	n3 = int(n3)
	n4 = int(n4)

	question = '$' + str(n1) + r'\times\frac{' + str(n2) + '}{' + str(d2) + '}$'

	if n3 == n4:
		answer = r'$\frac{' + str(n3) + '}{' + str(d3) + '}$'
	else:
		answer = r'$\frac{' + str(n3) + '}{' + str(d3) + r'} = \frac{' + str(n4) + '}{' + str(d4) + '}$'

	return question, answer

def dividing_fractions():
	d1 = random.randint(2,6)
	d2 = random.randint(2,6)
	n1 = random.randint(1,d1-1)
	n2 = random.randint(1,d2-1)

	d3 = d1 * n2
	n3 = n1 * d2

	n4, d4 = simplify_frac(n3, d3)
	n4 = str(n4).strip('0')
	d4 = str(d4).strip('0')
	if n4[-1] == '.':
		n4 = n4[:-1]
	if d4[-1] == '.':
		d4 = d4[:-1]


	question = r'$\frac{' + str(n1) + '}{' + str(d1) + r'}\div\frac{' + str(n2) + '}{' + str(d2) + '}$'
	if n3 == n4:
		answer = r'$\frac{' + str(n3) + '}{' + str(d3) + '}$'
	else:
		answer = r'$\frac{' + str(n3) + '}{' + str(d3) + r'} = \frac{' + str(n4) + '}{' + str(d4) + '}$'

	return question, answer

def fraction_of_an_amount(unit, reverse=0, apply = 0):
	if unit == 1:
		d = random.randint(2,12)
		n = 1
	else:
		d = random.randint(3,12)
		n = random.randint(2, d - 1)

	part = random.randint(2,10)
	amount = d * part
	ans = n * part
	if apply == 0:
		if reverse == 0:

			q = r'$\frac{' + str(n) + '}{' + str(d) + '}\;\; of\;\; ' + str(amount) + '$'

		else:

			q = r'$\frac{' + str(n) + '}{' + str(d) + '}\;\; of\;\; x = ' + str(ans) + '$'
			ans = amount
	else:
		q = 'Bill and Ben share the profits of their business. Bens share of the profits is ' + r'$\frac{' + str(n) + '}{' + str(d) + '}$. Ben gets ' + str(ans) + '. How much profit did they make?'
		ans = amount


	return q,ans

def gen_fraction_of_an_amount(n,unit,reverse=0,d=0,e=0,f=0):
	qs = []
	ans = []
	for i in range(n):

		q,a = fraction_of_an_amount(unit, reverse)
		#q,a = fraction_of_an_amount(unit, reverse, 1)
		qs.append(q)
		ans.append(a)

	return {'count': [i for i in range(0,n)], 'questions': qs, 'answers': ans}