import random
from decimal import Decimal
import datetime

def percentages_non_calc(n=-1,compound=0,calc=0, facts=0):
    if calc == 0:
        easy_small = [1,5,10]
        easy_big = [20,25,50]

        if facts == 1:
            percentage = random.choice(easy_small + easy_big)
            n = str(100 / percentage)
            if n[-2] == '.':
                n = n[:-2]
            if random.randint(0,1)==0:
                q = '$100 \div [\;\;] = ' + str(percentage) + '$'
                ans = '$100 \div ' + str(n) + ' = ' + str(percentage) + '$'
            else:
                ans = '$' + str(percentage) + r' \times ' + str(n) + ' = 100 $'
                if random.randint(0,1)==0:
                    q = '$' + str(percentage) + r' \times [\;\;] = 100 $'
                else:
                    q = r'$ [\;\;] \times ' + str(n) + ' = 100 $'
        else:
            if compound == 0:
                if n < 6:
                    percentages = easy_small + easy_big
                    random.seed(int(str(datetime.datetime.now().time())[6:8]))
                    random.shuffle(percentages)
                    percentage = percentages[n]
                else:
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


    if facts == 0:
        if str(percentage) == '25':
            amount = random.randint(2,10)*4
        elif str(percentage) == '20':
            amount = random.randint(2, 10) * 5
        elif str(percentage) == '50':
            amount = random.randint(2, 10) * 2 * random.choice([1,10])
        elif str(percentage)[-1] == '0':
            amount = random.randint(2,10) * 10
        elif str(percentage)[-1] == '5':
            amount = random.randint(2,10) * 20
        else:
            amount = random.randint(2,9) * 100
        if calc == 1:
            amount = int(str(amount/10)[:-2])

        q = str(percentage) + '% of ' + str(amount)
        percentage = Decimal(percentage)
        amount = Decimal(amount)
        ans = str(percentage / Decimal(100.0) * amount)
        while ans[-1] == '0' or ans[-1] == '.':
            ans = ans[:-1]

    return q,ans

def gen_percentages_non_calc(n, compound, calc,facts,d,e):
    qs = []
    ans = []
    for i in range(n):
        q, a = percentages_non_calc(i,compound,calc,facts)

        qs.append(q)
        ans.append(a)

    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': ans}


