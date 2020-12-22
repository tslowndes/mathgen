import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *

def gen_linear_sequences(add_or_subtract, neg_first_term, a3, a4, a5, a6):
    if neg_first_term == 1:
        first_term = random.randint(-1,-20)
    else:
        first_term = random.randint(0, 20)

    common_difference = random.randint(2, 15)
    if add_or_subtract == 1:
        common_difference = common_difference * -1
    terms = ''
    for i in range(0,5):
        if i != 0:
            terms = terms + ', ' + str(first_term + i * common_difference)
        else:
            terms = terms + str(first_term + i * common_difference)
    answer = first_term + 5 * common_difference

    return terms, answer