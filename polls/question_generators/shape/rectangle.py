import random
from scipy import array as ar
from polls.question_generators.shape.shape_tools import *

def gen_rectanlge_area(a1,a2,a3,a4,a5,a6):
    questions = []
    answers = []
    count = [i for i in range(6)]

    for i in count:
        q,a = rectangle_area_perimeter(0)
        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}

def gen_rectangle_perimeter(a1,a2,a3,a4,a5,a6):
    questions = []
    answers = []
    count = [i for i in range(6)]

    for i in count:
        q,a = rectangle_area_perimeter(1)
        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}

def rectangle_area_perimeter(area_or_perimeter):
    w = random.randint(3,10)
    l = random.randint(w,w+10)
    units = random.choice(['mm', 'cm', 'm'])

    points = ar([[0,0],[l,0],[l,w],[0,w], [0,0]])

    label_points = labels_for_shape(points)

    labels = [str(l) + units, str(w) + units, '', '']

    fig = plot_shape(points, label_points, labels)
    if area_or_perimeter == 0:
        plt.text(l / 2, w / 2, 'Area = ?', horizontalalignment='center', verticalalignment='center', fontsize='large')
    else:
        plt.text(l / 2, w / 2, 'Perimeter = ?', horizontalalignment='center', verticalalignment='center', fontsize='large')

    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, bbox_inches='tight', pad_inches=0, transparent=True)
    question = fn

    if area_or_perimeter == 0:
        ans = '$' + str( l * w ) + units + '^2$'
    else:
        ans = '$' + str(l + l + w + w) + units + '$'

    return question, ans
