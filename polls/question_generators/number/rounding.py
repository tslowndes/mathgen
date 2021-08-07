import random

def rounding(dec_or_sf, n):
    num = random.random() * random.choice([1,10,100,1000])
    q = round(num,n+random.randint(1,4))
    ans = round(num,n)
    return q, ans

def gen_rounding(n,b,c,d,e,f):
	pass
	