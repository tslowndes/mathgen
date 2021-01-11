import random
from polls.question_generators.shape.shape_tools import *
import numpy as np
def gen_sum_of_interior_angles(a1,a2,a3,a4,a5,a6):
    questions = []
    answers = []
    count = [i for i in range(4)]

    for i in count:
        q,a = sum_of_interior_angles()
        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}

def sum_of_interior_angles():
    n = random.randint(8,14)
    shape = to_convex_contour(n)
    lens = []
    shape = shape.tolist()
    for i in range(int(len(shape))-3):
        m1 = (shape[i+1][1] - shape[i][1])/(shape[i+1][0] - shape[i][0])
        m2 = (shape[i+2][1] - shape[i+1][1])/(shape[i+2][0] - shape[i+1][0])
        if m2 > 0.9*m1 and m2<1.1*m1:
            shape = shape[:i + 1] + shape[i + 2:]

    shape = shape + [shape[0]]
    shape = np.array(shape)

    sides = shape.size/2-1

    lbl_points = labels_for_shape(shape)
    lbls = ['' for i in lbl_points]
    fig = plot_shape(shape, lbl_points, lbls, 3, 1)

    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, bbox_inches='tight', pad_inches=0, transparent=True)
    question = fn
    answer = '$' + str((sides - 2)*180) + '^o$'

    return question, answer
