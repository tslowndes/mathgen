import random
from decimal import Decimal
import numpy as np
def mental_addition():
    a = random.choice([100 - random.randint(1,3), 100 + random.randint(1,3)])
    b = random.randint(150,250)
    if random.randint(0,1) == 0:
        q = '$' + str(b) + ' + ' + str(a) + '$'
        ans = b + a
    else:
        q = '$' + str(b) + ' - ' + str(a) + '$'
        ans = b - a

    return q, ans

def addition():
    a = round(random.random(),random.randint(2,4))
    b = round(random.random(),random.randint(2,4))

    q = '$' + str(a) + ' + ' + str(b) + '$'
    ans = a + b

    return q, ans

def gen_mental_addition(n,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q,a = mental_addition()
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}

def mental_multiple_of_10s(max_2):
    a = random.randint(2,9) * random.choice([10,100])
    b = random.randint(2,5) * random.choice([1,max_2])

    return '$' + str(a) + r'\times' + str(b) + '$', a*b

def gen_mental_multiplication(n,b,c,d,e,f):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q,a = mental_multiple_of_10s(10)
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}

def gen_addition(n,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q,a = addition()
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}

def multiply_decimals():
    a = round(random.random(), 1)
    b = round(random.random(), 2)

    q = '$' + str(a) + r'\times' + str(b) + '$'
    ans = round(Decimal(a) * Decimal(b), 3)
    return q,ans
