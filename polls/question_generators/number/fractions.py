import random
from polls.question_generators.tools import *

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


	question = r'$\frac{' + str(n1) + '}{' + str(d1) + r'}\times\frac{' + str(n2) + '}{' + str(d2) + '}$'
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