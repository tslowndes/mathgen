import random
from scipy import array as ar
from polls.question_generators.shape.shape_tools import *
import math
from polls.question_generators.tools import *

def gen_triangles(a1,a2,a3,a4,a5,a6):
    clear_temp_img()
    questions = []
    answers = []
    count = [i for i in range(8)]
    scalene = [0,0,0,1,1,1]
    random.shuffle(scalene)
    scalene = [0,0] + scalene
    for i in count:
        q,a = area_of_triangle(scalene[i])
        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}


def area_of_triangle(scalene):

    height = random.randint(5,12)
    points = [[0,0], [random.randint(5,12),0]]
    base = points[1][0]
    if scalene ==1:
        points = points + [[random.randint(points[1][0],points[1][0]+5), height]]
    else:
        points = points + [[random.randint(0, points[1][0]), height]]
    points = points + [[0,0]]

    units = random.choice(['mm', 'cm', 'm'])
    lengths = [points[1][0], round(math.sqrt(((points[1][0]-points[2][0])**2)+((points[1][1]-points[2][1])**2)),0), round(math.sqrt((points[2][0]**2)+(points[2][1]**2)), 0)]

    #label_points = labels_for_shape(ar(points))
    label_points = ar([[points[1][0]/2, -2], [0,0], [0,0]])
    #points = [points[2], points[1], points[0], points[2], [points[2][0], 0]]

    labels = [str(lengths[0]) + units, '', '']
    height_arrow = [points[2], [points[2][0],0]]
    height_txt = str(height) + units
    if height_arrow[1][0] < points[1][0] and height_arrow[1][0] > 0:
        if height_arrow[1][0] < points[1][0]/2:
            #right
            height_lbl = [height_arrow[1][0] + 1, height_arrow[0][1]/2]
            height_ang = -90
        else:
            #Left
            height_lbl = [height_arrow[1][0] - 1, height_arrow[0][1]/2]
            height_ang = 90
    else:
        if height_arrow[1][0] > points[1][0]:
            height_lbl = [height_arrow[1][0] + 1, height_arrow[0][1]/2]
            height_ang = -90
        else:
            height_lbl = [height_arrow[1][0] - 1, height_arrow[0][1]/2]
            height_ang = 90

    fig = plot_shape(ar(points), label_points, labels, 3, 0, 0, height_arrow, height_lbl, height_ang, height_txt)

    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, pad_inches=0, dpi=200, transparent=True)

    return fn, '$$' + str((base*height)/2) + units + '^2' + '$$'
