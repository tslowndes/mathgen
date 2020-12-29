import random
from functools import reduce

def factors(n):
    return list(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def list_factors():
    number = random.randint(15,50)
    facts = factors(number)

    question = 'List the factors of ' + str(number)
    answer = ''
    for i in range(len(facts)):
        if i > 0:
            answer = answer + ', ' + str(facts[i])
        else:
            answer = answer + str(facts[i])

    return question, answer

def list_multiples():
    number = random.randint(2,12)
    question = 'List the first five multiples of ' + str(number)
    answer = ''
    for i in range(1,6):
        if i == 1:
            answer = str(number)
        else:
            answer = answer + ', ' +  str(number * i)

    return question, answer

def product_of_primes(bigones=0):
    if bigones == 1:
        primes = [2,3,5,7,11,13,17]
    else:
        primes = [2,3,5,7]
    numbers = random.randint(2,4)
    product = [random.choice(primes) for i in range(numbers)]

    product.sort()
    unique = list(set(product))

    number = 1
    for n in product:
        number = number * n

    format = ''
    times = ''
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