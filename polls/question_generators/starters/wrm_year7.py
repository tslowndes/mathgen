import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.number.fdp_conversions import *
from polls.question_generators.algebra.linear_sequences import *
from polls.question_generators.algebra.collecting_like_terms import *
from polls.question_generators.algebra.solving_equations import *
from polls.question_generators.number.place_value import *

def gen_white_rose_maths_starter(year, ht, a2, a3, a4, a5):
    count = [i for i in range(8)]
    questions = [0 for i in range(8)]
    answers = [0 for i in range(8)]
    questions[0], answers[0] = gen_linear_sequences(0, 0, 0, 0, 0, 0)
    questions [0] = 'Find the next term: ' + questions[0]
    questions[1], answers[1] = gen_linear_sequences(1, 0, 0, 0, 0, 0)
    questions [1] = 'Find the next term: ' + questions[1]
    questions[2], answers[2] = gen_adding_algebra_terms(0, 0, 0, 0, 0, 0)
    questions [2] = 'Simplify: ' + questions[2]
    out = gen_solving_equations(1, 0, 0, 1, 0, 0)
    questions[3] = 'Solve the equation: ' + out['questions'][0]
    answers[3] = out['answers'][0]
    questions[4], answers[4] = frac_to_percentage()
    questions[4] = r'Convert the fraction to a percentage: ' + questions[4]
    questions[5], answers[5] = frac_to_decimal()
    questions[5] = r'Convert the decimal to a fraction: ' + str(questions[5])
    answers[5] = answers[5]
    questions[6], answers[6] = name_the_value()
    questions[6] = 'What is the value of the underlined digit? ' + questions[6]

    return {'count': count,
            'questions': questions,
            'answers': answers}