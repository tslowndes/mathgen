import matplotlib.pyplot as plt
import numpy as np
from scipy import array as ar
import random
from polls.question_generators.shape.shape_tools import *
import math

def circle_measure(circ_or_area, r_or_d, backwards):
    # plotting
    radius=random.randint(1,20)
    diam=2*radius
    circum=diam*math.pi
    area = math.pi * (radius**2)

    fig = plt.figure(figsize =(2,1))

    ax = fig.add_subplot(111)

    ax.set_aspect('equal')
    plt.axis('off')
    plt.xlim(-2,2)
    plt.ylim(-1.2,1.2)

    circle_r = 1
    circle_x = np.arange(-1.1,1.1,.0001)
    circle_y = np.sqrt(circle_r**2-np.square(circle_x))

    circle_x = np.append(circle_x, circle_x)
    circle_y = np.append(circle_y, -1*circle_y)

    n = random.randint(0,len(circle_x))
    if r_or_d == 0:
        rx = [0, circle_x[n]]
        ry = [0, circle_y[n]]
    else:
        rx = [circle_x[n], -1*circle_x[n]]
        ry = [circle_y[n], -1*circle_y[n]]

    r = [[rx[0],ry[0]],[rx[1],ry[1]]]
    label_points = labels_for_shape(ar(r))

    plt.plot(circle_x, circle_y, color = '#1f77b4', linewidth = 1.5, solid_capstyle='round')
    plt.plot(rx, ry, color = '#1f77b4', linewidth = 1.5,linestyle='--', solid_capstyle='round')
    if r_or_d == 0:
        plt.text(label_points[0][0],label_points[0][1],str(radius), horizontalalignment='center', verticalalignment='center', fontsize = 'small')
    else:
        plt.text(label_points[0][0],label_points[0][1],str(diam), horizontalalignment='center', verticalalignment='center', fontsize = 'small')
    
    if circ_or_area == 0:
         plt.text(-2,0.8,"C=?", fontsize = 'large')
         ans = round(circum,2)
    else:
         plt.text(-2,0.8,"A=?", fontsize = 'large')
         ans = round(area,2)


    #fig.tight_layout()
    r = random.randint(0, 999999999999999)
    fn = 'temp_img/temp' + str(r) + '.png'

    fig.savefig('media/' + fn, pad_inches=0.1, dpi=300, transparent=True, bbox_inches='tight')

    
    #return fig
    return fn, ans
