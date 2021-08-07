import random

def numerical_indices(non_calc):
    n = random.randint(1,12)
    if non_calc == 1:
        if n == 1 or n == 2 or n == 10:
            max_power = 6
        elif n==3:
            max_power = 4
        elif n==4 or n==5:
            max_power = 3
        else:
            max_power = 2

        power = random.randint(2, max_power)
    else:
        power = random.randint(5,10)



    q = '$' + str(n) + '^{' + str(power) + '}' + '$'
    ans = n ** power

    return q,ans

def gen_numerical_indices(n,non_calc,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(n):

        q,a = numerical_indices(non_calc)

        while q in questions:
            q,a = numerical_indices(non_calc)

        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

