import random

def negative_addition(type, additive_inverse=0):
    # type 1 1 - 2
    # type 2 -1 + 2
    # type 3 2 + -1
    # type 4 2 - - 1
    # type 5 -1 - 2
    if type > 5:
        type = random.randint(1,4)

    neg = random.randint(-10,-1)
    non_neg = random.randint(1,10)
    if type == 0:
        a,b = random.randint(1,10), random.randint(1,10)
        if a > b:
            q = '$' + str(b) + ' - ' + str(a) + '$'
            ans = b - a
        else:
            q = '$' + str(a) + ' - ' + str(b) + '$'
            ans = a-b
    elif type == 1:
        a,b = random.randint(1,10), random.randint(1,10)
        if a > b:
            q = '$-' + str(b) + ' + ' + str(a) + '$'
            ans = (-1*b) + a
        else:
            q = '$-' + str(a) + ' + ' + str(b) + '$'
            ans = (-1*a)+b
    elif type == 2:
        q = '$' + str(neg) + ' + ' + str(non_neg) + '$'
        ans = neg + non_neg
    elif type == 3:
        q = '$' + str(non_neg) + ' + ' + str(neg) + '$'
        ans = non_neg + neg
    elif type == 4:
        q = '$' + str(non_neg) + ' - ' + str(neg) + '$'
        ans = non_neg - neg
    elif type == 5:
        q = '$' + str(neg) + ' - ' + str(non_neg) + '$'
        ans = neg - non_neg
    ans = '$' + str(ans) + '$'
    return q,ans

def gen_crossing_zero(n,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]
    type = [0,0,0,0,0,1,1,1,1,1]
    random.shuffle(type)
    for i in range(10):
        q,a = negative_addition(type[i])
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def gen_adding_negatives(n,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(10):
        q,a = negative_addition(i+1)
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}
