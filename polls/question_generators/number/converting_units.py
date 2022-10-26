import random

def converting_lengths():
    a = round(random.random(),3)
    units = ['mm','cm','mm','km']
    unit1 = random.choice(units)
    unit2 = random.choice(units)
    while unit1 == unit2:
        unit2 = random.choice(units)

    multipliers = [1000,100,1,0.001]
    n1 = a * multipliers[units.index(unit1)]
    n2 = a * multipliers[units.index(unit2)]

    q =  '$' + str(n1) + unit1 + r' = \left [ \;\; ]\right ' + unit2 + '$'
    ans = n2
    return q,ans


def gen_converting_units(units,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(10):
        q,a = converting_lengths()


        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}
