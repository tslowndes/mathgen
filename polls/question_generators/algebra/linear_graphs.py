import random
from polls.question_generators.tools import *
from polls.question_generators.shape.shape_tools import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patheffects
import numpy as np

def gen_picking_m_c(form_read_both,b,c,d,e,f):
    questions = []
    answers = []
    count = [i for i in range(8)]
    j = [0,0,0,0,0,1,1,1,1,1]
    random.shuffle(j)
    for i in count:
        if form_read_both == 0:
            q,a = form_equation()
        elif form_read_both == 1:
            q,a = m_and_c_from_equation()
        else:
            if j[i] == 0:
                q,a = form_equation()
            else:
                q,a = m_and_c_from_equation()

        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}

def form_equation():
	c = rand_no0_no1(-5,5)
	m = rand_no0_no1(-5,5)

	equation = tidy_algebra('y = ' + str(m) + 'x + ' + str(c))
	if random.randint(0,1)==0:
	    question = 'A line has a gradient of ' + str(m) + ' and a y-intercept of ' + str(c) + '. Write the equation of the line.'
	else:
	    question = 'A line has a y-intercept of ' + str(c) + ' and a gradient of ' + str(m) +  '. Write the equation of the line.'
	answer = equation

	return question, answer

def m_and_c_from_equation():
	c = random.randint(-5,5)
	m = random.randint(-5,5)

	equation = tidy_algebra('y = ' + str(m) + 'x + ' + str(c))
	if random.randint(0,1) == 0:
		question = 'A line has the equation $' + equation + '$What is the gradient of the line?'
		answer = str(m)
	else:
		question = 'A line has the equation $' + equation + '$What is the y-intercept of the line?'
		answer = str(c)

	return question, answer

def line_on_points():
	b = random.randint(-9, 9)
	a = [random.randint(-9, 9), random.randint(-9, 9), random.randint(-9, 9)]
	points = []
	if random.randint(0,1) == 1:
		points = [(b,a[0]), (b, a[1]), (b, a[2])]
		answer = 'x = ' + str(b)
	else:
		points = [(a[0],b), (a[1], b), (a[2], b)]
		answer = 'y = ' + str(b)

	question = 'The points: ' + str(points[0]) + ', ' + str(points[1]) + ' and ' + str(points[2]) + ' all lie on which line?'

	return question, answer

def point_on_the_line():
	x1 = random.randint(-10,10)
	y1 = random.randint(-10,10)
	if random.randint(0,1)==1:
		answer = 'x = ' + str(x1)
	else:
		answer = 'y = ' + str(y1)

	if x1 != y1:
		if random.randint(0,1) == 1:
			option2 = 'x = ' + str(y1)
		else:
			option2 = 'y = ' + str(x1)
	else:
		option2 = 'x = ' + str(-1*y1)

	option3 = 'y = x'

	options = [answer, option2, option3]
	random.shuffle(options)

	if x1 == y1:
		answer = answer + ' and ' + option3



	question = r'The point (' + str(x1) + ' , ' + str(y1) + ') lies on which line? \n\n'

	question = question + options[0] + ' ,  ' + options[1] + '  or  ' + options[2]

	return question, answer

def gen_linear_plots(grad_yint_both,parallel,posm_negm,d,e,f):
    clear_temp_img()
    questions = []
    answers = []
    count = [i for i in range(8)]
    if posm_negm == 9:
        ms = [-4,1,-2,3,-1,3,4,-3]
        #random.shuffle(ms)
    for i in count:
        q,a = straight_line_graphs(grad_yint_both,parallel,0,ms[i])
        while a in answers:
            q,a = straight_line_graphs(grad_yint_both,parallel)

        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}

def straight_line_graphs(grad_yint_both,parallel,starter=0,posm_negm=2):
    if parallel == 0:
        if grad_yint_both != 1:
            if posm_negm == 7:
                m = rand_no0(1,5)
            elif posm_negm==8:
                m = rand_no0(-5,-1)
            else:
                m = posm_negm


            if starter == 1:
                m = rand_no0(1,3)

        else:
            m = 1

        if grad_yint_both != 0:
            if grad_yint_both == -1:
                c = random.randint(-4,4)
            else:
                if starter == 1:
                    c = random.randint(-3,3)
                else:
                    c = random.randint(-4,4)
        else:
            c=0

        x = range(-5,6)
        y = [m*i+c for i in x]
    else:
        f = rand_no0(-3,3)
        if random.randint(0,1) == 0:
            x = [i for i in range(-5,6)]
            y = [f for i in range(-5,6)]
        else:
            y = [i for i in range(-5,6)]
            x = [f for i in range(-5,6)]

    if grad_yint_both == -1:
        new_x = []
        new_y = []
        for i in range(len(x)):
            if x[i] >= -5 and x[i] <= 5 and y[i] >= -5 and y[i] <= 5:
                new_x.append(x[i])
                new_y.append(y[i])
        x = new_x
        y = new_y
        x = [i + abs(x[0]) for i in x]
        y = [i + abs(y[0]) for i in y]

        max_y_add = 10 - max(y)
        max_x_add = 10 - max(x)
        add_y = random.randint(0,max_y_add)
        add_x = random.randint(0,max_x_add)

        x = [i + add_x for i in x]
        y = [i + add_y for i in y]




    fig = plt.figure(figsize =(1,1))

    ax = fig.add_subplot(111)
    plt.plot(x,y,c='r',linewidth=0.5)
    plt.plot([-10,10],[-10,10],c='k',linewidth=0.001)

    plt.margins(x=0, y=0)


    if grad_yint_both != -1:
        ax.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
        ax.set_yticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])

        if starter==1:
            plt.xlim(-3.2,3.2)
            plt.ylim(-3.2,3.2)
        else:
            plt.xlim(-5.2,5.2)
            plt.ylim(-5.2,5.2)


    else:
        plt.xlim(0,10)
        plt.ylim(0,10)
        ax.set_yticks([i for i in range(0,11)])
        ax.set_xticks([i for i in range(0,11)])

    ax.tick_params(axis='x', which='major', pad=0.1, length=1)#, linewidth = 0.5)
    ax.tick_params(axis='y', which='major', pad=0.1, length=1)#, linewidth = 0.5)


    ax.set_aspect('equal')
    #ax.spines['right'].set_visible(False)
    #ax.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(0.3)
    if grad_yint_both != -1:
        ax.spines['left'].set_position('center')
    #else:
    #    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    if grad_yint_both != -1:
        ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_tick_params(width=0.3)
    ax.yaxis.set_tick_params(width=0.3)
    ax.grid(c = 'k', linestyle='-', linewidth=0.05)
    fig.tight_layout()

    if starter==1:
        fs = 3
    else:
        fs = 2

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(fs)
        if tick.label.get_text() == "0":
            tick.label.set_fontsize(0)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(fs)
        if tick.label.get_text() == "0":
            tick.label.set_fontsize(0)


    r = random.randint(0,999999999999999)
    fn = 'temp_img/temp'+ str(r) + '.png'

    fig.savefig('media/' + fn, dpi = 500, pad_inches = 0.02, transparent=True, bbox_inches='tight')
    if parallel == 0:
        if grad_yint_both == -1:
            ans=str(m)
        elif grad_yint_both == 0:
            ans = "$ y=" + str(m) + "x $"
        elif grad_yint_both == 1:
            ans = "$ y=x+" + str(c) + " $"
        else:
            ans = "$ y=" + str(m) + "x+" + str(c) + " $"
    else:
        if x[0] == x[1]:
            ans = "$ x=" + str(f) + " $"
        else:
            ans = "$ y=" + str(f) + " $"
    if grad_yint_both != -1:
        if grad_yint_both == 1:
            ans = c
        else:
            ans = tidy_algebra(ans)

            if "+" in ans:
                if ans[ans.find("+") + 1] == "-":
                    ans = ans[:ans.find("+")] + ans[ans.find("+")+1:]

            if ans[-3] == "0" and ans[-4] == "+":
                ans=ans[:-4] + " $"

    return fn, ans

def gen_finding_gradient(pos_neg_frac, pn_axis, a3, a4, a5, a6):
    clear_temp_img()
    questions = []
    answers = []
    count = [i for i in range(8)]

    for i in count:
        q,a = finding_grad_of_line(pos_neg_frac, pn_axis, i)

        questions.append(q)
        answers.append(a)

    return {'questions': questions, 'answers': answers, 'count': count}

def finding_grad_of_line(pos_neg_frac, pn_axis, n):
    ms = [1,1,2,2,3,3,4,4]
    random.shuffle(ms)
    if pos_neg_frac == 0:
        m = ms[n]
        start_point = (random.randint(1,5),random.randint(1,2))

    elif pos_neg_frac == 1:
        m = -1*ms[n]
        start_point = (random.randint(1,4),random.randint(7,10))
    else:
        d = rand.randint(2,5)
        n = rand.randint(1,d)
        start_point = (random.randint(0,5),random.randint(0,5))

    if m > 0:
        end_point = (start_point[0]+1, start_point[1]+m)
        while end_point[0] < 10 and end_point[1] < 10-m:
            end_point = (end_point[0]+1, end_point[1]+m)
    else:
        end_point = (start_point[0]+1, start_point[1]+m)
        while end_point[0] < 10 and end_point[1] > abs(m):
            end_point = (end_point[0]+1, end_point[1]+m)


    fig = plt.figure(figsize =(1.2,1.2))

    ax = fig.add_subplot(111)
    plt.plot((start_point[0], end_point[0]), (start_point[1], end_point[1]),c='r',linewidth=.5)
    plt.plot([-10,10],[-10,10],c='k',linewidth=0.001)

    plt.margins(x=0, y=0)

    plt.xlim(0,11)
    plt.ylim(0,11)
    ax.set_yticks([i for i in range(0,12)])
    ax.set_xticks([i for i in range(0,12)])

    ax.tick_params(axis='x', which='major', pad=0.1, length=1)#, linewidth = 0.5)
    ax.tick_params(axis='y', which='major', pad=0.1, length=1)#, linewidth = 0.5)


    ax.set_aspect('equal')
    #ax.spines['right'].set_visible(False)
    #ax.spines['top'].set_visible(False)
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(0.3)
    #if grad_yint_both != -1:
    #    ax.spines['left'].set_position('center')
    #else:
    #    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')

    ax.spines['top'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_tick_params(width=0.3)
    ax.yaxis.set_tick_params(width=0.3)
    ax.grid(c = 'k', linestyle='-', linewidth=0.1)
    fig.tight_layout()

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(3)
        if tick.label.get_text() == "0" or tick.label.get_text() == "-1":
            tick.label.set_fontsize(0)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(3)
        if tick.label.get_text() == "0":
            tick.label.set_fontsize(0)


    r = random.randint(0,999999999999999)
    fn = 'temp_img/temp'+ str(r) + '.png'

    fig.savefig('media/' + fn, dpi = 750, pad_inches = 0.02, transparent=True, bbox_inches='tight')

    return fn, m



