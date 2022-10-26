import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *
import math

def gen_expanding_brackets(powers,neg_coefficient,diff_letters,a4,a5,a6):
    qs = []
    ans = []
    count = []
    ### Generates expanding brackets questions in the form c(ax + b)
    for i in range(0,10):
        alpha = get_alpha()
        a = random.randint(1,10)
        b = rand_no0(-10,10)
        if i < 4:
            if neg_coefficient == 0:
                c = random.randint(2,4)
            else:
                c = random.randint(-4,-2)
        else:
            if neg_coefficient == 0:
                c = random.randint(2,10)
            else:
                c = random.randint(-10,-2)

        if powers == 1 or powers == 2:
            if powers == 1:
                a_ind = 1
                c_ind = 1
            else:
                a_ind = random.randint(1,3)
                c_ind = random.randint(1,3)

            if random.randint(0,1) == 1:
                expanded = tidy_algebra(str(c*a) + alpha + '^' + str(a_ind+c_ind) + ' + ' + str(c*b) + alpha + '^' + str(c_ind))
                factorised = tidy_algebra(str(c) + alpha + '^' + str(c_ind) +'(' + str(a) + alpha + '^' + str(a_ind) + ' + ' + str(b) + ')')
            else:
                if b < 0:
                    b = b *-1
                    a = a *-1
                expanded = tidy_algebra(str(c*b) + alpha + '^' + str(c_ind) + ' + ' + str(c*a) + alpha + '^' + str(a_ind+c_ind))

                factorised = tidy_algebra(str(c) + alpha + '^' + str(c_ind) +'(' + str(b)  + ' + ' + str(a) + alpha + '^' + str(a_ind) + ')')

        else:
            if diff_letters == 1:
                alpha2 = get_alpha()
                while alpha== alpha2:
                    alpha2 = get_alpha()
            else:
                alpha2 = ''

            if random.randint(0,1)==0:
                factorised = tidy_algebra(str(c) + alpha2 + '(' + str(a) + alpha + ' + ' + str(b) + ')')
                sorted_characters = sorted(alpha + alpha2)
                a_string = "".join(sorted_characters)
                expanded = tidy_algebra(str(c*a) + a_string + ' + ' + str(c*b) + alpha2)
            else:
                factorised = tidy_algebra(str(c) + alpha2 + '(' + str(a) + ' + ' + str(b) + alpha + ')')
                sorted_characters = sorted(alpha + alpha2)
                a_string = "".join(sorted_characters)
                expanded = tidy_algebra(str(c*a) + alpha2 + ' + ' + str(c*b) + a_string )

        qs.append('$' + factorised + '$')
        ans.append('$' + expanded + '$')
        count.append(i)

    context = {
        'count':count,
        'questions':qs,
        'answers':ans,
    }

    return context

def gen_factorising(single_double, indices, neg_xs, multiple_unknowns,a5,a6):
    qs = []
    ans = []
    count = [i for i in range(0, 10)]
    ### Generates expanding brackets questions in the form c(ax + b)
    for i in range(0,10):
        q,a = factorise_single_brackets(0,0,multiple_unknowns)

        qs.append(q)
        ans.append(a)

    context = {
        'count':count,
        'questions':qs,
        'answers':ans,
    }

    return context

def factorise_single_brackets(indices, neg_xs,multiple_unknowns=0):
    letters1 = ['a','b','c','d','e','f','g','h','j','k','l','m']
    letters2 = ['n','p','q','r','s','t','u','v','w','x','y','z']

    a = random.randint(2,10)
    b = random.randint(2,10)
    while a == b:
        a = random.randint(2,10)
    if random.randint(0,1)==1:
        b=-1*b
    fac = random.randint(2,5)

    alpha = random.choice(letters1)
    alpha2 = ''
    if multiple_unknowns==1:
        alpha2 = random.choice(letters2)

    hcf = math.gcd(a*fac, b*fac)

    if random.randint(0,multiple_unknowns) == 0:

        q = tidy_algebra(str(a*fac) + alpha + alpha2 + " + " + str(b*fac) + alpha2)

        ans = "$" + tidy_algebra(str(hcf) + alpha2 + "(" + tidy_algebra(strip_0(str((a*fac)/hcf))+ alpha + " + " + strip_0(str((b*fac)/hcf))) + ")") + "$"

    else:

        q = tidy_algebra(str(a*fac) + alpha + " + " + str(b*fac) + alpha + alpha2)

        ans = "$" + tidy_algebra(str(hcf) +  alpha + "(" + tidy_algebra(strip_0(str((a*fac)/hcf))+ " + " + strip_0(str((b*fac)/hcf))) + alpha2 + ")") + "$"

    q = "$" + q + "$"

    return q,ans


def gen_expanding_binomials(x_or_ax,a2,a3,a4,a5,a6):
    questions = []
    answers = []
    count = [i for i in range(0, 10)]

    for i in count:
        if i < 4:
            q,a = expanding_binomials(x_or_ax, 0)
        else:
            q,a = expanding_binomials(x_or_ax, 1)

        questions.append(q)
        answers.append(a)
    return {'count':count, 'questions':questions, 'answers':answers}

def expanding_binomials(x_or_ax=0,subtract=1):
    if x_or_ax == 0:
        bin_1_a = 1
        bin_2_a = 1
    else:
        bin_1_a = random.randint(2,5)
        bin_2_a = random.randint(2,5)

    alpha = get_alpha()
    if subtract == 1:
        bin_1_b = rand_no0(-9,9)
        bin_2_b = rand_no0(-9,9)
    else:
        bin_1_b = rand_no0(1,9)
        bin_2_b = rand_no0(1,9)
    exp_a = bin_1_a * bin_2_a
    exp_b = (bin_2_a * bin_1_b) + (bin_1_a * bin_2_b)
    exp_c = bin_1_b * bin_2_b

    bin_1 = tidy_algebra(str(bin_1_a) + alpha + ' + ' + str(bin_1_b))
    bin_2 = tidy_algebra(str(bin_2_a) + alpha + ' + ' + str(bin_2_b))

    question = 'Expand: $(' + bin_1 + ')(' + bin_2 + ')$'

    if exp_b == 0:
        answer = tidy_algebra('$' + str(exp_a) + alpha + '^2 + ' + str(exp_c) + '$')
    else:
        answer = tidy_algebra('$' + str(exp_a) + alpha + '^2 + ' + str(exp_b) + alpha + ' + ' + str(exp_c) + '$')

    return question, answer