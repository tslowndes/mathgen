import random
from polls.question_generators.tools import *
from math import gcd

def gen_simplifying_ratio(one_to_n,b,c,d,e,f):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q, a = simplify_ratio(one_to_n)
        while q in questions:
            q, a = simplify_ratio(one_to_n)
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def gen_sharing_into_ratio(n,total_value_difference,unit_ratio,fraction,e,f):
    questions = []
    answers = []
    count = [i for i in range(n)]
    for i in count:
        if total_value_difference == 0:
            if i < 6:
                q, a = sharing_into_ratio(10, 8,0,unit_ratio,fraction)
            else:
                q, a = sharing_into_ratio(12, 12,0,unit_ratio,fraction)
        elif total_value_difference == 1:
            if i < 6:
                q, a = sharing_into_ratio(10, 8, total_value_difference,unit_ratio,fraction)
            else:
                q, a = sharing_into_ratio(12, 12, total_value_difference,unit_ratio,fraction)
        elif total_value_difference == 2:
            if i < 6:
                q, a = sharing_into_ratio(10, 8, total_value_difference,unit_ratio,fraction)
            else:
                q, a = sharing_into_ratio(12, 12, total_value_difference,unit_ratio,fraction)
        elif total_value_difference == 3:
                q, a = sharing_into_ratio(12, 12, random.randint(0,1),unit_ratio,fraction)

        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def sharing_into_ratio(max_part, max_number, total_or_value_or_difference=0, unit_ratio=0, fraction=0):
	### b:c where a is 1 part
    a = random.randint(2, max_part)
    if unit_ratio == 0:
        b = random.randint(2, max_number)
        c = random.randint(2, max_number)
    else:
        if random.randint(0,1)==0:
            b = 1
            c = random.randint(2, max_number)
        else:
            b = random.randint(2, max_number)
            c = 1

    while b == c:
        b = random.randint(2, max_number)
        c = random.randint(2, max_number)

    total = (b*a) + (c*a)
    thing = thing_chooser()
    if fraction == 0:
        if total_or_value_or_difference == 0:
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
                question = name1 + ' and ' + name2 + ' share some ' + thing + ' in the ratio ' + str(b) + ':' + str(c) + '.\n ' + name1 + ' gets ' + str(b*a) + ' ' + thing + '. ' + '\n How many ' + thing + ' does ' + name2 + ' get?'
                answer = str(c * a) + ' ' + thing
            else:
                question = name1 + ' and ' + name2 + ' share some ' + thing + ' in the ratio ' + str(b) + ':' + str(c) + '.\n ' + name2 + ' gets ' + str(c*a) + ' ' + thing + '. ' + '\n How many ' + thing + ' does ' + name1 + ' get?'
                answer = str(b*a) + ' ' + thing
                
        elif total_or_value_or_difference==2:
            name1=name_chooser()
            name2=name_chooser()
            while name1 == name2:
                name1=name_chooser()
                name2=name_chooser()
            diff1=(b-c)*a
            diff2=(c-b)*a
            if diff1>0:
                question = name1 + ' and ' + name2 + ' share some ' + thing + ' in the ratio ' + str(b) + ':' + str(c) + '.\n ' + name1 + ' gets ' + strip_0(diff1) + ' ' + thing + ' more than ' + name2 +'. ' + '\n How many ' + thing + ' does ' + name2 + ' get?'
                answer = str(c * a) + ' ' + thing
            else:
                question = name1 + ' and ' + name2 + ' share some ' + thing + ' in the ratio ' + str(b) + ':' + str(c) + '.\n ' + name2 + ' gets ' + strip_0(diff2) + ' ' + thing + ' more than ' + name1 +'. ' + '\n How many ' + thing + ' does ' + name1 + ' get?'
                answer = str(b*a) + ' ' + thing
    else:
        name1=name_chooser()
        name2=name_chooser()
        while name1 == name2:
            name1=name_chooser()
            name2=name_chooser()
        question = 'hello'
        answer = 'hello'
        if random.randint(0,1)==1:
            n,d = simplify_frac(c, b+c)
            question = name1 + ' and ' + name2 + ' share some ' + thing + ' in the ratio ' + str(b) + ':' + str(c) + '.\n What fraction does ' + name1 + ' get?'
            answer = '$' + as_fraction(c, b+c) + ' = ' + as_fraction(strip_0(n),strip_0(d)) + '$'
        else:
            n,d = simplify_frac(b, b+c)
            question = name1 + ' and ' + name2 + ' share some ' + thing + ' in the ratio ' + str(b) + ':' + str(c) + '.\n What fraction does ' + name1 + ' get?'
            answer = '$' + as_fraction(b, b+c) + ' = ' + as_fraction(strip_0(int(n)),strip_0(d)) + '$'
    return question, answer


def simplify_ratio(one_to_n):
	simplifiedL = random.randint(1,12)
	simplifiedR = random.randint(1,12)

	multiplier = random.randint(2,7)

	starterL = simplifiedL * multiplier
	starterR = simplifiedR * multiplier

	answer = strip_0(simplifiedL/gcd(simplifiedL, simplifiedR)) + ' : ' + strip_0(simplifiedR/gcd(simplifiedL, simplifiedR))
	question = str(starterL) + ' : ' + str(starterR)

	return question, answer