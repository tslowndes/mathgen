import random
from math import cos, radians,sin
import matplotlib.pyplot as plt
import numpy as np

from polls.question_generators.tools import *

def basic_angle_facts():
    qs = ['around a point', 'on a straight line', 'in a triangle', 'in a quadrilateral']
    anss = ['Add up to $360^o$', 'Add up to $180^o$', 'Add up to $180^o$', 'Add up to $180^o$']
    n = random.randint(0, len(qs)-1)
    q = 'Angles ' + qs[n] + '...'
    ans = anss[n]
    return q,ans

def angles_around_a_point(n_angles):
    a = (1,0)
    b = (0.5,0)
    rat = []
    for i in range(n_angles):
        if i == 0:
            rat.append(random.randint(20,360-(20*(n_angles-(i+1)))))
        elif i != n_angles-1:
            rat.append(random.randint(20,360-np.sum(rat)-(20*(n_angles-(i+1)))))
        else:
            rat.append(360-np.sum(rat))
    angles = rat

    angle_labels = []
    for i in range(len(angles)):
        if i == 0:
            angle_labels.append((angles[i]-5)/2)
        else:
            if np.sum(angles[:i]) + angles[i]/2 < 90:
                angle_labels.append(np.sum(angles[:i]) + ((angles[i]-5)/2))
            elif np.sum(angles[:i]) + angles[i]/2 < 180:
                angle_labels.append(np.sum(angles[:i]) + ((angles[i]+5)/2))
            elif np.sum(angles[:i]) + angles[i]/2 < 270:
                angle_labels.append(np.sum(angles[:i]) + ((angles[i]-5)/2))
            else:
                angle_labels.append(np.sum(angles[:i]) + ((angles[i]+5)/2))

    r = 0.5

    # problem here with angles > 140
    r_labels = []
    for angle in angles:
        if angle > 140:
            r_labels.append(r/3)
        else:
            r_labels.append((r/2) - (r/3 * ((angle-20)/140)))
    #r_labels = [0.3 for angle in angles]

    point_labels = []
    for i in range(len(angles)):
        if angle_labels[i] <= 90:
            point_labels.append((0.5 + (r_labels[i]*cos(radians(angle_labels[i]))), r_labels[i]*sin(radians(angle_labels[i]))))
        elif angle_labels[i] <= 180:
            point_labels.append((0.5 - (r_labels[i]*cos(radians(180 - angle_labels[i]))), r_labels[i]*sin(radians(180 - angle_labels[i]))))
        elif angle_labels[i] <= 270:
            point_labels.append((0.5 -(r_labels[i]*cos(radians(angle_labels[i] - 180))),-1 * r_labels[i]*sin(radians(angle_labels[i] - 180))))
        else:
            point_labels.append((0.5 + (r_labels[i]*cos(radians(360 - angle_labels[i]))),-1 * r_labels[i]*sin(radians(360 - angle_labels[i]))))

    ds = []
    for i in range(0,len(angles)-1):
        angle = np.sum(angles[:i+1])
        if angle <=90:
            ds.append((0.5 + (r*cos(radians(angle))), r*sin(radians(angle))))
        elif angle <=180:
            ds.append((0.5 - (r*cos(radians(180 - angle))), r*sin(radians(180 - angle))))
        elif angle <=270:
            ds.append((0.5 - (r*cos(radians(angle-180))), -1*r*sin(radians(angle-180))))
        else:
            ds.append((0.5 + (r*cos(radians(360 - angle))), -1*r*sin(radians(360 - angle))))

    # plotting

    fig = plt.figure(figsize =(1.5,1.5))

    ax = fig.add_subplot(111)

    plt.plot([a[0], b[0]], [a[1],b[1]], color = '#1f77b4', linewidth = 1)
    for d in ds:
        plt.plot([b[0], d[0]], [b[1],d[1]], color = '#1f77b4', linewidth = 1 , solid_capstyle='round')
    a = random.randint(0,len(angles)-1)
    ans = angles[a]
    angles[a] = "x"

    for i in range(len(angles)):
        plt.text(point_labels[i][0], point_labels[i][1], str(angles[i]), fontsize='xx-small', horizontalalignment='center', verticalalignment='center')

    ax.set_aspect('equal')
    plt.axis('off')
    plt.xlim(0,1)
    plt.ylim(-.5,.5)

    circle_r = 0.6*r
    circle_x = np.arange(0,1,.0001)
    circle_y = np.sqrt(circle_r**2-np.square(circle_x-0.5))
    circle_x = np.append(circle_x, circle_x)
    circle_y = np.append(circle_y, -1*circle_y)



    plt.plot(circle_x, circle_y, color = '#1f77b4', linewidth = 1 , solid_capstyle='round')

    #fig.tight_layout()
    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, pad_inches=0.1, dpi=300, transparent=True, bbox_inches='tight')

    #return fig
    return fn, ans

def angles_on_a_straight_line(n_angles):
    a = (0,0)
    b = (0.5,0)
    c = (1,0)
    rat = []
    for i in range(n_angles):
        if i == 0:
            rat.append(random.randint(20,180-(20*(n_angles-(i+1)))))
        elif i != n_angles-1:
            rat.append(random.randint(20,180-np.sum(rat)-(20*(n_angles-(i+1)))))
        else:
            rat.append(180-np.sum(rat))
    angles = rat
    angle_labels = []
    for i in range(len(angles)):
        if i == 0:
            angle_labels.append((angles[i]-5)/2)
        else:
            if np.sum(angles[:i]) + angles[i]/2 > 90:
                angle_labels.append(np.sum(angles[:i]) + ((angles[i]+5)/2))
            else:
                angle_labels.append(np.sum(angles[:i]) + ((angles[i]-5)/2))

    r = 0.5


    r_labels = [(r/2) - (r/3 * ((angle-20)/140)) for angle in angles]
    #r_labels = [0.3 for angle in angles]

    point_labels = []
    for i in range(len(angles)):
        if angle_labels[i] <= 90:
            point_labels.append((0.5 + (r_labels[i]*cos(radians(angle_labels[i]))), r_labels[i]*sin(radians(angle_labels[i]))))
        else:
            point_labels.append((0.5 - (r_labels[i]*cos(radians(180 - angle_labels[i]))), r_labels[i]*sin(radians(180 - angle_labels[i]))))
    ds = []
    for i in range(0,len(angles)-1):
        angle = np.sum(angles[:i+1])
        if angle <=90:
            ds.append((0.5 + (r*cos(radians(angle))), r*sin(radians(angle))))
        else:
            ds.append((0.5 - (r*cos(radians(180 - angle))), r*sin(radians(180 - angle))))

    #Up to here!!!

    # plotting

    fig = plt.figure(figsize =(1.5,1.5))

    ax = fig.add_subplot(111)

    plt.plot([a[0], c[0]], [a[1],c[1]], color = '#1f77b4', linewidth = 1)
    for d in ds:
        plt.plot([b[0], d[0]], [b[1],d[1]], color = '#1f77b4', linewidth = 1 , solid_capstyle='round')
    a = random.randint(0,len(angles)-1)
    ans = angles[a]
    angles[a] = "x"

    for i in range(len(angles)):
        plt.text(point_labels[i][0], point_labels[i][1], str(angles[i]), fontsize='xx-small', horizontalalignment='center', verticalalignment='center')

    ax.set_aspect('equal')
    plt.axis('off')
    plt.xlim(0,1)
    plt.ylim(-.01,.5)

    circle_r = 0.6*r
    circle_x = np.arange(0,1,.0001)
    circle_y = np.sqrt(circle_r**2-np.square(circle_x-0.5))


    plt.plot(circle_x, circle_y, color = '#1f77b4', linewidth = 1 , solid_capstyle='round')

    #fig.tight_layout()
    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, pad_inches=0.1, dpi=300, transparent=True, bbox_inches='tight')

    #return fig
    return fn, ans

def gen_angles_straight_line(strline_or_point,a2,a3,a4,a5,a6):
    clear_temp_img()
    questions = []
    answers = []
    count = [i for i in range(8)]

    for i in count:
        if strline_or_point == 0:
            if i < 4:
                q,a = angles_on_a_straight_line(2)
            else:
                q,a = angles_on_a_straight_line(random.randint(3,4))
        else:
            if i < 4:
                q,a = angles_around_a_point(2)
            else:
                q,a = angles_around_a_point(random.randint(3,5))
        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}
