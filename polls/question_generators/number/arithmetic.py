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
    
def order_of_operations():
    q = "$"
    m = []
    mops = ["+","-","*","/"]
    qops = ["+","-",r"\times","\div"]
    brackets = random.randint(0,2)
    
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

def times_tables(min_n, div_fact):
    a = random.randint(min_n,12)
    b = random.randint(min_n,12)
    c = a*b 
    if div_fact == 1:
        if random.randint(0,1) == 1:
            q = "$" + str(c) + "\div" + str(b) + "$"
            ans = a
        else:
            q = "$" + str(c) + "\div" + str(a) + "$"
            ans = b
    else:
        if random.randint(0,1) == 1:
            q = "$" + str(a) + r"\times" + str(b) + "$"
            ans = c
        else:
            q = "$" + str(b) + r"\times" + str(a) + "$"
            ans = c
    return q, ans
        


def addition(decimal=1, add_sub=0):
    dps = random.randint(3,4)
    a = round(random.random(),dps)
    dps_adj =random.randint(-1,1)
    b = round(random.random(),dps+dps_adj)
    
    if decimal==0:
        a=strip_0(round(a*10**dps,0))
        b=strip_0(round(b*10**(dps+ dps_adj),0))
        
    if add_sub==0:
        q = '$' + str(a) + ' + ' + str(b) + '$'
        ans = int(a) + int(b)
    else:
        if int(a) > int(b):
            q = '$' + str(a) + ' - ' + str(b) + '$'
            ans = int(a)-int(b)
        else:
            q = '$' + str(b) + ' - ' + str(a) + '$'
            ans=int(b)-int(a)

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
