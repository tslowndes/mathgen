import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *

def gen_fraction_conversions(a1=0,a2=0,a3=0,a4=0,a5=0,a6=0):
    questions = []
    answers = []
    for i in range(10):
        if (i%2)==0:
            a,q = frac_to_decimal(1)
            question = 'Write the fraction as a decimal.' + q
            answer = str(a)
        else:
            q,a = frac_to_percentage()
            question = 'Write the fraction as a percentage: ' + q
            answer = a
        questions.append(question)
        answers.append(answer)
    return {'count':[i for i in range(0,10)], 'questions':questions, 'answers':answers}

def gen_decimal_conversions(a1=0,a2=0,a3=0,a4=0,a5=0,a6=0):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in count:
        if (i%2) == 0:
            a,q = percentage_to_decimal(0,0)
            questions.append('Write ' + q + ' as a percentage.')
            answers.append(a)
        else:
            q,a = frac_to_decimal(0)
            questions.append('Write ' + q + ' as a fraction.')
            answers.append(a)

    return {'count':count, 'questions':questions, 'answers':answers}


def gen_percentage_conversions(a1=0,a2=0,a3=0,a4=0,a5=0,a6=0):
    questions = []
    answers = []
    count = [i for i in range(0,10)]
    for i in range(10):
        if (i%2)==0:
            q,a = percentage_to_fraction()
            question = 'Write ' + q + ' as a fraction.'
            answer = a
        else:
            if i < 6:
                q,a = percentage_to_decimal(0,0)
            else:
                if random.randint(0,1) == 0:
                    q,a = random.choice([percentage_to_decimal(0,1), percentage_to_decimal(1,0)])
                else:
                    q,a = percentage_to_decimal(1,1)

            question = 'Write ' + q + ' as a decimal.'
            answer = a
        questions.append(question)
        answers.append(answer)

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

    if str(numerator) == numerator1:
        fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + '}$'
    else:
        fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + r'} = \frac{' + numerator1 + '}{' + denominator1 + '}$'

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

def frac_to_percentage(a1=0, a2=0, a3=0, a4=0, a5=0,a6=0):
    denominator = random.choice([2,4,5,10, 20, 25, 50])
    numerator = random.randint(1,denominator-1)

    percentage = numerator / denominator * 100
    percentage = str(percentage)
    if percentage[-2:] == '.0':
        percentage = percentage[:-2]
    percentage = str(percentage) + '%'

    fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + '}$'

    return fraction, percentage

def frac_to_decimal(q=0, a2=0, a3=0, a4=0, a5=0,a6=0):
    a = round(random.random(), 2)

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
        if random.randint(0,1)==1:
            fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + '}$'
        else:
            fraction = r'$\frac{' + numerator1 + '}{' + denominator1 + '}$'
    decimal = a

    return decimal, fraction