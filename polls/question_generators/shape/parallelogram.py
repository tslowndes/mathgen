import random
from scipy import array as ar
from polls.question_generators.shape.shape_tools import *
import math
from polls.question_generators.tools import *

def gen_parallelogram(para_trap=0,a2=0,a3=0,a4=0,a5=0,a6=0):
    clear_temp_img()
    questions = []
    answers = []
    count = [i for i in range(8)]
    scalene = [0,0,0,1,1,1]
    random.shuffle(scalene)
    scalene = [0,0] + scalene
    for i in count:
        if i < 4:
            q,a = area_of_parallelogram(0, 0, 0, para_trap)
        elif i < 6:
            q, a = area_of_parallelogram(0, 1, 0, para_trap)
        else:
            q, a = area_of_parallelogram(0, 1, 0, para_trap)

        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}


def area_of_parallelogram(scalene, lbls, rot, para_trap=0):

    height = random.randint(5,12)
    base = random.randint(3,12)
    
    if para_trap == 0:
        height = random.randint(5,12)
        base = random.randint(3,12)
        offset = random.randint(1,int(round(base*0.75,0)))
        points = [[0,0], [base,0], [base+offset,height], [offset, height], [0,0]]
    else:
        height = random.randint(5,12)
        base = random.randint(6,12)
        offset = random.randint(1,int(round(base*0.4,0)))
        offset2 = random.randint(0,1)
        if base - (offset*2) - offset2 <= 0:
            offset2 = 0
        points = [[0,0], [base,0], [base-offset-offset2,height], [offset, height], [0,0]]

    if rot == 1:
        ang = random.randint(30, 300)
        points = rotate(ar(points), ang)

    units = random.choice(['mm', 'cm', 'm'])
    if para_trap == 0:
        lengths = [base, round(math.sqrt(offset**2 + height**2),1), base, round(math.sqrt(offset**2 + height**2),1)]
    else:
        lengths = [base, round(math.sqrt((offset+offset2)**2 + height**2),2), base-(offset*2)-offset2, round(math.sqrt(offset**2 + height**2),1)]
        
    label_points = labels_for_shape(ar(points))

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
    labels = []
    if para_trap == 0:
        if lbls == 0:
            labels = [str(lengths[0]) + units, '', '', '']
        else:
            labels = random.choice([[str(lengths[0]) + units, str(lengths[1]) + units, '', ''], [str(lengths[0]) + units, '', '', str(lengths[1]) + units]])
    else:
        if lbls == 0:
            labels = [str(lengths[0]) + units, '', str(lengths[2])+units, '']
        else:
            labels = random.choice([[str(lengths[0]) + units, str(lengths[1]) + units, str(lengths[2])+units, ''], [str(lengths[0]) + units, '', str(lengths[2])+units, str(lengths[1]) + units]])
        
    if random.randint(0,1)==1:
        height_arrow = [points[3], [offset,0]]
        height_txt = str(height) + units
        height_lbl = [offset+math.sqrt(height/10), height/2]
        height_ang=-90
    else:
        height_arrow = [points[2], [base-offset-offset2,0]]
        height_txt = str(height) + units
        height_lbl = [base-offset-offset2-math.sqrt(height/10), height/2]
        height_ang = 90
        
    if rot == 1:
        height_ang = -90+ang
        height_arrow = rotate(ar(height_arrow), ang).tolist()

    fig = plot_shape(ar(points), label_points, labels, 3, 0, angs, height_arrow, height_lbl, height_ang, height_txt)
    plt.text(-2,height + 0.25*height,"A=?")
    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, pad_inches=0.1, dpi=200, transparent=True, bbox_inches='tight')
    if para_trap == 0:
        ans = base * height
    else:
        ans = 0.5 * (base + lengths[2]) * height
        
    return fn, '$$' + str(ans) + units + '^2' + '$$'
