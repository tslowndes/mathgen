import random

def name_the_value(a1=0, a2=0, a3=0, a4=0, a5=0, a6=0):
    value = random.random()
    multiplier = random.choice([10,100,1000,10000, 100000,1000000, 10000000, 100000000, 1000000000])
    value = str(round(value * multiplier, random.randint(0,3)))
    u = random.randint(0,len(value)-1)

    while value[u] == '.' or value[u] == '0':
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


