import random
from polls.question_generators.tools import *

def sharing_into_ratio(max_part, max_number):
	### b:c where a is 1 part

	a = random.randint(2, max_part)
	b = random.randint(2, max_number)
	c = random.randint(2, max_number)
	while b == c:
		b = random.randint(2, max_number)
		c = random.randint(2, max_number)


	total = (b*a) + (c*a)

	question = name_chooser() + ' and ' + name_chooser() + ' share £' + str(total) + ' in the ratio ' + str(b) + ':' + str(c) + '.\n How much does each person get?'
	answer = '£' + str(b*a) + ':£' + str(c*a)
	return question, answer


def simplify_ratio():
	simplifiedL = random.randint(1,12)
	simplifiedR = random.randint(1,12)

	multiplier = random.randint(2,7)

	starterL = simplifiedL * multiplier
	starterR = simplifiedR * multiplier

	answer = str(simplifiedL) + ':' + str(simplifiedR)
	question = str(starterL) + ':' + str(starterR)

	return question, answer