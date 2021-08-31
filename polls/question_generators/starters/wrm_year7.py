import os, sys
sys.path.append(os.path.join('../../', "lib"))
import random
from polls.question_generators.number.fdp_conversions import *
from polls.question_generators.algebra import linear_sequences
from polls.question_generators.algebra.collecting_like_terms import *
from polls.question_generators.algebra.solving_equations import *
from polls.question_generators.number.place_value import *
from polls.question_generators.data.averages import *
from polls.question_generators.number.ratio import *
from polls.question_generators.number.direct_proportion import *
from polls.question_generators.number.fractions import *
from polls.question_generators.algebra import linear_graphs
from polls.question_generators.data.types_of_data import *
from polls.question_generators.data.probability import *
from polls.question_generators.number import factors_multiples_primes
from polls.question_generators.algebra import inequalities
from polls.question_generators.algebra import expanding_and_factorising
from polls.question_generators.shape import pythagoras
from polls.question_generators.shape import cuboid, parallelogram
from polls.question_generators.number import arithmetic
from polls.question_generators.number import money
from polls.question_generators.number import negatives, fractions, standard_form, percentages,rounding
from polls.question_generators.algebra import inequalities
from polls.question_generators.algebra import indices
from polls.question_generators.shape import angles, shape_facts, circles


def gen_white_rose_maths_starter(year, ht, a2, a3, a4, a5):
    print('ht = ' + str(ht))
    if year == 7:
        context = wrm_7_starter(ht)
    elif year == 8:
        context = wrm_8_starter(ht)
    elif year == 9:
        context = wrm_9_starter(ht)

    return context


def wrm_7_starter(ht):
    count = [i for i in range(8)]
    questions = [0 for i in range(24)]
    answers = [0 for i in range(24)]
    j = 0
    if ht == 1: 
        questions[j], answers[j] = arithmetic.times_tables(6,random.randint(0,1))
        j+=1
        questions[j], answers[j] = arithmetic.addition(0,0)
        j+=1
        questions[j], answers[j] = arithmetic.addition(0,1)
        j+=1
        questions[j], answers[j] = arithmetic.long_mult(0)
        j+=1
        
        
    if ht == 1 or ht ==2:
        questions[j], answers[j] = arithmetic.long_mult(1)
        j+=1
        questions[j], answers[j] = arithmetic.order_of_operations()
        j+=1
        questions[j], answers[j] = rounding.round_to_nearest()
        j+=1
        questions[j], answers[j] = fractions.adding_fractions(1, 0, 0, 0)
        j += 1

    if ht == 2 or ht == 3:
        questions[j], answers[j] = linear_sequences.find_the_next_term(0, 0, 0, 0, 0, 0)
        questions[j] = 'Find the next term: ' + questions[j]
        j += 1
        questions[j], answers[j] = linear_sequences.find_the_next_term(1, 0, 0, 0, 0, 0)
        questions[j] = 'Find the next term: ' + questions[j]
        j += 1
        questions[j], answers[j] = adding_algebra_terms(0, 0, 0, 0, 0, 0)
        questions[j] = 'Simplify: ' + questions[j]
        j += 1
        questions[j], answers[j] = gen_solving_equations(1, 0, 0, 1, 0, 0)
        questions[j] = 'Solve the equation: ' + questions[j]
        j += 1
    if ht == 3 or ht == 4:
        questions[j], answers[j] = frac_to_percentage()
        questions[j] = r'Convert the fraction to a percentage: ' + questions[j]
        j += 1
        questions[j], answers[j] = frac_to_decimal()
        questions[j] = r'Convert the decimal to a fraction: ' + str(questions[j])
        j += 1
        questions[j], answers[j] = name_the_value()
        questions[j] = 'What is the value of the underlined digit? ' + questions[j]
        j += 1
        a = random.randint(0,1)
        questions[j], answers[j] = [gen_range(), find_median(0,0)][a]
        if a == 0:
            questions[j] = 'Find the range of: ' + questions[j]
        j += 1
    if ht == 4 or ht == 5:
        questions[j], answers[j] = random.choice([arithmetic.addition(), arithmetic.mental_addition()])
        j += 1
        questions[j], answers[j] = money.basic_purchase(1)
        j += 1
        questions[j], answers[j] = random.choice([factors_multiples_primes.list_factors(), factors_multiples_primes.list_multiples()])
        j += 1
        questions[j], answers[j] = arithmetic.multiply_decimals()
        j += 1
    if ht == 5 or ht == 6:
        questions[j], answers[j] = gen_solving_equations(1, 1, 0, 2, 0, 0)
        j += 1
        questions[j], answers[j] = negatives.negative_addition(random.randint(3,4), 0)
        j += 1
        questions[j], answers[j] = fractions.mixed_numbers(random.randint(0,1))
        j += 1
        questions[j], answers[j] = fractions.adding_fractions(0, 0, 0, 0)
        j += 1

    if ht == 6:
        questions[j], answers[j] = angles.basic_angle_facts()
        j+=1
        questions[j], answers[j] = angles.angles_on_a_straight_line(2)
        j+=1
        questions[j], answers[j] = shape_facts.polygon_names()
        j+=1
        questions[j], answers[j] = shape_facts.classify_angles()
        j+=1
    return {'count': count,
            'questions': questions,
            'answers': answers}

def wrm_8_starter(ht):
    print('ht = ' + str(ht))
    count = [i for i in range(8)]
    questions = [0 for i in range(8)]
    answers = [0 for i in range(8)]
    j = 0
    if ht == 1:
        starter = wrm_7_starter(random.randint(2,6))
        questions = starter['questions']
        answers = starter['answers']
    
    if ht == 2:
        starter = wrm_7_starter(random.randint(2,6))
        questions[0:4] = starter['questions'][4:8]
        answers[0:4] = starter['answers'][4:8]
        j = 4
    
    if ht == 2 or ht == 3:
        questions[j], answers[j] = sharing_into_ratio(5, 6)
        j += 1
        questions[j], answers[j] = simplify_ratio()
        questions[j] = 'Simplify the ratio ' + questions[j]
        j += 1
        questions[j], answers[j] = currency_conversion()
        j += 1
        if random.randint(0,1) == 1:
            questions[j], answers[j] = multiplying_fractions()
        else:
            questions[j], answers[j] = multiplying_fraction_by_integer()
        j += 1

    if ht == 3 or ht == 4:
        questions[j], answers[j] = dividing_fractions()
        j += 1
        questions[j], answers[j] = linear_graphs.point_on_the_line()
        j += 1
        if random.randint(0,1) == 1:
            questions[j], answers[j] = discrete_or_continuous()
        else:
            questions[j], answers[j] = qual_or_quant()
        j += 1
        if random.randint(0,1) == 1:
            questions[j], answers[j] = fair_dice()
        else:
            questions[j], answers[j] = spinner()
        j += 1

    if ht == 4 or ht == 5:
        a = expanding_and_factorising.gen_expanding_brackets(0, 0, 0, 0, 0, 0)
        questions[j], answers[j] = a['questions'][0], a['answers'][0]
        questions[j] = 'Expand ' + questions[j]
        j+=1
        questions[j], answers[j] = inequalities.solving_inequalities(1,1,0,2,0,0)
        j+=1
        a = random.randint(0,1)
        b = [linear_sequences.generate_from_nth(0,0,0),linear_sequences.generate_from_nth(0,0,1)]
        if a == 1:
            questions[j] = r'Find the nth term of the sequence $ $' + b[a][0]
            answers[j] = b[a][1]
        else:
            questions[j] = b[a][0]
            answers[j] = b[a][1]
        j+=1
        questions[j], answers[j] = indices.laws_of_indices_multiplying(2,2,0)
        j+=1
        
    if ht == 5 or ht == 6:
        questions[j], answers[j] = percentages.percentages_non_calc(-1,random.randint(0,1),random.randint(0,1), 0, random.randint(1,2))
        j+=1
        questions[j], answers[j] = standard_form.standard_form_large(9, 1, 0, random.randint(0,1))
        questions[j] = "Write " + str(questions[j]) + " in standard form."
        j+=1
        dp = random.randint(1,3)
        questions[j], answers[j] = rounding.rounding(0,dp)
        questions[j] = "Round " + str(questions[j]) + " to " + str(dp) + " decimal places."
        j+=1
        questions[j], answers[j] = money.basic_purchase(1)
        j+=1
    if ht == 6:
        # interior angles 
        # exterior angles
        # area of circles
        questions[j], answers[j] = circles.circle_measure(random.randint(0,1), random.randint(0,1), 0)
        j+=1
        # area of trapezia
        questions[j], answers[j] = parallelogram.area_of_parallelogram(0, 1, 0, 1)
        j+=1




    return {'count': count,
            'questions': questions,
            'answers': answers}

def wrm_9_starter(ht):
    count = [i for i in range(8)]
    questions = [0 for i in range(8)]
    answers = [0 for i in range(8)]

    questions[0], answers[0] = random.choice([linear_graphs.form_equation(), linear_graphs.m_and_c_from_equation()])
    questions[1], answers[1] = linear_graphs.line_on_points()
    questions[2],answers[2] = gen_solving_equations(1, 1, 0, 2, 1, 0)
    questions[3], answers[3] = inequalities.solving_inequalities(1, 1, 0, 2, 0, 0)
    questions[4], answers[4] = random.choice([factors_multiples_primes.list_factors(), factors_multiples_primes.list_multiples(), factors_multiples_primes.product_of_primes()])
    questions[5], answers[5] = expanding_and_factorising.expanding_binomials(0)
    questions[6], answers[6] = random.choice([cuboid.cuboid(), cuboid.triangular_prism()])





    return {'count': count,
            'questions': questions,
            'answers': answers}