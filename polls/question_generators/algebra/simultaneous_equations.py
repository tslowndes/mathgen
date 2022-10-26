import random
from polls.question_generators.tools import *

def gen_simultaneous_equations(same_coeff, same_sign,c,d,e,f):
    qs = []
    ans = []
    count = [i for i in range(0, 8)]

    for i in range(0,8):
        q,a = simultaneous_equations(same_coeff, same_sign)

        qs.append(q)
        ans.append(a)

    context = {
        'count':count,
        'questions':qs,
        'answers':ans,
    }
    return context

def simultaneous_equations(same_coeff,same_sign):
    x = random.randint(1,5)
    y = random.randint(1,5)
    a = random.randint(1,5)
    b = random.randint(1,5)
    if same_coeff == 0:
        c = random.randint(1,5)
        while a == c:
            c = random.randint(1,5)
        d = random.randint(1,5)
        while b == d:
            d = random.randint(1,5)
    else:
        if random.randint(0,1) == 0:
            if same_sign == 0:
                c = -a
            else:
                c=a

            d = random.randint(1,5)
            while d == b:
                d = random.randint(1,5)

        else:
            c = random.randint(1,5)
            while c == a:
                c = random.randint(1,5)
            if same_sign == 0:
                d = -b
            else:
                d = b

    e = a*x + b*y
    f = c*x + d*y

    eq1 = tidy_algebra('$' + strip_0(a) + 'x + ' + strip_0(b) + 'y = ' + strip_0(e) + '$' )
    eq2 = tidy_algebra('$' + strip_0(c) + 'x + ' + strip_0(d) + 'y = ' + strip_0(f) + '$' )

    q = eq1 + ' ' + eq2
    ans = '$ x = ' + str(x) + ', y = ' + str(y) + '$'
    return q, ans