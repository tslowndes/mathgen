import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *
from polls.question_generators.shape.shape_tools import *
from scipy import array as ar
import math

def gen_pythagoras(n, hyp_or_small,a2=0,a3=0,a4=0,a5=0):
    clear_temp_img()
    fns = []
    ans = []
    mixture = []
    for i in range(n):
        if (i % 2) == 0:
            mixture.append(0)
        else:
            mixture.append(1)

    random.shuffle(mixture)
    temp_save = 0
    n = int(n)
    for i in range(0,n):
        angs = []
        units = random.choice(['mm', 'cm', 'm'])

        if hyp_or_small == 2:
            temp_save = 2
            hyp_or_small = mixture[i]

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

        ang = 0
        if i < 2:
            ang = 0
        elif i < 4:
            ang = random.choice([90,180,270,360])
        else:
            ang = random.randint(30, 360)
        tri = rotate(tri, ang)
        right_angle_marker = rotate_shape(right_angle_marker, c, ang*pi/180)

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


        if hyp_or_small == 0:
            fig = plot_shape(tri, lbl_points, ['  '+str(lens[0]) + units, '  '+str(lens[1]) + units, 'x'], 3, 0, angs)
        else:
            fig = plot_shape(tri, lbl_points, ['  '+str(lens[0]) + units, 'x', '  '+str(lens[2]) + units], 3, 0, angs)

        r = random.randint(0,999999999999999)
        fn = 'temp_img/temp'+ str(r) + '.png'

        fig.savefig('media/' + fn, dpi = 200, pad_inches = 0, transparent=True)

        fns.append(fn)
        if hyp_or_small == 0:
            ans.append(str(lens[-1]) + units)
        else:
            ans.append(str(lens[1]) + units)

        if temp_save == 2:
            hyp_or_small = 2

    count = [i for i in range(0,n)]
    if n == 1:
        return fns[0], ans[0]
    else:
        return {'count':count, 'questions':fns, 'answers':ans}