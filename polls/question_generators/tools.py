import random
import os
from os import listdir
from math import gcd
import os
import time
from math import floor

def name_chooser():
    names = ['Raj','Kai','Tom','Joe','Cody','Jaz','Carlos','Juan','Kate','Evie','Kim','Adam', 'Muhammad', 'Alex', 'Jeremy', 'Ibrahim', 'Will', 'Pedro', 'Gio', 'Fran', 'Jess', 'Selma', 'Mia', 'Clare', 'Asha', 'Lily']
    return random.choice(names)

def as_fraction(n,d):
    return r'\frac{' + str(n) + '}{' + str(d) + '}'

def thing_chooser():
    things = ['sweets', 'bananas', 'apples', 'pens','pencils','slices of cake']
    return random.choice(things)

def rand_no0_no1(min, max):
    result = 0
    while result == 0 or result == 1:
        result = random.randint(min, max)
    return result

def strip_0(s):
    if '.' in str(s):
        s = str(s).strip("0")
        if s[-1]==".":
            s = s[:-1]
    return str(s)


def rand_no0(min, max):
    result = 0
    while result == 0:
        result = random.randint(min, max)
    return result

def clear_temp_img():
    mypath = 'media/temp_img/'
    now = time.time()
    for f in listdir(mypath):
        path = mypath + f
        if os.stat(path).st_mtime < now - 60:
            if os.path.isfile(path):
                os.remove(path)

def get_alpha():
    return random.choice('abcdefghjklmnpqrstuvwxyz')

def simplify_frac(num, den):
    simp = gcd(num, den)
    return num/simp, den/simp

def readable_digits(n,comma=0,tex=0):

    new = ''
    n = str(n)[::-1]
    #n=str(n)
    #i = floor(len(n)/3)
    if comma == 1:
        s = ','
    elif tex == 1:
        s = r';\ '
    else:
        s = ' '
    insert = 0
    count = 0
    i = 0
    while i < len(n):
        if insert == 3:
            new = new + s
            insert = 0
            count += 1
        else:
            new = new + n[i]
            insert +=1
            i += 1




    #for j in range(i):
    #    if j == 0:
    #        n = n[:-3*(j+1)] + s + n[-3*(j+1):]
    #    else:
    #        n = n[:-3*(j+1)-j] + s + n[-3*(j+1)-j:]
    return new[::-1]

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