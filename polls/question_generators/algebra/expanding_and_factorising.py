import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *

def gen_expanding_brackets(powers,a2,a3,a4,a5,a6):
    qs = []
    ans = []
    count = []
    ### Generates expanding brackets questions in the form c(ax + b)
    for i in range(0,10):
        a = random.randint(1,10)
        b = rand_no0(-10,10)
        c = random.randint(2,10)

        if powers == 1 or powers == 2:
            if powers == 1:
                a_ind = random.randint(1,2)
                c_ind = 1
            else:
                a_ind = random.randint(1,3)
                c_ind = random.randint(1,3)

            expanded = tidy_algebra(str(c*a) + 'x^' + str(a_ind+c_ind) + ' + ' + str(c*b) + 'x^' + str(c_ind))
            factorised = tidy_algebra(str(c) + 'x^' + str(c_ind) +'(' + str(a) + 'x^' + str(a_ind) + ' + ' + str(b) + ')')
        else:

            expanded = tidy_algebra(str(c*a) + 'x' + ' + ' + str(c*b))
            factorised = tidy_algebra(str(c) + '(' + str(a) + 'x' + ' + ' + str(b) + ')')

        qs.append('$' + factorised + '$')
        ans.append('$' + expanded + '$')
        count.append(i)

    context = {
        'count':count,
        'questions':qs,
        'answers':ans,
    }

    return context

def expanding_binomials(x_or_ax=0):
    if x_or_ax == 0:
        alpha = get_alpha()
        bin_1_b = rand_no0(-9,9)
        bin_2_b = rand_no0(-9,9)
        exp_b = bin_1_b + bin_2_b
        exp_c = bin_1_b * bin_2_b

        bin_1 = tidy_algebra(alpha + ' + ' + str(bin_1_b))
        bin_2 = tidy_algebra(alpha + ' + ' + str(bin_2_b))

        question = 'Expand: $(' + bin_1 + ')(' + bin_2 + ')$'

        answer = tidy_algebra('$' + alpha + '^2 + ' + str(exp_b) + alpha + ' + ' + str(exp_c) + '$')

    return question, answer