import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *

def gen_solving_equations(n, negs, negxs, steps, bothsides, brackets):
    count = []
    qs = []
    ans = []
    max = 9
    min = 1
    minx = 1

    if negs == 1:
        min = -10
    else:
        min = 1

    for i in range(0, n):

        if i > 5:
            minx = -10
        else:
            minx = 1

        count.append(i)
        a=0
        b=0
        x=0

        if steps == 1:
            if random.randint(0,1) == 0:
                a = 1
                b = rand_no0_no1(min, 9)
            else:
                a = rand_no0_no1(minx, 9)
                b = 0
        else:
            a = rand_no0_no1(minx, 9)
            b = rand_no0_no1(min, 9)

        x = rand_no0_no1(minx, 9)

        if a == 1 or brackets == 1 or bothsides == 1:
            multidiv = 0
        else:
            multidiv = random.randint(0,1)
            a = rand_no0_no1(2, 5)

        if multidiv == 0:
            c = (a*x) + b
        else:
            c = rand_no0_no1(b+1, 10)
            x = (c-b)*a

        if brackets == 1:
            d = rand_no0_no1(0,5)
            c = c * d

        if bothsides == 1:
            e = rand_no0(-10, 10)
            f = a + e

            while f == 0:
                e = rand_no0(-10, 10)
                f = a + e

            a = f

        x_side = ''
        ans_side = str(c)

        alpha = random.choice('abcdefghjklmnpqrstuvwxyz')

        if bothsides == 1:
            if random.randint(0,1) == 0:
                ans_side = ans_side + " + " + str(e) + alpha
            else:
                ans_side = str(e) + alpha + " + " + ans_side
            ans_side = tidy_algebra(ans_side)

        if b == 0:
            if multidiv == 0:
                x_side = str(a) + alpha
            else:
                x_side = r"\frac{" + alpha + "}{" + str(a) + "}"

        else:
            if random.randint(0,1) > 0 or i < 4:
                if multidiv == 0:
                    x_side = str(a) + alpha + " + " + str(b)
                else:
                    x_side = r'\frac{' + alpha + "}{" + str(a) + "}" + " + " + str(b)
            else:
                if multidiv == 0:
                    x_side = str(b) + " + " + str(a) + alpha
                else:
                    x_side = str(b) + " + " + r'\frac{' + alpha + "}{" + str(a) + "}"

        x_side = tidy_algebra(x_side)

        if brackets == 1:
            x_side = str(d) + "(" + x_side + ")"

        if random.randint(0,1)>0 or i < 6:
            q = x_side + " = " + ans_side
        else:
            q = ans_side + " = " + x_side

        qs.append('$' + q + '$')

        ans.append('$' + alpha + " = " + str(x) + '$')
    if n > 1:
        return {
            'count': count,
            'questions': qs,
            'answers': ans
        }
    else:
        return qs[0], ans[0]
