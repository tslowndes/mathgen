import random

def point_on_the_line():
	x1 = random.randint(-10,10)
	y1 = random.randint(-10,10)
	if random.randint(0,1)==1:
		answer = 'x = ' + str(x1)
	else:
		answer = 'y = ' + str(y1)
		
	if x1 != y1:
		if random.randint(0,1) == 1:
			option2 = 'x = ' + str(y1)
		else:
			option2 = 'y = ' + str(x1)
	else:
		option2 = 'x = ' + str(-1*y1)

	option3 = 'y = x'

	options = [answer, option2, option3]
	random.shuffle(options)

	if x1 == y1:
		answer = answer + ' and ' + option3



	question = 'The point (' + str(x1) + ' , ' + str(y1) + ') lie on which line? '

	for i in range(len(options)):
		if i == 2:
			question = question + ' or ' + options[i]
		else:
			question = question + options[i] + ' , '

	return question, answer