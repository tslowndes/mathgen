import random

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