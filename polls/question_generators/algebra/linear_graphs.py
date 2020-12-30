import random
from polls.question_generators.tools import *
def form_equation():
	c = rand_no0(-5,5)
	m = rand_no0(-5,5)

	equation = tidy_algebra('y = ' + str(m) + 'x + ' + str(c))

	question = 'A line has a gradient of ' + str(m) + ' and a y-intercept of ' + str(c) + '.\n Write the equation of the line in the form y = mx + c.'
	answer = equation

	return question, answer

def m_and_c_from_equation():
	c = random.randint(-5,5)
	m = random.randint(-5,5)

	equation = tidy_algebra('y = ' + str(m) + 'x + ' + str(c))
	if random.randint(0,1) == 0:
		question = 'A line has the equation ' + equation + '.\n What is the gradient of the line?'
		answer = str(m)
	else:
		question = 'A line has the equation ' + equation + '.\n What is the y-intercept of the line?'
		answer = str(c)

	return question, answer

def line_on_points():
	b = random.randint(-9, 9)
	a = [random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9)]
	points = []
	if random.randint(0,1) == 1:
		points = [(b,a[0]), (b, a[1]), (b, a[2])]
		answer = 'x = ' + str(b)
	else:
		points = [(a[0],b), (a[1], b), (a[2], b)]
		answer = 'y = ' + str(b)

	question = 'The points: ' + str(points[0]) + ', ' + str(points[1]) + ' and ' + str(points[2]) + ' all lie on which line?'

	return question, answer

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



	question = 'The point (' + str(x1) + ' , ' + str(y1) + ') lies on which line? \n'

	question = question + options[0] + ', ' + options[1] + ' or ' + options[2]

	return question, answer