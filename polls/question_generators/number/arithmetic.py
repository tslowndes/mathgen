import random

def mental_addition():
    a = random.choice([100 - random.randint(1,3), 100 + random.randint(1,3)])
    b = random.randint(150,250)
    if random.randint(0,1) == 0:
        q = '$' + str(b) + ' + ' + str(a) + '$'
        ans = b + a
    else:
        q = '$' + str(b) + ' - ' + str(a) + '$'
        ans = a - b

    return q, ans

def addition():
    a = round(random.random(),random.randint(2,4))
    b = round(random.random(),random.randint(2,4))

    q = '$' + str(a) + ' + ' + str(b) + '$'
    ans = a + b

    return q, ans

def gen_mental_addition(n,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q,a = mental_addition()
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}

def gen_addition(n,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        q,a = addition()
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}

def multiply_decimals():
    a = round(random.random(), 1)
    b = round(random.random(), 2)

    q = '$' + str(a) + r'\times' + str(b) + '$'
    ans = a * b

    return q,ans
