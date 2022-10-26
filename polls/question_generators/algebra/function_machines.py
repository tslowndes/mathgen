import random
from polls.question_generators.tools import *
from polls.question_generators.shape.shape_tools import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patheffects
import numpy as np

def gen_function_machine(a1,a2,a3,a4,a5,a6):
    questions = []
    answers = []
    count = [i for i in range(10)]

    for i in range(10):
        q,a = single_function_machine()
        questions.append(q)
        answers.append(a)

    return {'questions':questions, 'answers':answers, 'count':count}

def single_function_machine(steps=1):
    clear_temp_img()
    fig = plt.figure(figsize =(1,1))
    n = random.randint(0,3)
    ops = ['+','-',r'\times','\div']
    op = ops[n]
    a = random.randint(2,9)
    alpha = get_alpha()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')

    plt.plot([0,1,1,3,3,4,3,3,1,1,0],[0,0,1,1,0,0,0,-1,-1,0,0],c='b')
    plt.plot([0.5,1,0.5],[0.5,0,-0.5],c='b')
    plt.plot([3.5,4,3.5],[0.5,0,-0.5],c='b')
    plt.text(-0.35,0,r"$" + alpha + "$", ha='right',va='center')
    plt.text(2,0,r"$" + op + str(a) +"$", ha='center',va='center')
    plt.axis('off')
    r = random.randint(0,999999999999999)
    fn = 'temp_img/temp'+ str(r) + '.png'

    fig.savefig('media/' + fn, dpi = 500, pad_inches = 0.02, transparent=True, bbox_inches='tight')

    return fn,0