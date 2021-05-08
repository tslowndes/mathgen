import random
from scipy import array as ar
from polls.question_generators.shape.shape_tools import *
from polls.question_generators.tools import *
import math

def gen_rectangle_area(a1,a2,a3,a4,a5,a6):
    clear_temp_img()
    questions = []
    answers = []
    count = [i for i in range(8)]

    for i in count:
        if i == 4:
            q, a = rectangle_area_perimeter(0, random.randint(10,60))
        elif i >= 5:
            q,a = rectangle_area_perimeter(0, random.randint(280,340))
        else:
            q,a = rectangle_area_perimeter(0)
        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}

def gen_rectangle_perimeter(a1,a2,a3,a4,a5,a6):
    clear_temp_img()
    questions = []
    answers = []
    count = [i for i in range(8)]

    for i in count:
        if i < 4:
            q,a = rectangle_area_perimeter(1, 0)
        else:
            q,a = rectangle_area_perimeter(1,random.randint(10,170))
        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}

def rectangle_area_perimeter(area_or_perimeter, rotate_shape = 0):
    w = random.randint(3,10)
    l = random.randint(w+1,w+10)
    units = random.choice(['mm', 'cm', 'm'])

    points = ar([[0,0],[l,0],[l,w],[0,w], [0,0]])

    if rotate_shape != 0:
        points = rotate(points, rotate_shape)

    label_points = labels_for_shape(points)
    filler = ''
    for i in range(len(str(w))+len(units)):
        filler = filler + ' '

    labels = [str(l) + units, filler + str(w) + units, '', '']
    angs = []

    for j in range(len(points) - 1):
        if points[j + 1][0] == points[j][0]:
            angs.append(90)
        elif points[j + 1][1] == points[j][1]:
            angs.append(0)
        else:
            m = (points[j + 1][1] - points[j][1]) / (points[j + 1][0] - points[j][0])
            angs.append(math.degrees(math.atan(m)))

    fig = plot_shape(points, label_points, labels, 3, 0, angs)
    #if area_or_perimeter == 0:
    #    plt.text(l / 2, w / 2, 'Area = ?', horizontalalignment='center', verticalalignment='center', fontsize='large')
    #else:
    #    plt.text(l / 2, w / 2, 'Perimeter = ?', horizontalalignment='center', verticalalignment='center', fontsize='large')

    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, pad_inches=0, dpi=200, transparent=True)
    question = fn

    if area_or_perimeter == 0:
        ans = '$' + str( l * w ) + units + '^2$'
    else:
        ans = '$' + str(l + l + w + w) + units + '$'

    return question, ans
