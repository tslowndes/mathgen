import random
from math import atan2, pi, sqrt
from scipy import dot, sin, cos
from scipy import array as ar
import matplotlib.path as mpltPath

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


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

def gen_ratriangle():
    x = [0]
    y = [0]
    a = random.randint(5,20)
    b = random.randint(5,20)

    x.append(x[0]+a)
    y.append(0)

    x.append(x[1])
    y.append(y[1] + b)
    x.append(x[0])
    y.append(y[0])
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

    #delta = (max(points[:,0]) - min(points[:,0]))/5
    delta = 2

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

def plot_shape(shape, lbl_points, lbls):
    fig = plt.figure(figsize = (4,4))
    ax = fig.add_subplot(111)
    plt.plot(shape[:, 0], shape[:, 1], color = '#1f77b4', linewidth = 4)
    for i in range(len(lbls)):
        plt.text(lbl_points[i][0], lbl_points[i][1], lbls[i], horizontalalignment='center', verticalalignment='center', fontsize = 'xx-large')

    delta = (max(shape[:, 0]) - min(shape[:, 0])) / 100

    x_min = min(shape[:,0])-2
    x_max = max(shape[:,0])+2
    y_min = min(shape[:,1])-2
    y_max = max(shape[:,1])+2

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')

    return fig

def test():
    #x,y = gen_ratriangle()
    #shape = ar([[x[i], y[i]] for i in range(len(x))])
    shape = gen_ratriangle()
    shape = rotate(shape, random.randint(1, 360))
    lbl_points = labels_for_shape(shape)

    plot_shape(shape, lbl_points, ['a','b','c'])
