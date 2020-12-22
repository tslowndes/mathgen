import random
from polls.question_generators.tools import *

def sharing_into_ratio():
    ### b:c where a is 1 part

    a = random.randint(5,10)
    b = random.randint(3,10)
    c = random.randint(3,10)

    total = (b*a) + (c*a)

    question = name_chooser() + ' and ' + name_chooser() + ' share £' + str(total) + ' in the ratio ' + str(b) + ':' + str(c) + '. How much does each person get.'
    answer = '£' + str(b*a) + ':£' + str(c*a)

    return question, answer