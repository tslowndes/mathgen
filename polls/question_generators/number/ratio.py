import random
from polls.question_generators.tools import *

def gen_sharing_into_ratio(n,total_value_difference,c,d,e,f):
    questions = []
    answers = []
    count = [i for i in range(n)]
    for i in count:
        if total_value_difference == 0:
            if i < 6:
                q, a = sharing_into_ratio(8, 6)
            else:
                q, a = sharing_into_ratio(12, 12)
        else:
            if i < 6:
                q, a = sharing_into_ratio(8, 6, total_value_difference)
            else:
                q, a = sharing_into_ratio(12, 12, total_value_difference)

        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def sharing_into_ratio(max_part, max_number, total_or_value_or_difference=0):
	### b:c where a is 1 part

	a = random.randint(2, max_part)
	b = random.randint(2, max_number)
	c = random.randint(2, max_number)
	while b == c:
		b = random.randint(2, max_number)
		c = random.randint(2, max_number)

	total = (b*a) + (c*a)
	thing = thing_chooser()
	if total_or_value_or_difference==0:
	    if random.randint(0,3) == 0:
	        question = name_chooser() + ' and ' + name_chooser() + ' share £' + str(total) + ' in the ratio ' + str(b) + ':' + str(c) + '.\n How much does each person get?'
	        answer = '£' + str(b*a) + ':£' + str(c*a)
	    else:
	        question = name_chooser() + ' and ' + name_chooser() + ' share ' + str(total) + ' ' + thing + ' in the ratio ' + str(b) + ':' + str(c) + '.\n How many ' + thing + ' does each person get?'
	        answer = str(b*a) + ' ' + thing + ' : ' + str(c*a) + ' ' + thing
	elif total_or_value_or_difference==1:
	    name1=name_chooser()
	    name2=name_chooser()
	    while name1 == name2:
	        name1=name_chooser()
	        name2=name_chooser()
	    question = 'hello'
	    answer = 'hello'
	    if random.randint(0,1)==1:
	        question = name1 + ' and ' + name2 + ' share some ' + thing + ' in the ratio ' + str(b) + ':' + str(c) + '. ' + name1 + ' gets ' + str(b*a) + ' ' + thing + '. ' + '\n How many ' + thing + ' does ' + name2 + ' get?'
	        answer = str(c * a) + ' ' + thing
	    else:
	        question = name1 + ' and ' + name2 + ' share some ' + thing + ' in the ratio ' + str(b) + ':' + str(c) + '. ' + name2 + ' gets ' + str(c*a) + ' ' + thing + '. ' + '\n How many ' + thing + ' does ' + name1 + ' get?'
	        answer = str(b*a) + ' ' + thing
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