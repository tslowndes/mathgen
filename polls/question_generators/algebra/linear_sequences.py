import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *
from math import abs

def gen_find_the_next_term(a1,a2,a3,a4,a5,a6):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(10):
        if i < 2:
            q, a = find_the_next_term(0, 0)
        elif i < 6:
            q,a = find_the_next_term(random.randint(0,1),0)
        else:
            q,a = find_the_next_term(random.randint(0,1),random.randint(0,1))
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def find_the_next_term(add_or_subtract, neg_first_term, a3=0, a4=0, a5=0, a6=0):
    if neg_first_term == 1:
        first_term = random.randint(-20,-1)
    else:
        first_term = random.randint(1, 20)

    common_difference = random.randint(2, 15)
    if add_or_subtract == 1:
        common_difference = common_difference * -1
    terms = ''
    for i in range(0,5):
        if i != 0:
            terms = terms + ', ' + str(first_term + i * common_difference)
        else:
            terms = terms + str(first_term + i * common_difference)
    answer = first_term + 5 * common_difference

    return terms, answer

def generate_from_words(min_first_term, negs, lang):
    first_term = random.randint(min_first_term,10)
    common_difference = random.randint(-10,10)

    if negs == 0:
        first_term = first_term + 5 * abs(common_difference)


    if lang == 0:
        if common_difference < 0:
            q = 'The first term is ' + str(first_term) + '. Subtract ' + str(abs(common_difference)) + ' to find the next term.'
        else:
            q = 'The first term is ' + str(first_term) + '. Add ' + str(abs(common_difference)) + ' to find the next term.'
    else:
        q = 'The first term is ' + str(first_term) + ' and the common difference is ' + str(common_difference) + '.'

    ans = str(first_term) + ', ' + str(first_term + 1*common_difference) + ', ' + str(first_term + 2*common_difference)+ ', ' + str(first_term + 3*common_difference)+ ', ' + str(first_term + 4*common_difference)

    return q,ans

def gen_generate_from_words(n,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(10):
        if i < 2:
            q, a = generate_from_words(3,0,0)
        elif i < 4:
            q,a = generate_from_words(3,1,1)
        else:
            q,a = generate_from_words(-10,1,1)

        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}


