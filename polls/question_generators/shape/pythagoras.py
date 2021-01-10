import os, sys
sys.path.append(os.path.join('../../', "lib"))
from polls.question_generators.tools import *
from polls.question_generators.shape.shape_tools import *
from scipy import array as ar

def gen_pythagoras(n, hyp_or_small,a2=0,a3=0,a4=0,a5=0):
    clear_temp_img()
    fns = []
    ans = []
    units = random.choice(['mm','cm','m'])
    for i in range(0,n):

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


        if i > 1:

            ang = random.randint(30, 360)
            tri = rotate(tri, ang)
            right_angle_marker = rotate_shape(right_angle_marker, c, ang*pi/180)

        lbl_points = labels_for_shape(tri)
        if hyp_or_small == 0:
            fig = plot_shape(tri, lbl_points, [str(lens[0]) + units, str(lens[1]) + units, 'x'])
        else:
            fig = plot_shape(tri, lbl_points, [str(lens[0]) + units, 'x', str(lens[2]) + units])

        plt.plot(right_angle_marker[:,0], right_angle_marker[:,1], color = '#1f77b4', linewidth = 4)




        r = random.randint(0,999999999999999)
        fn = 'temp_img/temp'+ str(r) + '.png'

        fig.savefig('media/' + fn, bbox_inches='tight', pad_inches = 0, transparent=True)

        fns.append(fn)
        if hyp_or_small == 0:
            ans.append(str(lens[-1]) + units)
        else:
            ans.append(str(lens[1]) + units)

    count = [i for i in range(0,4)]
    if n == 1:
        return fns[0], ans[0]
    else:
        return {'count':count, 'questions':fns, 'answers':ans}