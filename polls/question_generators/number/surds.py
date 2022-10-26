import random
import math
from polls.question_generators.tools import *

def gen_simplifying_surds(coefficient,squares,c,d,e,f):
    n = 10
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(n):
        q,a = simplifying_surds(coefficient,squares)
        while q in questions:
            q,a = simplifying_surds(coefficient,squares)
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}


def simplifying_surds(coefficient,only_squares):
    squares = [196,169,144,121,100,81,64,49,36,25,16,9,4]
    surds_simplify = [(2,6),(2,8),(2,10),(3,6),(3,8),(4,8),(4,9),(5,8),(5,10),(6,10),(7,8),(4,7),(36,2),(2,100),(3,100),(4,100)]
    if coefficient == 1:
        a = random.randint(2,9)
    else:
        a = 1

    if only_squares==1:
        b = random.choice(squares)
    else:
        b = random.choice(surds_simplify)
        b = b[0]*b[1]

    if a != 1:
        q = '$' + str(a) + '\sqrt{' + str(b) + '}$'
    else:
        q = '$' + '\sqrt{' + str(b) + '}$'
    i = 0
    simplified = 0
    if b in squares:
        a = a * math.sqrt(b)
        b = 1
        ans = '$' + strip_0(a) + '$'
    else:
        while simplified == 0 and i < len(squares):
            if (b/squares[i]).is_integer():
                b = b / squares[i]
                a = a * math.sqrt(squares[i])
                simplified = 1
            else:
                i += 1
        ans = '$' +strip_0(a) + '\sqrt{' + strip_0(b) + '}$'

    return q,ans




def gen_expanding_surds(simplify,coefficients,two_surds,d,e,f):
    n = 10
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(n):
        q,a = expanding_surds(simplify,coefficients,two_surds,)
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def expanding_surds(simplify, coefficients, two_surds):
    squares = [100,81,64,49,36,25,16,9,4]
    # a /b ( c/d + e/f )
    surds = [2,3,5,6,7,8,10]

    surds_no_simplify = [(2,3),(2,5),(2,7),(3,5),(3,7),(3,10),(5,6),(5,7),(6,7),(7,10)]
    surds_simplify = [(2,2),(2,6),(2,8),(2,10),(3,3),(3,6),(3,8),(5,5),(5,8),(5,10),(6,6),(6,10),(7,7),(8,8)]
    if coefficients == 0:
        a = 1
        c = 1
        e = 1
    elif coefficients == 1:
        if random.randint(0,1) == 1:
            a = random.randint(2,6)
            c = 1
        else:
            c = random.randint(2,6)
            a = 1
    elif coefficients == 2:
            a = random.randint(2,6)
            c = random.randint(2,6)
    e = random.randint(2,6)



    if simplify == 0:
        b,d = random.choice(surds_no_simplify)
    else:
        b,d = random.choice(surds_simplify)


    if two_surds == 1:
        f = random.choice(surds)
    else:
        if random.randint(0,1)==1:
            f = d
            d = 1
        else:
            f = 1

    if f == 1:
        q = '$' + str(a) + '\sqrt{' + str(b) + '}' + '\left (' + str(c) + '\sqrt{' + str(d) + '} + ' + str(e) + r'\right ) $'
    elif d == 1:
        q = '$' + str(a) + '\sqrt{' + str(b) + '}' + '\left (' + str(c) + ' + ' + str(e) + '\sqrt{' + str(f) + r'}\right ) $'
    else:
        q = '$' + str(a) + '\sqrt{' + str(b) + '}' + '\left (' + str(c) + '\sqrt{' + str(d) + '}' + ' + ' + str(e) + '\sqrt{' + str(f) + r'} \right ) $'

    q_new = ''
    for i in range(0,len(q)):
        if q[i] == '1':
            if q[i+1] != '\\':
                q_new = q_new + q[i]
        else:
            q_new = q_new + q[i]

    ans_a = a * c
    ans_b = b * d
    ans_c = a * e
    ans_d = b * f
    if simplify == 1:
        i = 0
        simplified = 0
        if ans_b in squares:
            ans_a = ans_a * math.sqrt(ans_b)
            ans_b = 1
        else:
            while simplified == 0 and i < len(squares):
                if (ans_b/squares[i]).is_integer():
                    ans_b = ans_b / squares[i]
                    ans_a = ans_a * math.sqrt(squares[i])
                    simplified = 1
                else:
                    i += 1

        i = 0
        simplified = 0
        if ans_d in squares:
            ans_c = ans_c * math.sqrt(ans_d)
            ans_d = 1
        else:
            while simplified == 0 and i < len(squares):
                if (ans_d/squares[i]).is_integer():
                    ans_d = ans_d / squares[i]
                    ans_c = ans_c * math.sqrt(squares[i])
                    simplified = 1
                else:
                    i += 1




    ans = '$' + strip_0(ans_a) + r'\sqrt{' + strip_0(ans_b) + '}' + ' + ' + strip_0(ans_c) + '\sqrt{' + strip_0(ans_d) + '} $'
    ans_new = ''

    for i in range(0,len(ans)):
        if ans[i] == '1':
            if ans[i+1] != '\\':
                ans_new = ans_new + ans[i]
        else:
            ans_new = ans_new + ans[i]

    if '\sqrt{1}' in ans_new:
        ans = ans_new.split('\sqrt{1}')
        ans_new = ans[0] + ans[1]

    return q_new,ans_new




