import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *
import math

def gen_fraction_conversions(dec_per,a2=0,a3=0,a4=0,a5=0,a6=0):
    questions = []
    answers = []
    i = 0
    while i < 10:
        if dec_per==0:
            if i < 4:
                a,q = frac_to_decimal(1)
            else:
                a,q = frac_to_decimal(1,1)
            question = q
            answer = str(a)
        else:
            if i < 4:
                q,a = frac_to_percentage(0)
            else:
                q,a = frac_to_percentage(1)
            question = q
            answer = a
        if q not in questions:
            questions.append(question)
            answers.append(answer)
            i += 1
    return {'count':[i for i in range(0,10)], 'questions':questions, 'answers':answers}

def gen_decimal_conversions(a1=0,a2=0,a3=0,a4=0,a5=0,a6=0):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in count:
        if (i%2) == 0:
            a,q = percentage_to_decimal(0,0)
            questions.append(q)
            answers.append(a)
        else:
            q,a = frac_to_decimal(0)
            questions.append(q)
            answers.append(a)

    return {'count':count, 'questions':questions, 'answers':answers}


def gen_percentage_conversions(frac_dec=0,a2=0,a3=0,a4=0,a5=0,a6=0):
    questions = []
    answers = []
    count = [i for i in range(0,10)]
    i = 0
    while i < 10:
        if frac_dec==0:
            q,a = percentage_to_fraction()
            question = q
            answer = a
        else:
            if i < 6:
                q,a = percentage_to_decimal(0,0)
            else:
                if random.randint(0,1) == 0:
                    q,a = random.choice([percentage_to_decimal(0,1), percentage_to_decimal(1,0)])
                else:
                    q,a = percentage_to_decimal(1,1)

            question = q
            answer = a
        if question not in questions:
            questions.append(question)
            answers.append(answer)
            i+=1

    return {'count':count, 'questions':questions, 'answers':answers}


def percentage_to_fraction(a1=0, a2=0, a3=0, a4=0, a5=0, a6=0):
    denominator = random.choice([2, 4, 5, 10, 20, 25, 50])
    numerator = random.randint(1, denominator - 1)

    percentage = numerator / denominator * 100
    percentage = str(percentage)
    if percentage[-2:] == '.0':
        percentage = percentage[:-2]
    percentage = str(percentage) + '%'

    numerator1, denominator1 = simplify_frac(numerator, denominator)

    numerator1 = str(numerator1).strip('0')
    denominator1 = str(denominator1).strip('0')

    if numerator1[-1] == '.':
        numerator1 = numerator1[:-1]

    if denominator1[-1] == '.':
        denominator1 = denominator1[:-1]

    if str(percentage[:-1]) == numerator1:
        fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + '}$'
    else:
        fraction = r'$\frac{' + str(percentage[:-1]) + '}{' + str(100) + r'} = \frac{' + numerator1 + '}{' + denominator1 + '}$'

    return percentage, fraction

def percentage_to_decimal(more_than_100,decimal):
    max = 100
    if more_than_100 == 1:
        max = 300

    percentage = random.randint(0,max)

    if decimal == 1:
        percentage += round(random.random(),1)

    q = str(percentage) + '%'
    a = str(percentage/100)

    return q,a

def frac_to_percentage(easy_hard, a2=0, a3=0, a4=0, a5=0,a6=0):
    if easy_hard == 0:
        if random.randint(0,1)==0:
            b = random.randint(1,99)
            while math.gcd(b,100)!=1:
                b += 1
            numerator = b
            denominator = 100
        else:
            numerator = random.choice([1,3,5,7,9])
            denominator = 10
    else:
        denominator = random.choice([2,4,5,10, 20, 25, 50])
        numerator = random.randint(1,denominator-1)

    percentage = numerator / denominator * 100
    percentage = str(percentage)
    if percentage[-2:] == '.0':
        percentage = percentage[:-2]

    percentage = str(percentage) + '%'
    numerator, denominator = simplify_frac(numerator, denominator)
    numerator = strip_0(numerator)
    denominator = strip_0(denominator)
    fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + '}$'

    return fraction, percentage

def frac_to_decimal(q=0, easy_hard=0, a3=0, a4=0, a5=0,a6=0):
    if easy_hard == 1:
        a = random.randint(1,99)
        while math.gcd(a,100)==1 or math.gcd(a,100)==10:
            a += 1
        a = a/100
    else:
        b = random.randint(1,99)
        while math.gcd(b,100)!=1:
            b += 1
        a = random.choice([random.choice([1,3,5,7,9])/10, b/100])

    a = str(a)
    if a[-1] == 0:
        a = a[:-1]

    numerator = a[a.find('.')+1:]

    if len(numerator) == 1:
        denominator = 10
    else:
        denominator = 100

    numerator = int(numerator)

    numerator1, denominator1 = simplify_frac(numerator, denominator)

    numerator1 = str(numerator1).strip('0')
    denominator1 = str(denominator1).strip('0')

    if numerator1[-1] == '.':
        numerator1 = numerator1[:-1]

    if denominator1[-1] == '.':
        denominator1 = denominator1[:-1]
    if q == 0:
        if str(numerator) == numerator1:
            fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + '}$'
        else:
            fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + r'} = \frac{' + numerator1 + '}{' + denominator1 + '}$'
    else:
        fraction = r'$\frac{' + numerator1 + '}{' + denominator1 + '}$'
    decimal = a

    return decimal, fraction