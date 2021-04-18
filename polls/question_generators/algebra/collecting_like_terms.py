import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *

def adding_algebra_terms(a1, a2, a3, a4, a5, a6):
    a = random.randint(1, 10)
    b = rand_no0(-10,10)
    while a == b:
        b = rand_no0(-10, 10)
    alpha = get_alpha()

    c = a + b
    question = '$' + tidy_algebra(str(a) + alpha + ' + ' + str(b) + alpha) + '$'
    answer = '$' + tidy_algebra(str(c) + alpha) + '$'

    return question, answer

def gen_adding_algebra_terms(n, a2, a3, a4, a5, a6):
    count = []
    qs = []
    anss = []
    for i in range(0, n):
        count.append(i)
        q,a = adding_algebra_terms(0,0,0,0,0,0)
        qs.append(q)
        anss.append(a)

    return {
        'count': count,
        'questions': qs,
        'answers': anss
    }

def gen_collecting_like_terms(powers, doubleletters, a3, a4, a5, a6):
    count = []
    qs = []
    anss = []
    for i in range(0, 10):
        y1 = rand_no0(-10, 10)
        y2 = rand_no0(-10, 10)
        x1 = rand_no0(-10, 10)
        x2 = rand_no0(-10, 10)

        if powers == 0 and doubleletters == 0:
            alpha1 = 'a'
            alpha2 = 'a'
            while alpha1 == alpha2:
                alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
                alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
        if powers == 1 and doubleletters == 1:
            if random.randint(0,1) ==0:
                alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
                alpha2 = alpha1 + "^" + str(random.randint(2, 3))
                if random.randint(0,1) == 0:
                    alpha1 = alpha1 + "^" + str(random.randint(4, 5))
            else:
                alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
                alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
                while alpha1 == alpha2:
                    alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
                alpha2 = alpha1 + alpha2

        elif powers ==1 and doubleletters ==0:
            alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
            alpha2 = alpha1 + "^" + str(random.randint(2,3))
            if random.randint(0, 1) == 0:
                alpha1 = alpha1 + "^" + str(random.randint(4, 5))

        elif doubleletters == 1 and powers ==0 :
            alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
            alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
            while alpha1 == alpha2:
                alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
            alpha2 = alpha1 + alpha2



        terms = [str(y1) + alpha1, str(y2) + alpha1, str(x1) + alpha2, str(x2) + alpha2]
        random.shuffle(terms)
        terms = terms[0] + ' + ' + terms[1] + ' + ' + terms[2] + ' + ' + terms[3]

        if y1 + y2 == 0:
            ans = str(x1 + x2) + alpha2
        elif x1 + x2 == 0:
            ans = str(y1 + y2) + alpha2
        elif x1 + x2 == 0 and y1 + y2 == 0:
            ans = 0
        else:
            ans = str(y1 + y2) + alpha1 + " + " + str(x1 + x2) + alpha2

        terms = tidy_algebra(terms)
        ans1 = tidy_algebra(ans)
        count.append(i)
        qs.append('$' + terms + '$')
        anss.append('$' + ans1 + '$')

    return {
        'count': count,
        'questions': qs,
        'answers': anss
    }
