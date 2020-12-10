from django.http import HttpResponse
from django.template import loader
import random
import string
import pandas as pd
import math

def index(request):
    #Importing Dataframe
    df = pd.read_csv('polls/dir.csv')
    template = loader.get_template('polls/index.html')
    err_template = loader.get_template('polls/plain.html')
    #Getting Arguments from URL
    year = int(request.GET.get('year'))
    task = request.GET.get('task')

    #Isolating task from dataframe
    df_task = df[df['Task_Code']==task]
    df_year = df_task[df_task['Yr']==year]

    #Getting method name
    method_name = df_year.Function_Name.to_list()[0]

    if type(method_name) == str:
        #Getting arguments for method
        args = [df_year['arg1'].to_list()[0],df_year['arg2'].to_list()[0],df_year['arg3'].to_list()[0],df_year['arg4'].to_list()[0],df_year['arg5'].to_list()[0],df_year['arg6'].to_list()[0]]
        #Setting up method
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(method_name)
        #Call method and get questions
        context = method(args[0], args[1], args[2], args[3], args[4], args[5])
        rows = []
        count = []
        i = 0
        while i < len(context['count']):
            if i == len(context['count']) - 1:
                rows.append([string.ascii_lowercase[i] + ")", context['questions'][i], "", ""])
                rows.append(["", context['answers'][i], "", ""])

            else:
                rows.append([string.ascii_lowercase[i] + ")", context['questions'][i], string.ascii_lowercase[i+1] + ")",  context['questions'][i+1]])
                rows.append(["", context['answers'][i], "", context['answers'][i+1]])
            i += 2

        context = {'rows':rows, 'count':count}
        return HttpResponse(template.render(context, request))

    else:
        return HttpResponse(err_template.render({'content':'Task Not Found.'}, request))




def subcontents(request):
    template = loader.get_template('polls/subcontents.html')
    df = pd.read_csv('polls/dir.csv')

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
            if (i % 2) == 0:
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

        qs.append(q)

        ans.append(alpha + " = " + str(x))

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
        qs.append(terms)
        anss.append(ans1)

    return {
        'count': count,
        'questions': qs,
        'answers': anss
    }

def gen_expanding_brackets(a1,a2,a3,a4,a5,a6):
    qs = []
    ans = []
    count = []
    for i in range(0,10):
        a = random.randint(1,10)
        b = rand_no0(-10,10)
        c = random.randint(2,10)

        expanded = str(c*a) + 'x' + ' + ' + str(c*b)
        factorised = str(c) + '(' + str(a) + 'x' + ' + ' + str(b) + ')'

        qs.append(factorised)
        ans.append(expanded)
        count.append(count)

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
                if q[i-1] == "1" and q[i-2] == " ":
                    q = q[:i-1] + q[i:]
                elif q[i-1] == "1" and q[i-2] == "-":
                    q = q[:i-1] + q[i:]
            else:
                if q[i-1] == "1":
                    q = q[:i-1] + q[i:]

        elif q[i] == "+":
            if q[i+2] == "-":
                q = q[:i] + " " + q[i+2] + " " + q[i+3:]

        i += 1
    return q

