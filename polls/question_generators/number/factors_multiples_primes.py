import random
from functools import reduce
import numpy as np
from polls.question_generators.tools import *

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
    if random.randint(0,1)==0:
        question = 'List the first five multiples of ' + str(number)
        answer = ''
        for i in range(1, 6):
            if i == 1:
                answer = str(number)
            else:
                answer = answer + ', ' + str(number * i)
    else:
        a = random.randint(5,20)
        b = random.randint(5,12)
        if random.randint(0,1) == 1:
            question = 'Find the ' + str(a) + 'th multiple of ' + str(b)
            answer = a * b
        else:
            question = strip_0(a*b) + ' is the ' + str(a) + 'th multiple of what number?'
            answer = b

    return question, answer


def gen_list_multiples(n, b, c, d, e, f):
    qs = []
    anss = []

    i=0
    while i < n:
        q, a = list_multiples()
        while q in qs:
            q, a = list_multiples()
        i+=1
        qs.append(q)
        anss.append(a)
    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': anss}


def HCF(n_max, i=4):
    primes = [2, 3, 5]
    HCF = 1
    n = random.randint(2,n_max)

    #n1 = [random.choice([2,3]) for i in range(n)]
    if i < 2:
        n1 = random.choice([1])
        n2 = random.choice([2,3,5])
    elif i < 6:
        n1 = random.choice([2,3])
        n2 = random.choice([2,3,5])
    else:
        n1 = random.choice([2,3,5])
        n2 = random.choice([2,3,5,7])
    numbers1 = [n1] + [n2] + [random.choice(primes)]
    numbers2 = [n1] + [n2] + [random.choice(primes)]
    while np.prod(numbers1)==np.prod(numbers2):
        numbers1 = [n1] + [n2] + [random.choice(primes)]
        numbers2 = [n1] + [n2] + [random.choice(primes)]
    #numbers1 = [n1] + [random.choice(primes)]
    #numbers2 = [n1] + [random.choice(primes)]
    #while np.prod(numbers1)==np.prod(numbers2):
    #    numbers2 = [n1] + [random.choice(primes)]

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
        if i < 7:
            n_max = 3
        else:
            n_max = 4
        q, a = HCF(n_max, i)
        qs.append(q)
        anss.append(a)
    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': anss}

def gen_product_of_primes_hcf(hcf_lcm,a2,a3,a4,a5,a6):
    qs = []
    anss = []
    i=0
    n=8
    while i < n:
        if hcf_lcm != 2:
            q,a = product_of_primes_hcf(hcf_lcm)
        else:
            q,a = product_of_primes_hcf(random.randint(0,1))

        qs.append(q)
        anss.append(a)
        i = i + 1

    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': anss}

def product_of_primes_hcf(hcf_lcm):
    primes = [2,3,5,7]

    three = [random.choice(primes) for i in range(3)]

    a = three + [random.choice(primes)]
    b = three + [random.choice(primes)]
    a_prod = calc_product(a)
    b_prod = calc_product(b)

    while a_prod == b_prod:
        b = three + [random.choice(primes)]
        b_prod = calc_product(b)

    a_format = format_product_of_primes(a)
    b_format = format_product_of_primes(b)

    hcf = calc_product(three)

    if hcf_lcm == 0:
        question = "  $" + str(a_prod) + " = " + a_format + "$ $" + str(b_prod) + " = " + b_format + "$ Find the HCF of " + str(a_prod) + " & " + str(b_prod) + "."
        ans = hcf
    else:
        question = "  $" + str(a_prod) + " = " + a_format + "$ $" + str(b_prod) + " = " + b_format + "$ Find the LCM of " + str(a_prod) + " & " + str(b_prod) + "."
        ans = strip_0(calc_product(three) * (a_prod/hcf) * (b_prod/hcf))




    return question, ans

def calc_product(product):
    number = 1
    for n in product:
        number = number * n
    return number

def format_product_of_primes(product):
    product.sort()
    unique = list(set(product))
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
    return format

def product_of_primes(numbers=3,bigones=0):
    if bigones == 1:
        primes = [2, 3, 5, 7, 11, 13, 17]
        primes = [2,3,5,7]
    else:
        primes = [2, 3, 5]
    #numbers = random.randint(2, 4)
    product = [random.choice(primes) for i in range(numbers)]

    number = calc_product(product)
    format = format_product_of_primes(product)


    answer = '$' + format + '$'
    question = 'Write ' + str(number) + ' as a product of its prime factors.'

    return question, answer


def gen_product_of_primes(n, b, c, d, e, f):
    qs = []
    anss = []
    i=0
    while i < n:
        if i < 2:
            q, a = product_of_primes(2,0)
        elif i < 4:
            q, a = product_of_primes(random.randint(3,4),0)
        elif i < 8:
            q,a = product_of_primes(random.randint(4,5),0)
        else:
            q, a = product_of_primes(random.randint(4,5),1)

        if q not in qs:
            qs.append(q)
            anss.append(a)
            i = i + 1

    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': anss}
