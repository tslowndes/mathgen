from django.http import HttpResponse
from django.template import loader
import random
import string
import pandas as pd
from polls.shapes import *
from math import sqrt, gcd
from os import listdir
from os.path import isfile, join
import os
import math
from time import sleep

def contents(request):
    template = loader.get_template('polls/contents.html')
    context = {}
    return HttpResponse(template.render(context, request))


def index(request):
    #Importing Dataframe
    df = pd.read_csv('polls/dir.csv')
    template = loader.get_template('polls/index2.html')
    template_image = loader.get_template('polls/index_image.html')
    err_template = loader.get_template('polls/plain.html')
    #Getting Arguments from URL
    year = int(request.GET.get('year'))
    task = request.GET.get('task')

    #Isolating task from dataframe
    df_task = df[df['Task_Code']==task]
    df_year = df_task[df_task['Yr']==year]
    task_code = df_year.Task_Code.to_list()[0]
    #Getting method name
    method_name = df_year.Function_Name.to_list()[0]

    if type(method_name) == str:
        #Getting arguments for method
        args = [df_year['arg1'].to_list()[0],df_year['arg2'].to_list()[0],df_year['arg3'].to_list()[0],df_year['arg4'].to_list()[0],df_year['arg5'].to_list()[0],df_year['arg6'].to_list()[0]]
        img = df_year['images'].to_list()[0]
        title = df_year['Task_Title'].to_list()[0]
        #Setting up method
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(method_name)
        #Call method and get questions
        context = method(args[0], args[1], args[2], args[3], args[4], args[5])
        #      rows = []
        #      count = []
        #     i = 0

        #        while i < len(context['count']):
        #            if i == len(context['count']) - 1:
        #               rows.append([string.ascii_lowercase[i] + ")", context['questions'][i], "", ""])
                #               rows.append(["", context['answers'][i], "", ""])

            #else:
                #rows.append([string.ascii_lowercase[i] + ")", context['questions'][i], string.ascii_lowercase[i+1] + ")",  context['questions'][i+1]])
                #   rows.append(["", context['answers'][i], "", context['answers'][i+1]])
            #            i += 2
#
        #context = {'rows':rows, 'count':count}
        alphas = []
        for i in range(len(context['questions'])):
            alphas.append(string.ascii_lowercase[i])
        task_code = task_code[0]
        context['alphas'] = alphas
        context['title'] = title
        context['task_code'] = task_code
        if task_code == 'A':
            strand = 'Algebra'
        elif task_code == 'N':
            strand = 'Number'
        elif task_code == 'S':
            strand = 'Shape'
        elif task_code == 'D':
            strand = 'Data'
        else:
            strand = 'Starters'
        context['strand'] = strand

        if img == 0:
            return HttpResponse(template.render(context, request))
        else:

            return HttpResponse(template_image.render(context, request))

    else:
        return HttpResponse(err_template.render({'content':'Task Not Found.'}, request))




def subcontents(request):
    task = request.GET.get('task')
    template = loader.get_template('polls/subcontents.html')
    df = pd.read_csv('polls/dir.csv')
    df = df.loc[df["Task_Code"].str.startswith(task)].copy()

    task_code_list = list(set(df['Task_Code'].to_list()))
    task_code_list.sort()

    fin_years = []
    fin_topics = []
    fin_task_codes = []
    fin_index = []
    j = 0

    for task_code in task_code_list:
        years = df[df.Task_Code == task_code]['Yr'].to_list()
        topics = df[df.Task_Code == task_code]['Task_Title'].to_list()

        count = 0
        i = 0

        while count < 5:
            fin_index.append(j)
            if i<len(years):
                if years[i] == count + 7:
                    fin_years.append(years[i])
                    fin_topics.append(topics[i])
                    fin_task_codes.append(task_code)
                    i += 1
                    count += 1
                else:
                    fin_years.append(count + 7)
                    fin_topics.append("")
                    fin_task_codes.append("")
                    count += 1
            else:
                fin_years.append(count + 7)
                fin_topics.append("")
                fin_task_codes.append("")
                count += 1
            j += 1

    context = {'count': fin_index, 'topics':fin_topics, 'year':fin_years, 'task_code':fin_task_codes}

    return HttpResponse(template.render(context, request))


def rand_no0_no1(min, max):
    result = 0
    while result == 0 or result == 1:
        result = random.randint(min, max)
    return result

def rand_no0(min, max):
    result = 0
    while result == 0:
        result = random.randint(min, max)
    return result

def gen_linear_sequences(add_or_subtract, neg_first_term, a3, a4, a5, a6):
    if neg_first_term == 1:
        first_term = random.randint(-1,-20)
    else:
        first_term = random.randint(0, 20)

    common_difference = random.randint(2, 15)
    if add_or_subtract == 1:
        common_difference = common_difference * -1
    terms = ''
    for i in range(0,5):
        if i != 0:
            terms = terms + ', ' + str(first_term + i * common_difference)
        else:
            terms = terms + str(first_term + i * common_difference)
    answer = first_term + 5 * common_difference

    return terms, answer


def gen_adding_algebra_terms(a1, a2, a3, a4, a5, a6):
    a = random.randint(1, 10)
    b = rand_no0(-10,10)
    alpha = get_alpha()

    c = a + b
    question = '$' + tidy_algebra(str(a) + alpha + ' + ' + str(b) + alpha) + '$'
    answer = '$' + tidy_algebra(str(c) + alpha) + '$'

    return question, answer

def gen_pythagoras(small_or_hyp,a1,a2,a3,a4,a5):
    clear_temp_img()
    fns = []
    ans = []
    for i in range(0,4):
        tri = gen_ratriangle()
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
        for i in range(len(tri)-1):
            lens.append(round(sqrt(((tri[i][0] - tri[i+1][0])**2)+((tri[i][1] - tri[i+1][1])**2)), 2))


        if i > 1:

            ang = random.randint(30, 360)
            tri = rotate(tri, ang)
            right_angle_marker = rotate_shape(right_angle_marker, c, ang*pi/180)

        lbl_points = labels_for_shape(tri)

        fig = plot_shape(tri, lbl_points, [lens[0], lens[1], 'x'])
        plt.plot(right_angle_marker[:,0], right_angle_marker[:,1], color = '#1f77b4', linewidth = 4)




        r = random.randint(0,999999999999999)
        fn = 'temp_img/temp'+ str(r) + '.png'

        fig.savefig('media/' + fn, bbox_inches='tight', pad_inches = 0, transparent=True)

        fns.append(fn)
        ans.append(lens[-1])
    count = [i for i in range(0,4)]

    return {'count':count, 'questions':fns, 'answers':ans}


def clear_temp_img():
    mypath = 'media/temp_img/'
    for f in listdir(mypath):
        os.remove(mypath + f)

def get_alpha():
    return random.choice('abcdefghjklmnpqrstuvwxyz')

def gen_solving_equations(n, negs, negxs, steps, bothsides, brackets):
    count = []
    qs = []
    ans = []
    max = 9
    min = 1
    minx = 1

    if negs == 1:
        min = -10
    else:
        min = 1

    if negxs ==1:
        minx = -10
    else:
        minx = 1

    for i in range(0, n):
        count.append(i)
        a=0
        b=0
        x=0

        if steps == 1:
            if random.randint(0,1) == 0:
                a = 1
                b = rand_no0_no1(min, 9)
            else:
                a = rand_no0_no1(minx, 9)
                b = 0
        else:
            a = rand_no0_no1(minx, 9)
            b = rand_no0_no1(min, 9)

        x = rand_no0_no1(minx, 9)

        if a == 1 or brackets == 1 or bothsides == 1:
            multidiv = 0
        else:
            multidiv = random.randint(0,1)

        if multidiv == 0:
            c = (a*x) + b
        else:
            c = rand_no0_no1(min, 9)
            x = (c-b)*a

        if brackets == 1:
            d = rand_no0_no1(0,5)
            c = c * d

        if bothsides == 1:
            e = rand_no0(-10, 10)
            f = a + e

            while f == 0:
                e = rand_no0(-10, 10)
                f = a + e

            a = f

        x_side = ''
        ans_side = str(c)

        alpha = random.choice('abcdefghjklmnpqrstuvwxyz')

        if bothsides == 1:
            if random.randint(0,1) == 0:
                ans_side = ans_side + " + " + str(e) + alpha
            else:
                ans_side = str(e) + alpha + " + " + ans_side
            ans_side = tidy_algebra(ans_side)

        if b == 0:
            if multidiv == 0:
                x_side = str(a) + alpha
            else:
                x_side = r"\frac{" + alpha + "}{" + str(a) + "}"

        else:
            if random.randint(0,1) > 0 or i < 4:
                if multidiv == 0:
                    x_side = str(a) + alpha + " + " + str(b)
                else:
                    x_side = r'\frac{' + alpha + "}{" + str(a) + "}" + " + " + str(b)
            else:
                if multidiv == 0:
                    x_side = str(b) + " + " + str(a) + alpha
                else:
                    x_side = str(b) + " + " + r'\frac{' + alpha + "}{" + str(a) + "}"

        x_side = tidy_algebra(x_side)

        if brackets == 1:
            x_side = str(d) + "(" + x_side + ")"

        if random.randint(0,1)>0 or i < 4:
            q = x_side + " = " + ans_side
        else:
            q = ans_side + " = " + x_side

        qs.append('$' + q + '$')

        ans.append('$' + alpha + " = " + str(x) + '$')

    return {
        'count': count,
        'questions': qs,
        'answers': ans
    }

def gen_collecting_like_terms(powers, doubleletters, a3, a4, a5, a6):
    count = []
    qs = []
    anss = []
    for i in range(0, 10):
        y1 = rand_no0(-10, 10)
        y2 = rand_no0(-10, 10)
        x1 = rand_no0(-10, 10)
        x2 = rand_no0(-10, 10)

        if powers == 0 and doubleletters == 0:
            alpha1 = 'a'
            alpha2 = 'a'
            while alpha1 == alpha2:
                alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
                alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
        if powers == 1 and doubleletters == 1:
            if random.randint(0,1) ==0:
                alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
                alpha2 = alpha1 + "^" + str(random.randint(2, 3))
                if random.randint(0,1) == 0:
                    alpha1 = alpha1 + "^" + str(random.randint(4, 5))
            else:
                alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
                alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
                while alpha1 == alpha2:
                    alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
                alpha2 = alpha1 + alpha2

        elif powers ==1 and doubleletters ==0:
            alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
            alpha2 = alpha1 + "^" + str(random.randint(2,3))
            if random.randint(0, 1) == 0:
                alpha1 = alpha1 + "^" + str(random.randint(4, 5))

        elif doubleletters == 1 and powers ==0 :
            alpha1 = random.choice('abcdefghjklmnpqrstuvwxyz')
            alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
            while alpha1 == alpha2:
                alpha2 = random.choice('abcdefghjklmnpqrstuvwxyz')
            alpha2 = alpha1 + alpha2



        terms = [str(y1) + alpha1, str(y2) + alpha1, str(x1) + alpha2, str(x2) + alpha2]
        random.shuffle(terms)
        terms = terms[0] + ' + ' + terms[1] + ' + ' + terms[2] + ' + ' + terms[3]

        if y1 + y2 == 0:
            ans = str(x1 + x2) + alpha2
        elif x1 + x2 == 0:
            ans = str(y1 + y2) + alpha2
        elif x1 + x2 == 0 and y1 + y2 == 0:
            ans = 0
        else:
            ans = str(y1 + y2) + alpha1 + " + " + str(x1 + x2) + alpha2

        terms = tidy_algebra(terms)
        ans1 = tidy_algebra(ans)
        count.append(i)
        qs.append('$' + terms + '$')
        anss.append('$' + ans1 + '$')

    return {
        'count': count,
        'questions': qs,
        'answers': anss
    }

def gen_expanding_brackets(powers,a2,a3,a4,a5,a6):
    qs = []
    ans = []
    count = []
    ### Generates expanding brackets questions in the form c(ax + b)
    for i in range(0,10):
        a = random.randint(1,10)
        b = rand_no0(-10,10)
        c = random.randint(2,10)

        if powers == 1 or powers == 2:
            if powers == 1:
                a_ind = random.randint(1,2)
                c_ind = 1
            else:
                a_ind = random.randint(1,3)
                c_ind = random.randint(1,3)

            expanded = tidy_algebra(str(c*a) + 'x^' + str(a_ind+c_ind) + ' + ' + str(c*b) + 'x^' + str(c_ind))
            factorised = tidy_algebra(str(c) + 'x^' + str(c_ind) +'(' + str(a) + 'x^' + str(a_ind) + ' + ' + str(b) + ')')
        else:

            expanded = tidy_algebra(str(c*a) + 'x' + ' + ' + str(c*b))
            factorised = tidy_algebra(str(c) + '(' + str(a) + 'x' + ' + ' + str(b) + ')')

        qs.append('$' + factorised + '$')
        ans.append('$' + expanded + '$')
        count.append(i)

    context = {
        'count':count,
        'questions':qs,
        'answers':ans,
    }

    return context




def tidy_algebra(q):
    i = 1
    while i < len(q):
        if q[i].isalpha():
            if i > 1:
                if q[i-1] == "1" and q[i-2].isnumeric()==False:
                    q = q[:i-1] + q[i:]
                elif q[i-1] == "1" and q[i-2] == "-":
                    q = q[:i-1] + q[i:]
                else:
                    i += 1
            else:
                if q[i-1] == "1":
                    #q = q[:i-1] + q[i:]
                    q = q[i:]
                i += 1
        else:
            i += 1

    i = 1

    while i < len(q):
        if q[i] == "+":
            if q[i+2] == "-":
                q = q[:i] + q[i+2] + " " + q[i+3:]
        i += 1

    i = 1

    while i < len(q):
        if q[i] == "^":
            if q[i+1] == '1':
                q = q[:i] + q[i+2:]
            else:
                i += 1
        else:
            i += 1

    return q

def frac_to_percentage(a1=0, a2=0, a3=0, a4=0, a5=0,a6=0):
    denominator = random.choice([2,4,5,10, 20, 25, 50])
    numerator = random.randint(1,denominator-1)

    percentage = numerator / denominator * 100
    percentage = str(percentage)
    if percentage[-2:] == '.0':
        percentage = percentage[:-2]
    percentage = str(percentage) + '%'

    fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + '}$'

    return fraction, percentage

def simplify_frac(num, den):
    simp = gcd(num, den)
    return num/simp, den/simp


def frac_to_decimal(a1=0, a2=0, a3=0, a4=0, a5=0,a6=0):
    a = round(random.random(), 2)

    a = str(a)
    if a[-1] == 0:
        a = a[:-1]

    numerator = a[a.find('.')+1:]

    if len(numerator) == 1:
        denominator = 10
    else:
        denominator = 100

    numerator = int(numerator)

    numerator1, denominator1 = simplify_frac(numerator, denominator)

    numerator1 = str(numerator1).strip('0')
    denominator1 = str(denominator1).strip('0')

    if numerator1[-1] == '.':
        numerator1 = numerator1[:-1]

    if denominator1[-1] == '.':
        denominator1 = denominator1[:-1]

    if str(numerator) == numerator1:
        fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + '}$'
    else:
        fraction = r'$\frac{' + str(numerator) + '}{' + str(denominator) + r'} = \frac{' + numerator1 + '}{' + denominator1 + '}$'

    decimal = a

    return decimal, fraction


def gen_white_rose_maths_starter(year, ht, a2, a3, a4, a5):
    count = [i for i in range(8)]
    questions = [0 for i in range(8)]
    answers = [0 for i in range(8)]
    questions[0], answers[0] = gen_linear_sequences(0, 0, 0, 0, 0, 0)
    questions [0] = 'Find the next term: ' + questions[0]
    questions[1], answers[1] = gen_linear_sequences(1, 0, 0, 0, 0, 0)
    questions [1] = 'Find the next term: ' + questions[1]
    questions[2], answers[2] = gen_adding_algebra_terms(0, 0, 0, 0, 0, 0)
    questions [2] = 'Simplify: ' + questions[2]
    out = gen_solving_equations(1, 0, 0, 1, 0, 0)
    questions[3] = 'Solve the equation: ' + out['questions'][0]
    answers[3] = out['answers'][0]
    questions[4], answers[4] = frac_to_percentage()
    questions[4] = r'Convert the fraction to a percentage: ' + questions[4]
    questions[5], answers[5] = frac_to_decimal()
    questions[5] = r'Convert the decimal to a fraction: ' + str(questions[5])
    answers[5] = answers[5]
    return {'count': count,
            'questions': questions,
            'answers': answers}