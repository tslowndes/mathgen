import random
from polls.question_generators.tools import *

def name_the_value(a1=0, a2=0, a3=0, a4=0, a5=0, a6=0):
    value = random.random()
    multiplier = random.choice([10000, 100000,1000000, 10000000, 100000000, 1000000000])
    value = str(round(value * multiplier, random.randint(0,3)))
    u = random.randint(0,len(value)-1)

    while value[u] == '.':
        u = random.randint(0, len(value)-1)

    question = '$' + value[:u] + r'\underline{' + value[u] + '}' + value[u+1:] + '$'
    decimal_pnt = value.find('.')
    column = decimal_pnt - u
    col_name = get_column(column)
    answer = value[u] + col_name
    return question, answer

def get_column(col_num):
    columns = {
        -3: " thousandths",
        -2: " hundredths",
        -1: " tenths",
        1: " units",
        2: " tens",
        3: " hundred",
        4: " thousand",
        5: " ten thousand",
        6: " hundred thousand",
        7: " million",
        8: "ten million",
        9: "hundred million",
        10: "billion",
    }
    return columns.get(col_num, "Invalid month")

def gen_name_the_value(n,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(n):
        q,a = name_the_value()


        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def gen_comparing_numbers(a,b,c,d,e,f):
    n = 10
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(n):
        q,a = comparing_numbers(0,0)
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}


def comparing_numbers(dec,neg):
    ind = random.randint(4,7)
    n1 = random.randint(1*10**ind, 10**(ind+1))
    temp = str(n1)
    l1 = random.randint(1,len(temp)-2)
    n2 = temp[:l1] + temp[l1+1] + temp[l1] + temp[l1+2:]
    n1n = n1
    n2n = n2
    n1 = readable_digits(n1,0,1)
    n2 = readable_digits(n2,0,1)
    if random.randint(0,1) == 0:
        q = '$' + str(n1) + ' \; [ \;\;\;  ] \; ' + str(n2) + '$'
        if n1n > int(n2n):
            ans =  '$' + str(n1) + r' \;\; > \;\;' + str(n2) + '$'
        elif n1n<int(n2n):
            ans =  '$' + str(n1) + r' \;\; < \;\;' + str(n2) + '$'
        else:
            ans =  '$' + str(n1) + r' \;\; = \;\;' + str(n2) + '$'
    else:
        q = '$' + str(n2) + ' \; [ \;\;\;  ] \; ' + str(n1) + '$'
        if n1n > int(n2n):
            ans =  '$' + str(n2) + r' \;\; < \;\;' + str(n1) + '$'
        elif n1n<int(n2n):
            ans =  '$' + str(n2) + r' \;\; > \;\;' + str(n1) + '$'
        else:
            ans =  '$' + str(n2) + r' \;\; = \;\;' + str(n1) + '$'


    return q,ans



def gen_multiplying_by_10(multi_div,decimal, places,d,e,f):
    n = 10
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(n):
        q,a = multiplying_by_10(multi_div,decimal, places)
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def multiplying_by_10(multi_div,decimal, places):
    a = round(random.random(),int(places))
    while a == 0:
        a = round(random.random(),int(places))
    if multi_div == 0:
        b = random.randint(0,20)
    else:
        b = random.randint(20,400)
    if multi_div == 1:
        if len(str(b)) == 3:
            if random.randint(0,1)==0:
                b = int(str(b)[0] + '0' + str(b)[2])
            else:
                b = int(str(b)[0] + str(b)[1] + '0')
        elif len(str(b)) == 2:
            b = int(str(b)[0] + '0')
    else:
        if random.randint(0,1) == 0:
            a = float(str(a)[1] + '0' + str(a)[2:])

    a = a + b

    power_of_ten = random.choice([10,100,1000])


    if multi_div == 0:
        q = '$' + strip_0(a) + r'\times' + str(power_of_ten) + '$'
        ans = a * power_of_ten
    else:
        q = '$' + strip_0(a) + r'\div' + str(power_of_ten) + '$'
        ans = a / power_of_ten

    return q, ans