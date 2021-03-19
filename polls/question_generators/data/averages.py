import random
import numpy as np

def gen_range():
    first = random.randint(0,100)
    numbers = [random.randint(first-20, first + 20) for i in range(random.randint(4,7))]
    question = ''
    for i in range(len(numbers)):
        if i == 0:
            question += str(numbers[i])
        else:
            question += ',  '
            question += str(numbers[i])
    answer = max(numbers) - min(numbers)
    return question, answer

def find_median(odd_or_even,decimal):

    if odd_or_even == 0:
        n = random.choice([5,7,9])
    else:
        n = random.choice([6,8])

    numbers = []
    for i in range(n):
        addition = 0
        if decimal == 1:
            addition = round(random.random(),1)
        num = random.randint(5,20) + addition
        numbers.append(num)

    med = np.median(numbers)

    q = 'Find the median of: '
    for n in range(len(numbers)):
        q = q + (str(numbers[n]))
        if n != len(numbers)-1:
            q = q + ', '
    a = str(med)

    return q,a

def gen_median(n,b,c,d,e,f):
    qs = []
    ans = []
    i = 0
    while i < n:
        if i < 4:
            q,a = find_median(0,0)
        else:
            q,a = find_median(random.randint(0,1), random.randint(0,1))

        if q not in qs:
            qs.append(q)
            ans.append(a)
            i = i + 1

    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': ans}
