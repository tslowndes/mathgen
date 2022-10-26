from math import acos,asin,degrees,radians,sin,cos,tan
import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *
from polls.question_generators.shape.shape_tools import *
from scipy import array as ar
import math


def right_angled(sin_cos_tan, multi_div,find_angle=0):
    hyp_or_small = 0
    clear_temp_img()

    units = random.choice(['mm', 'cm', 'm'])

    tri = gen_ratriangle(hyp_or_small)

    a = tri[1][0] - tri[0][0]
    b = tri[2][1] - tri[1][1]

    r = min(a,b)/5
    v = tri[1]
    c = (sum(tri[:, 0]) / len(tri[:, 0]), sum(tri[:, 1]) / len(tri[:, 1]))

    right_angle_marker = ar([[v[0], v[1]],
                             [v[0],v[1]+r],
                             [v[0]-r,v[1]+r],
                             [v[0]-r, v[1]],
                             [v[0], v[1]]])

    lens = []
    for j in range(len(tri)-1):
        length = str(round(sqrt(((tri[j][0] - tri[j+1][0])**2)+((tri[j][1] - tri[j+1][1])**2)), 2))
        length = length.strip('0')
        if length[-1] == '.':
            length = length[:-1]

        lens.append(length)

    angle_1 = round(degrees(acos(float(lens[0])/float(lens[2]))),0)
    angle_2 = round(degrees(asin(float(lens[0])/float(lens[2]))),0)


    #tri = rotate(tri, ang)
    #right_angle_marker = rotate_shape(right_angle_marker, c, ang*pi/180)
    angs = []
    for j in range(len(tri)-1):
        if tri[j+1][0] == tri[j][0]:
            angs.append(90)
        elif tri[j+1][1] == tri[j][1]:
            angs.append(0)
        else:
            m = (tri[j+1][1] - tri[j][1])/(tri[j+1][0] - tri[j][0])
            angs.append(math.degrees(math.atan(m)))


    lbl_points = labels_for_shape(tri)
    tri = ar(list(tri) + list(right_angle_marker))
    lens = [float(i) for i in lens]

    if sin_cos_tan == 0:
        if multi_div ==0:
            if random.randint(0,1) == 1:
                lbls = [ " ", "x", str(lens[2])+ units]
                plot_angle_1 = 1
                plot_angle_2 = 0
                ans = round(lens[2] * sin(radians(angle_1)),2)
            else:
                lbls = [ "x", " ", str(lens[2])+ units]
                plot_angle_1 = 0
                plot_angle_2 = 1
                ans = round(lens[2] * sin(radians(angle_2)),2)
        else:
            if random.randint(0,1) == 1:
                lbls = [" ", str(lens[1]) + units, "x"]
                plot_angle_1 = 1
                plot_angle_2 = 0
                ans = round(lens[1] / sin(radians(angle_1)),2)
            else:
                lbls = [str(lens[0]) + units, " ", "x"]
                plot_angle_1 = 0
                plot_angle_2 = 1
                ans = round(lens[0] / sin(radians(angle_2)),2)
    elif sin_cos_tan == 1:
        if multi_div ==0:
            if random.randint(0,1) == 1:
                lbls = ["x", " ", str(lens[2])+ units]
                plot_angle_1 = 1
                plot_angle_2 = 0
                ans = round(lens[2] * cos(radians(angle_1)),2)
            else:
                lbls = [" ", "x", str(lens[2])+ units]
                plot_angle_1 = 0
                plot_angle_2 = 1
                ans = round(lens[2] * cos(radians(angle_2)),2)
        else:
            if random.randint(0,1) == 1:
                lbls = [str(lens[0]) + units, " ", "x"]
                plot_angle_1 = 1
                plot_angle_2 = 0
                ans = round(lens[0] / cos(radians(angle_1)),2)
            else:
                lbls = [" ", str(lens[1]) + units, "x"]
                plot_angle_1 = 0
                plot_angle_2 = 1
                ans = round(lens[1] / cos(radians(angle_2)),2)
    else:
        if multi_div ==0:
            if random.randint(0,1) == 1:
                lbls =  [str(lens[0]) + units, "x", " "]
                plot_angle_1 = 1
                plot_angle_2 = 0
                ans = round(lens[0] * tan(radians(angle_1)),2)
            else:
                lbls = ["x", str(lens[1]) + units, " "]
                plot_angle_1 = 0
                plot_angle_2 = 1
                ans = round(lens[1] * tan(radians(angle_2)),2)
        else:
            if random.randint(0,1) == 1:
                lbls = ["x", str(lens[1]) + units, " "]
                plot_angle_1 = 1
                plot_angle_2 = 0
                ans = round(lens[1] / tan(radians(angle_1)),2)
            else:
                lbls = [str(lens[0]) + units, "x", " "]
                plot_angle_1 = 0
                plot_angle_2 = 1
                ans = round(lens[0] / tan(radians(angle_2)),2)

    if find_angle == 1:
        lbls[lbls.index("x")] = str(ans)+units
        if plot_angle_1 == 1:
            ans = angle_1
        else:
            ans = angle_2

    fig = plot_shape(tri, lbl_points, lbls, 3, 0, angs)
    r=float(lens[0])*0.4

    if plot_angle_1 == 1:
        a = str(angle_1)
        a = a.strip("0")
        if a[-1]==".":
            a = a[:-1]
        if find_angle == 0:
            plt.text(r*cos(radians((angle_1*0.9)/2)),r*sin(radians((angle_1*0.9)/2)), a, fontsize='small', horizontalalignment='center', verticalalignment='center')
        else:
            plt.text(r*cos(radians((angle_1*0.9)/2)),r*sin(radians((angle_1*0.9)/2)), "x", fontsize='small', horizontalalignment='center', verticalalignment='center')

        circle_r = float(lens[0])*0.6
        circle_x_min = lens[0]*(circle_r/lens[2])
        circle_x = np.arange(circle_x_min,circle_r,.0001)
        circle_y = np.sqrt(circle_r**2-np.square(circle_x))

        plt.plot(circle_x, circle_y, color = '#1f77b4', linewidth = 2 , solid_capstyle='round')

    if plot_angle_2 == 1:
        a = str(angle_2)
        a = a.strip("0")
        if a[-1]==".":
            a = a[:-1]
        r=float(lens[1])*0.4
        if find_angle == 0:
            plt.text(tri[2][0]-(r*sin(radians((angle_2*0.9)/2))),tri[2][1]-(r*cos(radians((angle_2*0.9)/2))), a, fontsize='small', horizontalalignment='center', verticalalignment='center')
        else:
            plt.text(tri[2][0]-(r*sin(radians((angle_2*0.9)/2))),tri[2][1]-(r*cos(radians((angle_2*0.9)/2))), "x", fontsize='small', horizontalalignment='center', verticalalignment='center')

        circle_r = float(lens[1])*0.5
        circle_x_min = tri[2][0]-(lens[0]*(circle_r/lens[2]))
        circle_x = np.arange(circle_x_min,tri[2][0],.0001)
        circle_y = tri[2][1]-np.sqrt(circle_r**2-np.square(circle_x-tri[2][0]))

        plt.plot(circle_x, circle_y, color = '#1f77b4', linewidth = 2 , solid_capstyle='round')



    r = random.randint(0,999999999999999)
    fn = 'temp_img/temp'+ str(r) + '.png'

    fig.savefig('media/' + fn, dpi = 200, pad_inches = 0, transparent=True)
    return fn, ans

def gen_trigonometry(trigf,multiordiv,find_angle,a4,a5,a6):
    clear_temp_img()
    questions = []
    answers = []
    count = [i for i in range(8)]

    if trigf == 0:
        f = random.randint(0,2)
        sct = [f for i in count]
    else:
        sct=[0,0,1,1,2,2,random.randint(0,2),random.randint(0,2)]
        random.shuffle(sct)

    if multiordiv == 2:
        md = [0,0,0,0,1,1,1,1]
        random.shuffle(md)
    else:
        md = [multiordiv for i in count]

    for i in count:
        if find_angle == 2:
            q,a = right_angled(sct[i],md[i], random.randint(0,1))
        else:
            q,a = right_angled(sct[i],md[i], find_angle)

        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}