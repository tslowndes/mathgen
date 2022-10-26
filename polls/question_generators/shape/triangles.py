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
        if i < 4:
            q,a = area_of_triangle(scalene[i],0)
        else:
            q, a = area_of_triangle(scalene[i],1)
        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}


def area_of_triangle(scalene, lbls):

    height = random.randint(5,12)
    base = random.randint(5,12)
    if (base%2) != 0:
        base += 1
    points = [[0,0], [base,0]]

    if scalene ==1:
        scalene_overhang = random.randint(points[1][0],points[1][0]+5)
        points = points + [[scalene_overhang, height]]
    else:
        points = points + [[random.randint(0, points[1][0]), height]]
    points = points + [[0,0]]

    units = random.choice(['mm', 'cm', 'm'])
    lengths = [points[1][0], round(math.sqrt(((points[1][0]-points[2][0])**2)+((points[1][1]-points[2][1])**2)),1), round(math.sqrt((points[2][0]**2)+(points[2][1]**2)), 1)]

    label_points = labels_for_shape(ar(points))
    label_points = ar([[points[1][0]/2, -1*math.sqrt(height/4)], label_points[1], label_points[2]])

    angs = []

    for j in range(len(points) - 1):
        if points[j + 1][0] == points[j][0]:
            angs.append(90)
        elif points[j + 1][1] == points[j][1]:
            angs.append(0)
        else:
            m = (points[j + 1][1] - points[j][1]) / (points[j + 1][0] - points[j][0])
            angs.append(math.degrees(math.atan(m)))

    #points = [points[2], points[1], points[0], points[2], [points[2][0], 0]]
    if lbls == 0:
        labels = [str(lengths[0]) + units, '', '']
    else:
        #if scalene == 1:
        if points[0][0] == points[2][0]:
            labels = [str(lengths[0]) + units, str(lengths[1]) + units, '']
        elif points[1][0] == points[2][0] or scalene == 1:
            labels = [str(lengths[0]) + units,'', str(lengths[2]) + units]
        else:
            labels = random.choice([[str(lengths[0]) + units, str(lengths[1]) + units, ''],
                                    [str(lengths[0]) + units, '', str(lengths[2]) + units]])

    height_arrow = [points[2], [points[2][0],0]]
    height_txt = str(height) + units
    if height_arrow[1][0] < points[1][0] and height_arrow[1][0] > 0:
        if height_arrow[1][0] < points[1][0]/2:
            #right
            height_lbl = [height_arrow[1][0] + math.sqrt(height/10), height_arrow[0][1]/2]
            height_ang = -90
        else:
            #Left
            height_lbl = [height_arrow[1][0] - math.sqrt(height/10), height_arrow[0][1]/2]
            height_ang = 90
    else:
        if height_arrow[1][0] > points[1][0]:
            height_lbl = [height_arrow[1][0] + math.sqrt(height/10), height_arrow[0][1]/2]
            height_ang = -90
        else:
            height_lbl = [height_arrow[1][0] - math.sqrt(height/10), height_arrow[0][1]/2]
            height_ang = 90

    fig = plot_shape(ar(points), label_points, labels, 3, 0, angs, height_arrow, height_lbl, height_ang, height_txt)
    plt.tight_layout()
    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, pad_inches=0.1, dpi=200, transparent=True, bbox_inches='tight')
    #fig.savefig('media/' + fn, pad_inches=0, dpi=200, transparent=True)
    return fn, '$$' + str((base*height)/2) + units + '^2' + '$$'
