from django.http import HttpResponse
from django.template import loader
import string
import pandas as pd

####### ALGEBRA #######
from polls.question_generators.algebra.solving_equations import *
from polls.question_generators.algebra.collecting_like_terms import *
from polls.question_generators.algebra.linear_sequences import *
from polls.question_generators.algebra.expanding_and_factorising import *
from polls.question_generators.algebra.inequalities import *
from polls.question_generators.algebra.substitution import *
from polls.question_generators.algebra.indices import *
####### NUMBER #######
from polls.question_generators.number.fdp_conversions import *
from polls.question_generators.number.place_value import *
from polls.question_generators.number.direct_proportion import *
from polls.question_generators.number.fdp_conversions import *
from polls.question_generators.number.factors_multiples_primes import *
from polls.question_generators.number.percentages import *
from polls.question_generators.number.negatives import *

####### SHAPE #######
from polls.question_generators.shape.pythagoras import *
from polls.question_generators.shape.cuboid import *
from polls.question_generators.shape.rectangle import *
from polls.question_generators.shape.interior_angles import *
####### STARTERS #######
from polls.question_generators.starters.wrm_year7 import *

def contents(request):

    template = loader.get_template('polls/contents.html')
    context = {}
    return HttpResponse(template.render(context, request))


def index(request):
    #Importing Dataframe
    df = pd.read_csv('polls/dir.csv')
    template = loader.get_template('polls/index2.html')
    template_image = loader.get_template('polls/index_image.html')
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
        examples = context['questions']
        context = method(args[0], args[1], args[2], args[3], args[4], args[5])
        context['examples']=examples
        alphas = []
        for i in range(len(context['questions'])):
            alphas.append(string.ascii_lowercase[i])
        imgs = []
        for q in context['questions']:

            if type(q) == str:
                print(q)
                if q[:8] == 'temp_img':
                    imgs.append(1)
                else:
                    print('string but not img')
                    imgs.append(0)
            else:
                imgs.append(0)
        print(imgs)

        task_code = task_code[0]
        context['alphas'] = alphas
        context['imgs'] = imgs
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

        context['row_height'] = 100/max(context['count'])

        return HttpResponse(template.render(context, request))

    else:
        return HttpResponse(err_template.render({'content':'Task Not Found.'}, request))


def find_strand(task_code):
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
    return strand

def subcontents(request):
    task = request.GET.get('task')
    template = loader.get_template('polls/subcontents.html')
    df = pd.read_csv('polls/dir.csv')
    df = df.loc[df["Task_Code"].str.startswith(task)].copy()
    strand = find_strand(task)
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

    context = {'strand': strand, 'count': fin_index, 'topics':fin_topics, 'year':fin_years, 'task_code':fin_task_codes}

    return HttpResponse(template.render(context, request))






