from random import random
from polls.question_generators.tools import *

def gen_quadratic_sequences(c_n2, c_n, c_c,b,c,d):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q, a = quadratic_sequences(c_n2, c_n, c_c)
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def quadratic_sequences(c_n2, c_n, c_c):
    a = 1
    b = 0
    c = 0

    if c_n2 == 1:
        a = random.randint(2,12)

    elif c_n2 == 2:
        a = random.randint(-12,-2)

    if c_n == 1:
        b = random.randint(2,12)
        if random.randint(0,2) == 1:
            b = b * -1
    if c_c == 1:
        c = random.randint(2,12)
        if random.randint(0,1) == 1:
            c = c * -1
    q = ""
    for i in range(1,6):
        if i != 5:
            q = q + strip_0(a*i**2 + b*i + c) + ', '
        else:
            q = q + strip_0(a*i**2 + b*i + c)


    ans = "$"
    if a == 1:
        ans = ans + "n^2"
    else:
        ans = ans + str(a) + "n^2"
    if b > 0:
        ans = ans + " + " + str(b) + "n"
    elif b < 0:
        ans = ans + " - " + str(abs(b)) + "n"
    if c > 0:
        ans = ans + " + " + str(c)
    elif c < 0:
        ans = ans + " - " + str(abs(c))
    ans = ans + "$"
    return q,ans
