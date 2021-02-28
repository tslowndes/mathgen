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
    shape = random_polygon()
    lens = []

    sides = len(shape.tolist())

    lbl_points = labels_for_shape(shape)
    lbls = ['' for i in lbl_points]
    fig = plot_shape(shape, lbl_points, lbls, 3, 1)

    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'
    x_min = shape[:,0].min()
    x_max = shape[:,0].max()
    y_min = shape[:,1].min()
    y_max = shape[:,1].max()
    plt.xlim([x_min-0.2, x_max+0.2])
    plt.ylim([y_min-0.2, y_max+0.2])
    fig.savefig('media/' + fn, bbox_inches='tight', pad_inches=0, transparent=True)
    question = fn
    answer = '$' + str((sides - 2)*180) + '^o$'

    return question, answer
