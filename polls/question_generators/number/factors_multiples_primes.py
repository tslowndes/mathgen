import random
from functools import reduce
import numpy as np

def factors(n):
    return list(set(reduce(list.__add__,
                           ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def list_factors():
    number = random.randint(2, 10) * random.randint(2, 10)
    facts = factors(number)

    question = 'List the factors of ' + str(number)
    answer = ''
    for i in range(len(facts)):
        if i > 0:
            answer = answer + ', ' + str(facts[i])
        else:
            answer = answer + str(facts[i])

    return question, answer


def gen_list_factors(n, b, c, d, e, f):
    qs = []
    anss = []

    while len(qs) < n:
        q, a = list_factors()
        if q not in qs:
            qs.append(q)
            anss.append(a)

    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': anss}


def list_multiples():
    number = random.randint(2, 12)
    question = 'List the first five multiples of ' + str(number)
    answer = ''
    for i in range(1, 6):
        if i == 1:
            answer = str(number)
        else:
            answer = answer + ', ' + str(number * i)

    return question, answer


def gen_list_multiples(n, b, c, d, e, f):
    qs = []
    anss = []

    for i in range(n):
        q, a = list_multiples()
        qs.append(q)
        anss.append(a)
    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': anss}


def HCF(n_max):
    primes = [2, 3, 5, 7]
    HCF = 1
    n = random.randint(2,n_max)
    n1 = random.choice(primes)
    n2 = random.choice(primes)
    numbers1 = [n1] + [n2] + [random.choice(primes)]
    numbers2 = [n1] + [n2] + [random.choice(primes)]
    while np.prod(numbers1)==np.prod(numbers2):
        numbers1 = [n1] + [n2] + [random.choice(primes)]
        numbers2 = [n1] + [n2] + [random.choice(primes)]

    for prime in primes:
        n1 = numbers1.count(prime)
        n2 = numbers2.count(prime)
        n = min([n1, n2])
        HCF = HCF * (prime ** n)

    numbers1 = np.prod(numbers1)
    numbers2 = np.prod(numbers2)

    q = 'Find the HCF of ' + str(numbers1) + ' and ' + str(numbers2)
    a = HCF
    return q, a

def LCM(max_n):
    primes = [2, 3, 5, 7]

    numbers1 = random.randint(5, max_n)
    numbers2 = random.randint(5, max_n)
    lcm = numbers1 * numbers2
    while lcm == numbers1 * numbers2 or lcm == numbers1 or lcm == numbers2:
        numbers1 = random.randint(5, max_n)
        numbers2 = random.randint(5, max_n)
        while numbers1 == numbers2:
            numbers1 = random.randint(5, max_n)
            numbers2 = random.randint(5, max_n)
        lcm = np.lcm(numbers1, numbers2)

    q = 'Find the LCM of ' + str(numbers1) + ' and ' + str(numbers2)
    a = str(lcm)

    return q,a

def gen_LCM(n,b,c,d,e,f):
    qs = []
    ans = []
    i = 0
    while i < n:
        if i < 6:
            q,a = LCM(15)
        else:
            q,a = LCM(30)

        if q not in qs:
            qs.append(q)
            ans.append(a)
            i = i + 1

    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': ans}

def gen_HCF(n,b,c,d,e,f):
    qs = []
    anss = []

    for i in range(n):
        if i < 6:
            n_max = 3
        else:
            n_max = 5
        q, a = HCF(n_max)
        qs.append(q)
        anss.append(a)
    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': anss}



def product_of_primes(bigones=0):
    if bigones == 1:
        primes = [2, 3, 5, 7, 11, 13, 17]
    else:
        primes = [2, 3, 5]
    numbers = random.randint(2, 4)
    product = [random.choice(primes) for i in range(numbers)]

    product.sort()
    unique = list(set(product))

    number = 1
    for n in product:
        number = number * n

    format = ''
    times = ''
    unique.sort()

    for n in unique:
        if unique.index(n) == 0:
            times = ''
        else:
            times = r'\times'
        if product.count(n) == 1:
            format = format + times + str(n)
        else:
            format = format + times + str(n) + '^' + str(product.count(n))
    answer = '$' + format + '$'
    question = 'Write ' + str(number) + ' as a product of its prime factors.'

    return question, answer


def gen_product_of_primes(n, b, c, d, e, f):
    qs = []
    anss = []
    i=0
    while i < n:
        if i < 6:
            q, a = product_of_primes(0)
        else:
            q, a = product_of_primes(1)

        if q not in qs:
            qs.append(q)
            anss.append(a)
            i = i + 1

    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': anss}
