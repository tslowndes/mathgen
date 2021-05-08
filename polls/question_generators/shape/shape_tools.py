import random
from math import atan2, pi, sqrt, acos
from scipy import dot, sin, cos
from scipy import array as ar
import matplotlib.path as mpltPath
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def random_polygon():
    points = (np.random.rand(50, 2) - .5)   # 30 random points in 2-D
    hull = ConvexHull(points)
    #plt.plot(points[:, 0], points[:, 1], 'o')
    x = points[hull.vertices,0].tolist()
    x = x + [x[0]]
    y = points[hull.vertices, 1].tolist()
    y = y + [y[0]]

    i = 1
    while i < len(x) - 1 and len(x) > 3:
        a = sqrt((x[i]-x[i+1])**2 + (y[i]-y[i+1])**2)
        b = sqrt((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2)
        c = sqrt((x[i-1]-x[i+1])**2 + (y[i-1]-y[i+1])**2)

        angle = acos((a**2 + b**2 - c**2)/(2*a*b)) * 180/pi

        if angle > 175:
            x = x[:i] + x[i+1:]
            y = y[:i] + y[i+1:]
        else:
            i = i + 1

    if x[-1] != x[0]:
        x = x + [x[0]]
        y = y + [y[0]]


    beam = max(x) - min(x)
    i = 0
    while i < len(x)-1 and len(x) > 3:
        dist = sqrt((x[i]-x[i+1])**2 + (y[i]-y[i+1])**2)
        if dist > beam/5:
            i = i + 1
        else:
            x = x[:i+1] + x[i+2:]
            y = y[:i+1] + y[i+2:]

    if x[-1] != x[0]:
        x = x + [x[0]]
        y = y + [y[0]]

    points = np.array([[x[i], y[i]] for i in range(len(x))])

    return points



def to_convex_contour(vertices_count,
                      x_generator=random.random,
                      y_generator=random.random):
    """
    Port of Valtr algorithm by Sander Verdonschot.

    Reference:
        http://cglab.ca/~sander/misc/ConvexGeneration/ValtrAlgorithm.java

    True
    """
    xs = [x_generator()*10 for _ in range(vertices_count)]
    ys = [y_generator()*10 for _ in range(vertices_count)]
    xs = sorted(xs)
    ys = sorted(ys)
    min_x, *xs, max_x = xs
    min_y, *ys, max_y = ys
    vectors_xs = _to_vectors_coordinates(xs, min_x, max_x)
    vectors_ys = _to_vectors_coordinates(ys, min_y, max_y)
    random.shuffle(vectors_ys)

    def to_vector_angle(vector):
        x, y = vector
        return atan2(y, x)

    vectors = sorted(zip(vectors_xs, vectors_ys),
                     key=to_vector_angle)
    point_x = point_y = 0
    min_polygon_x = min_polygon_y = 0
    points = []
    for vector_x, vector_y in vectors:
        points.append((point_x, point_y))
        point_x += vector_x
        point_y += vector_y
        min_polygon_x = min(min_polygon_x, point_x)
        min_polygon_y = min(min_polygon_y, point_y)
    shift_x, shift_y = min_x - min_polygon_x, min_y - min_polygon_y
    points = [(point_x + shift_x, point_y + shift_y)
            for point_x, point_y in points]
    points.append(points[0])
    return ar(points)


def _to_vectors_coordinates(coordinates, min_coordinate, max_coordinate):
    last_min = last_max = min_coordinate
    result = []
    for coordinate in coordinates:
        if _to_random_boolean():
            result.append(coordinate - last_min)
            last_min = coordinate
        else:
            result.append(last_max - coordinate)
            last_max = coordinate
    result.extend((max_coordinate - last_min,
                   last_max - max_coordinate))
    return result


def _to_random_boolean():
    return random.getrandbits(1)

def gen_ratriangle(hyp_or_small=0):
    x = [0]
    y = [0]
    if hyp_or_small == 0:
        a = random.randint(7,20)
        b = random.randint(a+1,a*2)
    else:
        a = random.randint(7, 10)
        c = random.randint(a+1,a+5)
        b = sqrt(c ** 2 - a ** 2)

    x = x + [x[0]+a, x[0]+a, x[0]]
    y = y + [y[0], y[0]+b, y[0]]

    points = [[x[i], y[i]] for i in range(len(x))]
    points = ar(points)
    return points

def rotate(pts, ang):
    cnt = (sum(pts[:,0])/len(pts[:,0]), sum(pts[:,1])/len(pts[:,1]))
    return rotate_shape(pts,cnt,ang*pi/180)

def rotate_shape(pts,cnt,ang=pi/4):
    '''pts = {} Rotates points(nx2) about center cnt(2) by angle ang(1) in radian'''
    return dot(pts-cnt,ar([[cos(ang),sin(ang)],[-sin(ang),cos(ang)]]))+cnt

def labels_for_shape(points):

    lbls = []
    x_len = max(points[:,0]) - min(points[:,0])
    y_len = max(points[:,1]) - min(points[:,1])

    if y_len > x_len:
        max_len = y_len
    else:
        max_len = x_len

    delta = max_len/5

    for i in range(len(points)-1):

        temp_lbls = find_label_point(points[i], points[i+1], delta)

        for lbl in temp_lbls:
            if is_in_shape([lbl],points) == False:
                lbls.append(lbl)
    return ar(lbls)

def find_label_point(v1,v2, delta):
    cntrs = []

    c = ((v1[0] + v2[0])/2, (v1[1] + v2[1])/2)

    if v2[0] - v1[0] == 0:
        lbl1 = (c[0]+delta, c[1])
        lbl2 = (c[0]-delta, c[1])
    elif v2[1] - v1[1] == 0:
        lbl1 = (c[0], c[1] + delta)
        lbl2 = (c[0], c[1] - delta)
    else:
        m = (v2[1] - v1[1])/(v2[0] - v1[0])
        mp = -1 / m
        d = sqrt((delta**2)/(1+(mp**2)))
        lbl1 = (c[0] + d), c[1] + (d * mp)
        lbl2 = (c[0] - d), c[1] - (d * mp)

    return lbl1, lbl2

def is_in_shape(points, polygon):
    path = mpltPath.Path(polygon)
    inside2 = path.contains_points(points)
    return inside2

def plot_shape_byedge(shape, lbl_points, lbls):
    fig = plt.figure(figsize = (4,4))
    ax = fig.add_subplot(111)
    for edge in shape:
        plt.plot(edge[:, 0], edge[:, 1], color = '#1f77b4', linewidth = 4)

    for i in range(len(lbls)):
        plt.text(lbl_points[i][0], lbl_points[i][1], lbls[i], horizontalalignment='center', verticalalignment='center', fontsize = 'xx-large')

    points = []
    for sh in shape:
        points.append(sh[0])
        points.append(sh[1])
    points = ar(points)

    delta = (max(points[:, 0]) - min(points[:, 0])) / 100


    x_min = min(points[:,0])-2
    x_max = max(points[:,0])+2
    y_min = min(points[:,1])-2
    y_max = max(points[:,1])+2

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')

    return fig


def plot_shape(shape, lbl_points, lbls, lw = 1, plt_points = 0, ang = 0, height_arrow=0, height_lbl=0,height_ang=0,height_txt=''):
    fig = plt.figure(figsize =(1.5,1.5))

    ax = fig.add_subplot(111)

    x_min = min(shape[:,0])
    x_max = max(shape[:,0])
    x_len = x_max - x_min
    y_min = min(shape[:,1])
    y_max = max(shape[:,1])
    y_len = y_max - y_min

    if x_len > y_len:
        normalise = x_max
    else:
        normalise = y_max

    #shape = shape / normalise * 5

    #lbl_points = lbl_points/normalise*5

    plt.plot(shape[:, 0], shape[:, 1], color = '#1f77b4', linewidth = 2)

    if plt_points == 1:
        plt.scatter(shape[:,0], shape[:,1], s=50, c='#1f77b4')
    for i in range(len(lbls)):
        if ang == 0:
            plt.text(lbl_points[i][0], lbl_points[i][1], lbls[i], horizontalalignment='center', rotation=0, verticalalignment='center', fontsize = 9)
        else:
            plt.text(lbl_points[i][0], lbl_points[i][1], lbls[i], horizontalalignment='center', rotation=ang[i],
                     verticalalignment='center', fontsize=9)
    if height_arrow != 0:
        plt.plot([height_arrow[0][0], height_arrow[1][0]],[height_arrow[0][1], height_arrow[1][1]], '--', color = '#1f77b4', linewidth = 1)
        plt.text(height_lbl[0],height_lbl[1], height_txt, horizontalalignment='center', verticalalignment='center', rotation=height_ang, fontsize = 9)

    all_points = ar(list(shape) + list(lbl_points))

    x_min = min(all_points[:,0])-0.5
    x_max = max(all_points[:, 0])+0.5
    y_min = min(all_points[:, 1])-0.5
    y_max = max(all_points[:, 1])+0.5
    if x_max > y_max:
        lim_max = x_max
    else:
        lim_max = y_max
    plt.xlim(x_min, lim_max)
    plt.ylim(y_min, lim_max)
    ax.set_aspect('equal')
    plt.axis('off')
    plt.tight_layout()

    return fig

def test():
    #x,y = gen_ratriangle()
    #shape = ar([[x[i], y[i]] for i in range(len(x))])
    shape = gen_ratriangle()
    shape = rotate(shape, random.randint(1, 360))
    lbl_points = labels_for_shape(shape)

    plot_shape(shape, lbl_points, ['a','b','c'])
