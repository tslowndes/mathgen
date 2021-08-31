import random
from polls.question_generators import tools
def rounding(dec_or_sf, n):
    num = random.random() * random.choice([1,10,100,1000])
    q = round(num,n+random.randint(1,4))
    ans = round(num,n)
    return q, ans
    
def round_to_nearest():
    a = round(random.random() * random.choice([100,1000,10000,100000]),0)
    n = ["ten","hundred","thousand"]
    r = [-1,-2,-3]
    if a > 1000:
        near = random.choice(["ten","hundred","thousand", "thousand"])
    elif a > 100:
        near = random.choice(["ten","hundred", "hundred"])
    else:
        near = "ten"
    q = "Round " + tools.strip_0(a) + " to the nearest " + near + "."
    ans = tools.strip_0(round(a, r[n.index(near)]))
    return q,ans

def gen_rounding(n,b,c,d,e,f):
	pass
	