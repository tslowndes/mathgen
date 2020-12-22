import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *


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

def frac_to_decimal(a1=0, a2=0, a3=0, a4=0, a5=0,a6=0):
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

    if str(numerator) == numerator1:
        fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + '}$'
    else:
        fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + r'} = \frac{' + numerator1 + '}{' + denominator1 + '}$'

    decimal = a

    return decimal, fraction