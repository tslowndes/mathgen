from random import randint, random
from polls.question_generators.tools import *
import math
def round_2_money(m):
    m = str(round(m,2))
    dec = m[m.find("."):]
    if len(dec) == 2:
        m = m+"0"

    return m

def basic_purchase(number_of_items):
    item1 = random.choice(['pens', 'pencils','rulers','sweets','KitKats','Mars Bars'])
    item2 = random.choice(['Twix', 'Kitkats','cans of coke', 'bottles of Lucozade'])

    unit_price1 = round(random.randint(0,2)+random.random(),2)
    unit_price2 = round(random.randint(0,2)+random.random(),2)

    quantity1, quantity2 = randint(2,4), randint(2,4)
    if number_of_items == 1:
        quantity2 = 0
    total = unit_price1*quantity1 + unit_price2*quantity2

    if total < 5:
        note = 5
    elif total < 10:
        note = 10
    else:
        note = 20

    name = name_chooser()

    if number_of_items == 2:
        q = name + ' buys ' + str(quantity1) + ' ' + item1 + ' at £' + round_2_money(unit_price1) + ' each and ' + str(quantity2) + ' ' + item2 + ' at £' + round_2_money(unit_price2) + ' each. ' + name + ' pays with a £' + str(note) + ' note. How much change does ' + str(name) + ' get?'
        ans = '£' + round_2_money(note - ((quantity1 * unit_price1) + quantity2*unit_price2))
    else:
        q = name + ' buys ' + str(quantity1) + ' ' + item1 + ' at £' + round_2_money(unit_price1) + ' each. ' + name + ' pays with a £' + str(
            note) + ' note. How much change does ' + str(name) + ' get?'
        ans = "£" + round_2_money(note - ((quantity1 * unit_price1)))
    return q,ans

def gen_basic_purchase(n,a,b,c,d,e):
	questions = []
	answers = []
	count = [i for i in range(10)]
	for i in count:
		if i < 5:
			q,a = basic_purchase(1)
		else:
		    q,a = basic_purchase(2)
		questions.append(q)
		answers.append(a)
	return {'questions':questions, 'answers':answers, 'count':count}

def basic_save(spend, item):
    m = random.randint(3,10)*10
    mfreq = random.choice(['week','month'])
    afreq = random.randint(1,3)
    name = name_chooser()


    if spend == 1:
        s = random.randint(10, m-5)
        q = name + " gets £" + str(m) + " a " + mfreq + ", spends £" + str(s) + " and saves the rest."
    else:
        s=0
        q = name + " saves £" + str(m) + " a " + mfreq + "."

    if item == 1:
        i = random.choice(['laptop','phone','bike','xbox'])
        cost = random.randint(2,5)*100
        q = q + " How many " + mfreq + " until " + name + " can buy a new " + i + " costing £" + str(cost) + "?"
        saved = math.ceil(cost/(m-s))
        return q, str(saved) + " " + mfreq + "s"
    else:
        q = q + " How much does " + name + " save in " + str(afreq) + " year(s)?"

        if mfreq == "week":
            saved = (m-s)*52*afreq
        else:
            saved = (m-s)*12*afreq

        return q, "£" + round_2_money(saved)

def gen_basic_save(n,a,b,c,d,e):
	questions = []
	answers = []
	count = [i for i in range(10)]
	for i in count:
		if i < 3:
			q,a = basic_save(0,0)
		elif i < 6:
			q,a = basic_save(1,0)
		else:
		    q,a = basic_save(1,1)
		questions.append(q)
		answers.append(a)
	return {'questions':questions, 'answers':answers, 'count':count}

def profit(unit_price, findprofit):
    item1 = random.choice(['pens', 'pencils','rulers','sweets','KitKats','Mars Bars'])
    item2 = random.choice(['Twix', 'Kitkats','cans of coke', 'bottles of Lucozade'])
    name = name_chooser()
    if unit_price == 0:
        total = random.randint(10,20)
        profit = random.randint(total, 2*total)
        total = total + round(random.random(),2)
        profit = profit + round(random.random(),2)
        if findprofit==1:
    	    q = name + " buys some " + item1 + " for £" + round_2_money(total) + " and sells them all for £" + round_2_money(total + profit) + ". How much profit does " + name + " make?"
    	    ans = round_2_money(profit)
        else:
            q = name + " buys some " + item1 + " for £" + round_2_money(total) + " and sells them all for £" + round_2_money(profit) + " profit. How much does " + name + " sell them for?"
            ans = round_2_money(profit + total)
    else:
        unit_spend_price = random.randint(0,2) + round(random.random(),2)
        quantity = random.choice([10,20,30,40])
        total_spend = unit_spend_price * quantity
        if unit_price == 1:
            total_sales = random.randint(round(total_spend,0),2*round(total_spend,0))
            profit = total_sales - total_spend
            q = name + " buys " + str(quantity) + " " + item1 + " for £" + round_2_money(unit_spend_price) + " each and sells them all for £" + round_2_money(total_sales) + ". How much profit does " + name + " make?"
            ans = round_2_money(total_sales - total_spend)
        else:
            unit_sale_price = random.randint(round(unit_spend_price+1,0),2*round(unit_spend_price+1,0)) + round(random.random(),2)
            total_sales = unit_sale_price * quantity
            q = name + " buys " + str(quantity) + " " + item1 + " for £" + round_2_money(unit_spend_price) + " each and sells them for £" + round_2_money(unit_sale_price) + " each. How much profit does " + name + " make?"
            ans = round_2_money(total_sales - total_spend)

    return q,ans

def gen_profit(n,a,b,c,d,e):
    questions = []
    answers = []
    count = [i for i in range(10)]
    for i in count:
        if i < 3:
            q,a = profit(0,random.randint(0,1))
        elif i < 6:
            q,a = profit(1,0)
        else:
            q,a = profit(2,0)
        questions.append(q)
        answers.append(a)
    return {'questions':questions, 'answers':answers, 'count':count}





















