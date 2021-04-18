import random
from polls.question_generators.tools import *
import numpy as np
def multiplying_terms(n_alphas):
    n_terms = random.randint(2,6)

    alpha1 = get_alpha()
    if n_alphas == 1:
        alpha2 = alpha1
    else:
        alpha2 = get_alpha()
        while alpha2 == alpha1:
            alpha2 = get_alpha()

    alphas = [alpha1, alpha2]
    q = '$' + alpha1 + r' \times ' + alpha2
    for i in range(n_terms-2):
        a = random.choice([alpha1, alpha2])
        alphas.append(a)
        q = q + r' \times ' + a
    q = q + '$'

    unique = list(set(alphas))

    unique.sort()

    if len(unique) == 1:
        ans = '$' + alpha1 + '^' + str(len(alphas)) + '$'
    else:
        ans = '$' + tidy_algebra(unique[0] + '^' + str(alphas.count(unique[0])) +'\;' + unique[1] + '^' + str(alphas.count(unique[1]))) + '$'
    return q,ans


def laws_of_indices_multiplying(n_terms, min_i, coefficient):
    alpha1 = get_alpha()
    i = []
    cs = []
    q = '$'
    for j in range(n_terms):
        i.append(rand_no0_no1(min_i,10))
        if coefficient == 0:
            cs.append('')
        else:
            cs.append(random.randint(2,5))

        if j == 0:
            q = q + str(cs[-1]) + alpha1 + '^{' + str(i[-1]) + '}'
        else:
            q = q + r' \times ' + str(cs[-1]) + alpha1 + '^{' + str(i[-1]) + '}'

    q = q + '$'
    if coefficient == 0:
        ans = '$' + alpha1 + '^{' + str(np.sum(i)) + '}$'
    else:
        ans = '$' + str(np.prod(cs)) + alpha1 + '^{' + str(np.sum(i)) + '}$'

    return q, ans

def laws_of_indices_dividing(n_terms, min_i, coefficient):
    alpha1 = get_alpha()
    i = []
    cs = []
    q = '$'
    fraction = 0
    index_ans = 0
    if coefficient == 0:
        c_ans = ''
    else:
        c_ans = 0


    for j in range(n_terms):
        if n_terms == 2:
            if j == 0:
                fraction = random.randint(0,1)
        i_temp = rand_no0_no1(min_i,10)
        while i_temp in i:
            i_temp = rand_no0_no1(min_i, 10)
        i.append(i_temp)
        if coefficient == 0:
            cs.append('')
        else:
            c = random.randint(2,5)
            while c in cs:
                c = random.randint(2, 5)
            cs.append(c)

        if j == 0:
            index_ans = i[-1]
            if coefficient == 1:
                c_ans = cs[-1]
        else:
            index_ans = index_ans - i[-1]
            if coefficient == 1:
                c_ans = c_ans * cs[-1]

    for j in range(n_terms):
        if j == 0:
            if fraction == 0:
                q = q + str(c_ans) + alpha1 + '^{' + str(i[j]) + '}'
            else:
                q = q + r'\frac{' + str(c_ans) + alpha1 + '^{' + str(i[j]) + '}' + '}{'
        else:
            if fraction == 0:
                q = q + r' \div ' + str(cs[j-1]) + alpha1 + '^{' + str(i[j]) + '}'
            else:
                q = q + str(cs[j-1]) + alpha1 + '^{' + str(i[j]) + '}}'


    q = q + '$'

    if coefficient == 0:
        ans = '$' + alpha1 + '^{' + str(index_ans) + '}$'
    else:
        ans = '$' + str(cs[-1]) + alpha1 + '^{' + str(index_ans) + '}$'

    return q, ans

def gen_law_of_indices(multi_or_div,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(10):
        if multi_or_div == 0:
            if i < 5:
                q, a = laws_of_indices_multiplying(2,2,0)
            elif i < 8:
                q, a = laws_of_indices_multiplying(2,-3, 1)
            else:
                q, a = laws_of_indices_multiplying(random.randint(2,3),-10, 1)
        elif multi_or_div == 1:
            if i < 5:
                q, a = laws_of_indices_dividing(2,2,0)
            elif i < 8:
                q, a = laws_of_indices_dividing(2,-3, 1)
            else:
                q, a = laws_of_indices_dividing(random.randint(2,3),-10, 1)


        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}



def gen_multiplying_terms(a,b,c,d,e,f):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(10):
        if i < 5:
            q, a = multiplying_terms(1)
        else:
            q,a = multiplying_terms(2)

        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

