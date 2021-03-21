import random
from polls.question_generators.tools import *

def one_step_substitution(minx,maxx,add_or_multi,op_or_inv):
    a = random.randint(2,10)
    x = rand_no0_no1(minx, maxx)
    alpha = get_alpha()
    if add_or_multi == 0:
        if op_or_inv == 0:
            q = '$' + alpha + ' = ' + str(x) + '$ $' + alpha + ' + ' + str(a) + '= ?$'
            ans = x + a
        else:
            q = '$' + alpha + ' = ' + str(x) + '$ $' + alpha + ' - ' + str(a) + '= ?$'
            ans = x - a
    else:
        if op_or_inv == 0:
            q = '$' + alpha + ' = ' + str(x) + '$ $' + str(a) + alpha + ' = ?$'
            ans = x * a
        else:
            c = x * a
            q = '$' + alpha + ' = ' + str(c) + r'$ $\frac{' + alpha + '}{' + str(a) + '}= ?$'
            ans = c / a
    return q,ans

def two_step_substitution(minx,maxx,multi_or_div, add_or_subtract,brackets):
    a = random.randint(2,10)
    x = rand_no0_no1(minx, maxx)
    if add_or_subtract == 0:
        b = random.randint(1,10)
    else:
        b = random.randint(-10,-1)

    alpha = get_alpha()

    if multi_or_div == 0:
        if brackets == 0:
            q = '$' + alpha + ' = ' + str(x) + '$ $' + tidy_algebra(str(a) + alpha + ' + ' + str(b)) + '= ?$'
            ans = a*x + b
        else:
            q = '$' + alpha + ' = ' + str(x) + '$ $' + tidy_algebra(str(a) + '(' + alpha + ' + ' + str(b)) + ') = ?$'
            ans = a*(x + b)
    else:
        if brackets == 0:
            c = x * a
            q = '$' + alpha + ' = ' + str(c) + '$ $' + tidy_algebra(as_fraction(alpha,a) + ' + ' + str(b)) + '= ?$'
            ans = c/a + b
        else:
            if add_or_subtract == 0:
                c = (x*a)-b
            else:
                c = (x*a)+b
            q = '$' + alpha + ' = ' + str(c) + '$ $' + tidy_algebra(as_fraction(alpha + ' + ' + str(b),a)) + '= ?$'
            ans = x

    return q,ans

def gen_substitutions(n, steps, neg_xs,d,e,f):
    questions = []
    answers = []
    count = [i for i in range(10)]
    add_or_multi = [0,1,0,1,0,1,0,1,0,1]

    for i in range(10):
        if steps == 1:
            if i > 5:
                q,a = one_step_substitution(-10,-2,add_or_multi[i],random.randint(0,1))
            else:
                q,a = one_step_substitution(2,10,add_or_multi[i],random.randint(0,1))
        elif steps == 2:
            q,a = two_step_substitution(2,10,add_or_multi[i],random.randint(0,1),0)
        elif steps == 3:
            q,a = two_step_substitution(2,10,add_or_multi[i], random.randint(0,1), 1)

        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}
