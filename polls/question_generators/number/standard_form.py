import random
from math import floor
from decimal import Decimal
from polls.question_generators.tools import *

def powers_of_ten(neg):
    #if neg == 0:
    power_of_ten = random.randint(1,9)
    #else:
    #    power_of_ten = random.randint(-9,-1)
    ordinary = 10**power_of_ten

    if random.randint(0,1)==1:
        q = '$10^{' + str(power_of_ten) + '} = $'
        ans = ordinary
    else:
        if neg == 1:
            q = '0.'
            for i in range(abs(power_of_ten)-1):
                q = q + '0'
            q = '$' + q + '1' +  r'= 10^{\left [ \;\; \right]}$'
        else:
            q = '$' + strip_0(ordinary) + r'= 10^{\left [ \;\; \right]}$'
        #q = '$' + str(ordinary) + r' = 10^{\left [ \;\; \right]}$'
        #q = '$' + strip_0('0' + '{:.10f}'.format(ordinary)) + r' = 10^{\left [ \;\; \right]}$'
        ans = power_of_ten

    return q,ans

def gen_power_of_ten(n,neg,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(n):
        q,a = powers_of_ten(neg)
        while q in questions:
            q,a = powers_of_ten(neg)

        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def multiplying_standard_form(adj, dec,neg_power):
    if neg_power == 0:
        min_power = 2
        max_power = 20
    else:
        min_power = -10
        max_power = 10
    if adj == 0:
        a1 = random.randint(1,3)
        a2 = rand_no0_no1(min_power,max_power)
        b1 = random.randint(1,3)
        b2 = rand_no0_no1(min_power, max_power)
        if random.randint(0,1) == 0:
            q = r'$ \left(' + str(a1) + r'\times 10^{' + str(a2) + r'} \right) \times \left ( ' + str(b1) + r'\times 10^{' + str(b2) + r'} \right) $'
        else:
            q = r'$ ' + str(a1) + r'\times 10^{' + str(a2) + r'}  \times  ' + str(b1) + r'\times 10^{' + str(b2) + r'}  $'

        ans = r'$' + str(a1*b1) + r'\times 10^{' + str(a2+b2) + r'} $'
        return q,ans
    else:
        a1 = random.randint(3,9)
        a2 = rand_no0_no1(min_power,max_power)
        b1 = random.randint(4,9)
        b2 = rand_no0_no1(min_power, max_power)
        if random.randint(0,1) == 0:
            q = r'$ \left(' + str(a1) + r'\times 10^{' + str(a2) + r'} \right) \times \left ( ' + str(b1) + r'\times 10^{' + str(b2) + r'} \right) $'
        else:
            q = r'$ ' + str(a1) + r'\times 10^{' + str(a2) + r'}  \times  ' + str(b1) + r'\times 10^{' + str(b2) + r'}  $'
        ans = a1*b1
        power = a2+b2
        if a1 * b1 >= 10:
            ans = ans / 10
            power = power + 1
        ans = r'$' + str(ans) + r'\times 10^{' + str(power) + r'} $'
        return q,ans
        pass

def gen_multiplying_standard_form(multi_div,adj,c,d,e,f):
    questions = []
    answers = []
    count = [i for i in range(10)]

    dec = 0
    for i in range(10):
        if i < 4:
            neg_power = 0
        else:
            neg_power = 1
        q,a = multiplying_standard_form(adj,dec,neg_power)
        while q in questions:
            q,a = multiplying_standard_form(adj,dec,neg_power)

        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def gen_standard_form(n,large_small_mix,max_power,std_to_ord,adj,e):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(n):
        if i < 3:
            dec = 0
        elif i < 6:
            dec = 1
        else:
            dec = 2

        if adj == 0:
            if large_small_mix == 0:
                q,a = standard_form_large(max_power,dec,std_to_ord)
                while q in questions:
                    q,a = standard_form_large(max_power,dec,std_to_ord)

            elif large_small_mix == 1:
                q,a = standard_form_large(max_power,dec,std_to_ord)
                while q in questions:
                    q,a = standard_form_large(max_power,dec,std_to_ord)
        else:
            q,a = standard_form_large(max_power,dec,std_to_ord,adj)
            while q in questions:
                q,a = standard_form_large(max_power,dec,std_to_ord)

        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def strip_zeros(a):
    if "." in a:
        a = a.strip("0")
        if a[-1] == ".":
            a = a[:-1]
    return a

def standard_form_large(max_power, decimal, std_to_ord, adj=0):
    if max_power > 0:
        if max_power > 4:
            power = random.randint(max_power-4,max_power)
        else:
            power = random.randint(1,max_power)
    else:
        if max_power > -5:
            power = random.randint(max_power,-1)
        else:
            power = random.randint(max_power,max_power+4)

    if decimal != 0:
        a = round(random.random()*10, decimal)
        while a < 1:
            a = a * 10
    else:
        a = random.randint(1,9)

    if std_to_ord == 0:
        if adj == 0:
            q = strip_zeros("{:.10f}".format(round(a*10**power,abs(power)+decimal)))
            if max_power > 0:
                q = readable_digits(strip_zeros(str(q)))
            else:
                #p = readable_digits(q[1:][::-1])
                #q = "0." + p[::-1]
                q="0" + str(q)
        else:
            adjustment = rand_no0(-3,3)
            q = '$' + strip_zeros(str(round(a*10**adjustment,abs(adjustment)))) + r'\times 10^{' + str(power-adjustment) + '}$'
            if q[1] == '.':
                q = q[0] + "0" + q[1:]

        a = strip_zeros(str(a))
        ans = '$' + str(a) + r'\times 10^{' + str(power) + '}$'
    else:

        ans=readable_digits(strip_zeros(str(round(a*10**power,0))))
        a = strip_zeros(str(a))

        q = '$' + str(a) + r'\times 10^{' + str(power) + '}$'

    return q,ans