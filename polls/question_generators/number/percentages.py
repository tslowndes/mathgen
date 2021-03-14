import random
from decimal import Decimal

def percentages_non_calc(compound=0,calc=0):
    if calc == 0:
        easy_small = [1,5,10]
        easy_big = [20,25,50]

        if compound == 0:
            percentage = random.choice(easy_small + easy_big)
        else:
            percentage = 25
            while percentage ==25:
                if random.randint(0,1)==0:
                    percentage = random.choice(easy_big) + random.choice(easy_small)
                else:
                    percentage = random.choice(easy_small) * random.randint(2,9)
    else:
        percentage = random.randint(1,99)

    if str(percentage)[-1] == '0':
        amount = random.randint(2,20) * 10
    elif str(percentage)[-1] == '5':
        amount = random.randint(2,20) * 20
    else:
        amount = random.randint(2,12) * 100

    if calc == 1:
        amount = int(str(amount/10)[:-2])

    q = str(percentage) + '% of ' + str(amount)
    percentage = Decimal(percentage)
    amount = Decimal(amount)
    ans = str(percentage / Decimal(100.0) * amount)
    while ans[-1] == '0' or ans[-1] == '.':
        ans = ans[:-1]


    return q,ans

def gen_percentages_non_calc(n, compound, calc,c,d,e):
    qs = []
    ans = []
    for i in range(n):
        q, a = percentages_non_calc(compound,calc)

        qs.append(q)
        ans.append(a)

    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': ans}


