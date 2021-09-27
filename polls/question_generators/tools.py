import random
import os
from os import listdir
from math import gcd
import os
import time

def name_chooser():
    names = ['Adam', 'Muhammad', 'Alex', 'Jeremy', 'Ibrahim', 'William', 'Pedro', 'Giovanni', 'Fran', 'Jess', 'Selma', 'Mia', 'Clare', 'Asha', 'Lily']
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