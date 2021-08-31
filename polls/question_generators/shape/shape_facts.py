import random

def polygon_names():
    n =[3,4,5,6,7,8,9,10,11,12]
    s =["Triangle","Quadrilateral","Pentagon","Hexagon","Heptagon","Octogon","Nonagon","Decagon","Hendecagon","Dodecagon"]
    sides =random.choice(n)
    name = s[n.index(sides)]
    if random.randint(0,1)==0:
        q = "A ___________ has " + str(sides) + " sides."
        ans = name 
    else:
        q = "A " + name + " has _____ sides."
        ans = sides
    return q,ans

def classify_angles():
    ang = random.randint(1,359)
    if ang < 90:
        ans = "Acute"
    elif ang == 90:
        ans = "Right"
    elif ang < 180:
        ans = "Obtuse"
    else:
        ans = "Reflex"
    q = "An angle of " + str(ang) + u"\N{DEGREE SIGN}" + " is a ________ angle"
    return q,ans