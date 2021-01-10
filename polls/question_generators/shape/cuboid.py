import random
from polls.question_generators.shape.shape_tools import *
from scipy import array as ar
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def gen_cuboid_volume(a1,a2,a3,a4,a5,a6):
    questions = []
    answers = []
    count = [i for i in range(6)]

    for i in count:
        q,a = cuboid()
        questions.append(q)
        answers.append(a)
    return {'questions': questions, 'answers': answers, 'count': count}

def gen_triprism_volume(a1,a2,a3,a4,a5,a6):
    questions = []
    answers = []
    count = [i for i in range(4)]

    for i in count:
        q,a = triangular_prism()
        questions.append(q)
        answers.append(a)
    return {'questions': questions, 'answers': answers, 'count': count}

def cuboid():
    width = random.randint(4,12)
    height = random.randint(3,6)
    depth = random.randint(2,8)
    units = random.choice(['mm','cm','m'])
    points = [((0,0),(width,0)),
              ((width,0),(width,height)),
              ((width,height),(0, height)),
              ((0,height),(0,0))]

    point1 = (width+depth, 0+depth/2)
    point2 = (width+depth, height + depth/2)
    point3 = (depth, height + depth/2)
    points = points + [((width, 0), point1), ((width, height), point2), ((0, height), point3), (point1, point2), (point2, point3)]
    points = ar(points)
    edges_for_labels = ar([points[3][0], points[0][0], points[4][0], points[4][1]])
    label_points = labels_for_shape(edges_for_labels)
    labels = [str(height)+units, str(width)+units, str(depth)+units]
    fig = plot_shape_byedge(points, label_points, labels)
    plt.text(width/2,height/2,'Volume = ?', horizontalalignment='center', verticalalignment='center', fontsize = 'large')
    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, bbox_inches='tight', pad_inches=0, transparent=True)
    question = fn
    answer = '$' + str(width * height* depth) + units + '^3$'

    return question, answer

def triangular_prism():
    width = random.randint(4,12)
    height = random.randint(3,6)
    depth = random.randint(2,8)

    points = [((0,0),(width,0)),
              ((width,0),(0,height)),
              ((0,height),(0,0))]

    point1 = (width+depth, 0+depth/2)

    point2 = (depth, height + depth/2)
    points = points + [((width, 0), point1), ((0, height), point2), (point1, point2)]
    points = ar(points)
    edges_for_labels = ar([points[2][0], points[2][1], points[0][1], point1])
    label_points = labels_for_shape(edges_for_labels)
    labels = [str(height), str(width), str(depth)]
    fig = plot_shape_byedge(points, label_points, labels)
    plt.text(width/3,height/3,'Volume = ?', horizontalalignment='center', verticalalignment='center', fontsize = 'large')
    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, bbox_inches='tight', pad_inches=0, transparent=True)
    question = fn
    answer = str(width * height* depth)

    return question, answer

