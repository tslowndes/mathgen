import random
import string 
def fair_dice():
	choice = random.randint(0,2)
	outcomes = [1,2,3,4,5,6]
	den = 6

	if choice == 0:
		value = random.randint(2,6)
		in_values = [o for o in outcomes if o < value]
		num = len(in_values)
		question = 'What is the probability of rolling a number less than ' + str(value) + ' on a fair, 6 sided dice?'

	elif choice == 1:
		value = random.randint(1,5)
		in_values = [o for o in outcomes if o > value]
		num = len(in_values)
		question = 'What is the probability of rolling a number greater than ' + str(value) + ' on a fair, 6 sided dice?'
	else:
		value = random.randint(1,5)
		in_values = [o for o in outcomes if o == value]
		num = len(in_values)
		question = 'What is the probability of rolling a ' + str(value) + ' on a fair, 6 sided dice?'
	answer = r'$\frac{' + str(num) + '}{' + str(den) + '}$'

	return question, answer

def spinner():
	sides = random.randint(3,8)
	outcomes = [random.choice('abcde') for i in range(sides)]
	choice = random.choice(outcomes)

	den = len(outcomes)

	num = len([out for out in outcomes if out == choice])

	question = 'A fair spinner is labelled with the letters:\n '
	for out in outcomes:
		question = question + ' ' + str(out)
	question = question + '\n What is the probability the spinner lands on an ' + choice + '?'

	answer = r'$\frac{' + str(num) + '}{' + str(den) + '}$'

	return question, answer