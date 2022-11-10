import random
from decimal import Decimal
import numpy as np
from polls.question_generators.tools import *

def long_mult(multordiv):
    a = random.randint(4,9)
    b = random.randint(15,50)
    if multordiv ==0:
        q = "$" + str(a) + r"\times" + str(b) + "$"
        ans = a*b
    else:
        q = "$" + str(a*b) + "\div" + str(a) + "$"
        ans = b
    return q,ans

def get_random_op(m):
    mops = ["+","-","*","/"]
    op = random.choice(mops)
    while op in m:
        op = random.choice(mops)
    return op

def get_random_n(m):
    n = random.randint(2,9)
    while n in m:
        n = random.randint(2,9)
    return n

def order_of_operations(brackets=9):
    q = "$"
    m = []
    mops = ["+","-","*","/"]
    qops = ["+","-",r"\times","\div"]
    if brackets == 9:
        brackets = random.randint(0,2)
    elif brackets == 1:
        brackets = random.randint(1,2)

    for i in range(2):
        if brackets == 0:
            if i ==0:
                m.append(str(get_random_n(m)))
            m.append(get_random_op(m))
            m.append(str(get_random_n(m)))
        elif brackets == 1:
            if i ==0:
                m.append("(")
                m.append(str(get_random_n(m)))
            m.append(get_random_op(m))
            m.append(str(get_random_n(m)))
            if i == 0:
                m.append(")")
        elif brackets == 2:

            if i ==1:
                m.append("(")

            m.append(str(get_random_n(m)))
            m.append(get_random_op(m))

            if i == 1:
                m.append(str(get_random_n(m)))
                m.append(")")

    if "/" in m:
        i = m.index("/")
        if m[i-1]==")":
            m[i-2] = str(int(m[i-2]) * int(m[i+1]))
            if m[i-3]!="*":
                m[i-4] = str(int(m[i-4]) * int(m[i+1]))
        else:
            if m[i+1]!="(":
                m[i-1] = str(int(m[i-1]) * int(m[i+1]))
            else:
                e = eval(m[i+2] + m[i+3] + m[i+4])
                m[i-1] = str( int(m[i-1]) * e)

    if "-" in m:
        i = m.index("-")
        if m[i-2] != "(":
            m1 = eval("".join(m[:i]))
            m2 = eval("".join(m[i+1:]))
            if m2 > m1:
                 m = m[i+1:] + ["-"] + m[:i]
        else:
            if int(m[i-1]) - int(m[i+1]) < 0:
                temp = m[i-1]
                m[i-1] = m[i+1]
                m[i+1] = temp

    s = ""
    for c in m:
        if c in mops:
            q = q + qops[mops.index(c)]
        else:
            q = q + c
        s= s + c

    return q+"$", eval(s)

def mental_addition_number_bonds_10():
    a = random.randint(1,3)
    b = random.randint(2,8)
    c = random.randint(1,5)
    d = random.randint(10-b,9)
    a = a*10+b
    c = c*10+d
    q = '$' + strip_0(a) + ' + ' + strip_0(c) + '$'
    ans = strip_0(a+c)
    return q,ans

def gen_mental_addition_number_bonds_10(a,b,c,d,e,f):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q,a = mental_addition_number_bonds_10()
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}



def mental_addition(just_over_100=1):
    if just_over_100 == 0:
        a=100 - random.randint(1,3)
    else:
        a=100 + random.randint(1,3)
    b = random.randint(150,250)
    if random.randint(0,1) == 0:
        q = '$' + str(b) + ' + ' + str(a) + '$'
        ans = b + a
    else:
        q = '$' + str(b) + ' - ' + str(a) + '$'
        ans = b - a

    return q, ans

def gen_times_tables(min_n,div_fact,related_calc,d,e,f):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q,a = times_tables(min_n,div_fact,related_calc)
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}


def times_tables(min_n, div_fact,related_calc=0):
    a = random.randint(min_n,12)
    b = random.randint(min_n,12)
    c = a*b
    if div_fact == 1:
        if related_calc ==1:
            c = c / 10
            if c < 1:
                c = '0' + str(c)

        if random.randint(0,1) == 1:
            q = "$" + strip_0(c) + "\div" + str(b) + "$"
            ans = a
        else:
            q = "$" + strip_0(c) + "\div" + str(a) + "$"
            ans = b

    else:
        if related_calc == 1:
            a = a / 10
            if a < 1:
                a = '0' + strip_0(a)
            else:
                a = strip_0(a)

        if random.randint(0,1) == 1:
            q = "$" + str(a) + r"\times" + str(b) + "$"
            ans = c
        else:
            q = "$" + str(b) + r"\times" + str(a) + "$"
            ans = c

    if related_calc == 1:
        ans = ans / 10
        if ans < 1:
            ans = '0' + strip_0(ans)

    return q, ans

def addition(decimal=1, add_sub=0, dec_offset=0):
    dps = random.randint(2,4)
    a = random.randint(1,9) + round(random.random(),dps)

    if dec_offset == 1:
        if add_sub == 0:
            dec_offset = -1
        else:
            dec_offset = 1
    elif dec_offset == 2:
        a = a + 10*random.randint(1,3)
        if add_sub == 0:
            dec_offset = -1
        else:
            dec_offset = 1
    elif dec_offset == 3:
        a = a + 100*random.randint(1,3)
        dec_offset = random.randint(1,2)
        if random.randint(0,1) == 0:
            dec_offset = dec_offset*-1

    b = random.randint(1,9) + round(random.random(),dps+dec_offset)

    if decimal==0:

        a = random.randint(100,999)
        b = random.randint(1000,9999)

        a=strip_0(round(a,0))
        b=strip_0(round(b,0))

    if len(str(a)) > 7:
        a = round(a,5)
    if len(str(b)) > 7:
        b = round(b,5)

    if add_sub==0:
        if random.randint(0,1) == 0:
            q = '$' + str(a) + ' + ' + str(b) + '$'
        else:
            q = '$' + str(b) + ' + ' + str(a) + '$'
        ans = float(a) + float(b)
    else:
        if int(a) > int(b):
            q = '$' + str(a) + ' - ' + str(b) + '$'
            ans = float(a)-float(b)
        else:
            q = '$' + str(b) + ' - ' + str(a) + '$'
            ans=float(b)-float(a)

        ans=strip_0(round(ans,8))

    return q, ans

def gen_mental_addition(n,just_over_100,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q,a = mental_addition(just_over_100)
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

def gen_addition(n,decimal,add_sub,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        if i < 2:
            dec_offset = 0
        elif i < 4:
            dec_offset = 1
        elif i < 6:
            dec_offset = 2
        else:
            dec_offset = 3

        q,a = addition(decimal, add_sub, dec_offset)
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}

def multiply_decimals():
    a = round(random.random(), 1)
    b = round(random.random(), 2)

    q = '$' + str(a) + r'\times' + str(b) + '$'
    ans = round(Decimal(a) * Decimal(b), 3)
    return q,ans

def gen_order_of_ops(brackets,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q,a = order_of_operations(brackets)
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}
