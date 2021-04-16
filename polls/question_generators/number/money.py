from random import randint, random
from polls.question_generators.tools import *

def basic_purchase(number_of_items):
    item1 = random.choice(['pens', 'pencils','rulers'])
    item2 = random.choice(['Twix', 'Kitkats','cans of coke', 'bottles of Lucozade'])

    unit_price1 = round(random.random(),2)
    unit_price2 = round(random.random(),2)

    quantity1, quantity2 = randint(2,4), randint(2,4)

    name = name_chooser()

    note = random.choice([10,20])
    if number_of_items == 2:
        q = name + ' buys ' + str(quantity1) + ' ' + item1 + ' at £' + str(unit_price1) + ' each and ' + str(quantity2) + ' ' + item2 + ' at £' + str(unit_price2) + ' each. ' + name + ' pays with a £' + str(note) + ' note. How much change does ' + str(name) + ' get?'
        ans = '£' + str(note - ((quantity1 * unit_price1) + quantity2*unit_price2))
    else:
        q = name + ' buys ' + str(quantity1) + ' ' + item1 + ' at £' + str(unit_price1) + ' each. ' + name + ' pays with a £' + str(
            note) + ' note. How much change does ' + str(name) + ' get?'
        ans = '£' + str(note - ((quantity1 * unit_price1)))
    return q,ans

