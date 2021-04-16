import random
from polls.question_generators.tools import *


def solving_inequalities(n, negs, negxs, steps, bothsides, brackets):
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

    if negxs ==1:
        minx = -10
    else:
        minx = 1

    for i in range(0, n):
        subtract = 0
        if i > 4:
            min = -10
        count.append(i)
        a=0
        b=0
        x=0

        if steps == 1:
            if i == 0:
                a = 1
                b = rand_no0_no1(1, 9)
            elif i == 1:
                a = 1
                b = rand_no0_no1(-9, -1)
            elif i == 2:
                a = rand_no0_no1(minx, 9)
                b = 0
            else:
                if random.randint(0,1) == 0:
                    a = 1
                    b = rand_no0_no1(min, 9)
                    if b < 0:
                        subtract = 1
                else:
                    a = rand_no0_no1(minx, 9)
                    b = 0
        else:
            if i == 0:
                a = rand_no0_no1(minx, 9)
                b = random.randint(1,9)
            elif i == 1:
                a = rand_no0_no1(minx, 9)
                b = random.randint(-9,-1)
                subtract = 1
            else:
                a = rand_no0_no1(minx, 9)
                b = rand_no0_no1(min, 9)

        x = rand_no0_no1(minx, 9)

        if a == 1 or brackets == 1 or bothsides == 1:
            multidiv = 0
        else:
            if (i % 2) != 0:
                multidiv = 1
            else:
                multidiv = 0

        if multidiv == 0:
            c = (a*x) + b
        else:
            c = rand_no0_no1(min, 9)
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
            if random.randint(0,1) > 0 or i < 7 or subtract == 1:
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

        sign = random.choice(['<', '>', '\leq', '\geq'])

        if random.randint(0,1)>0 or i < 4:
            q = x_side + sign + ans_side
            ans.append('$' + alpha + sign + str(x) + '$')
        else:
            q = ans_side + sign + ' ' + x_side
            ans.append('$' + str(x) + sign + ' ' + alpha + '$')

        qs.append('$' + q + '$')

    if n > 1:
        return {
            'count': count,
            'questions': qs,
            'answers': ans
        }
    else:
        return qs[0], ans[0]