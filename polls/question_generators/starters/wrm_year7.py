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
from polls.question_generators.number import percentages
from polls.question_generators.number.standard_form import *
from polls.question_generators.number import negatives, fractions, standard_form, percentages,rounding
from polls.question_generators.algebra import inequalities
from polls.question_generators.algebra import indices
from polls.question_generators.shape import angles, shape_facts, circles, parallelogram, triangles


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
    text = [0 for i in range(24)]
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
            'answers': answers,
            'text':text}

def wrm_8_starter(ht):
    print('ht = ' + str(ht))
    count = [i for i in range(8)]
    questions = [0 for i in range(8)]
    answers = [0 for i in range(8)]
    text = [0 for i in range(8)]
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
        questions[j], answers[j] = simplify_ratio(0)
        questions[j] = 'Simplify the ratio ' + questions[j]
        j += 1
        questions[j], answers[j] = currency_conversion(0)
        j += 1
        questions[j], answers[j] = random.choice([multiplying_fractions(), multiplying_fraction_by_integer(), dividing_fractions()])
        j += 1

    if ht == 3 or ht == 4:

        questions[j], answers[j] = random.choice([linear_graphs.point_on_the_line(), linear_graphs.line_on_points()])
        j+=1

        a = random.randint(1,2)
        if a == 1:
            text[j] = 'What is the y-intercept of the line?\n'
            questions[j], answers[j] = linear_graphs.straight_line_graphs(a,0,1)
        else:
            text[j] = 'What is the equation of the line?\n'
            questions[j], answers[j] = linear_graphs.straight_line_graphs(0,1,1)
        j+=1

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
        text[j] = 'Expand'
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
        questions[j], answers[j] = circles.circle_measure(random.randint(0,1), random.randint(0,1), 0,0)
        j+=1
        # area of trapezia
        questions[j], answers[j] = parallelogram.area_of_parallelogram(0, 1, 0, 1)
        j+=1




    return {'count': count,
            'questions': questions,
            'answers': answers,
            'text':text}

def wrm_9_starter(ht):
    print('ht = ' + str(ht))
    count = [i for i in range(8)]
    questions = [0 for i in range(8)]
    answers = [0 for i in range(8)]
    text = [0 for i in range(8)]
    j = 0
    if ht == 1 or ht == 2:
        starter = wrm_8_starter(random.randint(2,6))
        q = starter['questions']
        a = starter['answers']

        if ht == 1:
            questions = q
            answers = a
        else:
            a = random.randint(0,7)
            b = random.randint(0,7)
            while a == b:
                b = random.randint(0,7)
            questions[j], answers[j] = starter['questions'][a], starter['answers'][a]
            j+=1
            questions[j], answers[j] = starter['questions'][b], starter['answers'][b]
            j+=1

    if ht == 2 or ht == 3:
        if ht == 2:
            questions[j],answers[j] = gen_solving_equations(1, 1, 0, 2, 0, 0)   # n, negs, negxs, steps, bothsides, brackets
            j+=1

            temp = expanding_and_factorising.gen_expanding_brackets(0,0,0,0,0,0)
            text[j] = 'Expand'
            questions[j],answers[j] = temp['questions'][0], temp['answers'][0]
            j += 1


        text[j] = 'What is the equation of the line?\n'
        questions[j], answers[j] = linear_graphs.straight_line_graphs(0,1,1)
        j+=1

        a = random.randint(1,2)
        if a == 1:
            text[j] = 'What is the y-intercept of the line?\n'
        else:
            text[j] = 'What is the gradient of the line?\n'
        questions[j], answers[j] = linear_graphs.straight_line_graphs(a,0,1)
        j+=1

        text[j] = 'Expand:'
        questions[j], answers[j] = expanding_and_factorising.expanding_binomials(0)
        j+=1

        text[j] = 'Solve:'
        questions[j],answers[j] = gen_solving_equations(1, 1, 0, 2, 1, 0)
        j+=1

    if ht == 3 or ht == 4:
        text[j] = 'Find the area of the trapezium:\n'
        questions[j], answers[j] = parallelogram.area_of_parallelogram(0, 1, 0, 1)
        j+=1
        text[j] = 'Find the area of the triangle:\n'
        questions[j], answers[j] = triangles.area_of_triangle(0,0)
        answers[j] = '$' + answers[j] + '$'
        j+=1
        questions[j], answers[j] = random.choice([adding_fractions(0, 0, 0, 0),multiplying_fractions(),dividing_fractions()])
        j+=1
        questions[j],answers[j] = standard_form_large(6, 1, 0, 0)
        questions[j] = 'Write in standard form ' + questions[j]
        j+=1

    if ht == 4 or ht == 5:
        questions[j], answers[j] = percentages.percentages_non_calc(1,1,0,0,0,0)
        j+=1
        text[j] = 'Using your calculator:'
        questions[j], answers[j] = percentages.percentages_non_calc(1,0,1,0,1,0)
        j+=1
        # Maths and Money
        # Compound interest problem
        questions[j], answers[j] = percentages.interest(0)
        j += 1
        # Exchange rate problem
        questions[j], answers[j] = currency_conversion(1)
    if ht == 4 or ht == 5:
        pass


       # questions[j], answers[j] = inequalities.solving_inequalities(1, 1, 0, 2, 0, 0)
        #j+=1
        #questions[j], answers[j] = random.choice([factors_multiples_primes.list_factors(), factors_multiples_primes.list_multiples(), factors_multiples_primes.product_of_primes()])
        #j += 1
        #questions[j], answers[j] = expanding_and_factorising.expanding_binomials(0)
        #j+=1
        #questions[j], answers[j] = random.choice([cuboid.cuboid(), cuboid.triangular_prism()])
        #j+=1


    return {'count': count,
            'questions': questions,
            'answers': answers,
            'text':text}

def y10_foundation_starter(ht):
    count = [i for i in range(8)]
    questions = [0 for i in range(8)]
    answers = [0 for i in range(8)]
    text = [0 for i in range(8)]
    j = 0
    if ht == 1:
        starter = wrm_8_starter(random.randint(2,6))
        questions = starter['questions']
        answers = starter['answers']
    if ht == 2:
        questions[j],answers[j] = gen_solving_equations(1, 1, 0, 2, 0, 0)   # n, negs, negxs, steps, bothsides, brackets
        j+=1

        questions[j],answers[j] = gen_solving_equations(1, 1, 0, 2, 1, 0)   # n, negs, negxs, steps, bothsides, brackets
        j+=1

        text[j] = 'What is the equation of the line?\n'
        questions[j], answers[j] = linear_graphs.straight_line_graphs(0,1)
        j+=1
        a = random.randint(1,2)
        if a == 1:
            text[j] = 'What is the y-intercept of the line?\n'
        else:
            text[j] = 'What is the gradient of the line?\n'
        questions[j], answers[j] = linear_graphs.straight_line_graphs(a,0)
        j+=1


    if ht == 2 or ht == 3:
        pass
        #questions[j], answers[j] = random.choice([factors_multiples_primes.list_factors(), factors_multiples_primes.list_multiples(), factors_multiples_primes.product_of_primes()])
        #j += 1
        #questions[j], answers[j] = expanding_and_factorising.expanding_binomials(0)
        #j+=1
        #questions[j], answers[j] = random.choice([cuboid.cuboid(), cuboid.triangular_prism()])
        #j+=1

    if ht == 3 or ht == 4:
        pass

    if ht == 4 or ht == 5:
        pass

    if ht == 5 or ht == 6:
        pass

    if ht == 6:
        pass

    return {'count': count,
            'questions': questions,
            'answers': answers,
            'text':text}
