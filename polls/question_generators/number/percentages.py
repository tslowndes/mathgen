import random
from decimal import Decimal
import datetime
from polls.question_generators import tools

def interest(compound_simple,inc_dec=0):
    amount = random.randint(1,25) * 1000
    rate = random.randint(1,10)
    if inc_dec == 1:
        rate = rate + round(random.random(),1)
    years = random.randint(2,10)
    name = tools.name_chooser()
    if inc_dec == 0:
        savings_or_loan = [' opens a savings account and deposits ', ' opens an ISA and deposits ', ' takes out a loan of ', ' buys a car on finance for ', ' takes out a mortgage to buy a house for ']
        a = random.choice(savings_or_loan)
        if 'house' in a:
            if amount < 10000:
                amount = amount * 100
            else:
                amount = amount * 10

        savings_or_loan2 = [' have ' , ' have ', ' owe ', ' owe ', ' owe ']
        b = savings_or_loan2[savings_or_loan.index(a)]

        q = name + a + '£' + tools.readable_digits(str(amount),1) + ' at a compound interest rate of ' + str(rate) + '%. How much do they ' + b + ' after ' + str(years) + ' years?'

        ans = '£' + str(round(amount * (1 + (rate/100))**years,2))
    else:

        items = ['A house is valued at £{price:.2f}.',
                'In the Arctic, there are {price:.2f} polar bears.',
                'A car is bought for £{price:.2f}.',
                'In a colony, there are {price:.2f} ants.',
                'A tree is {price:.2f} when it is planted.',
                'A full water tank holds {price:.2f} litres.',
                'A plane can carry {price:.2f} litres of fuel.']
        texts = ['It depreciates by ',
                'The population decreases by ',
                'The car decreases in value by ',
                'The population of ants increases by ',
                'The tree grows by ',
                'Due to a leak, the volume of the tank is decreasing by ',
                'When flying, the plane uses fuel at a rate of ']
        time_unit = ['year', 'year', 'year', 'day', 'week', 'day', 'hour']
        end = ['How much is the house worth after ',
                'How many polar bears are there after',
                'What is the value of the car after',
                'How many ants are there in the colony after',
                'How tall is the tree after ',
                'How much water is left in the tank after',
                'How much fuel does the plane have after']

        a = random.randint(0,len(items)-1)
        q = items[a].format(price = amount) + ' ' + texts[a] + ' ' + str(rate) + '% every ' + time_unit[a] + '. ' + end[a] + ' ' + str(years) + ' ' + time_unit[a] + 's?'
        if a == 0 or a == 1 or a == 2 or a == 5 or a ==6:
            ans = str(round(amount * (1 - (rate/100))**years,2))
        else:
            ans = str(round(amount * (1 + (rate/100))**years,2))



    return q,ans

def gen_interest(compound_simple,inc_dec,c,d,e,f):
    qs = []
    ans = []

    for i in range(10):
        q, a = interest(compound_simple,inc_dec)

        qs.append(q)
        ans.append(a)

    return {'count': [i for i in range(0, 10)], 'questions': qs, 'answers': ans}


def percentages_non_calc(n=-1,compound=0,calc=0, facts=0, increase=0, reverse = 0):
    if calc == 0:
        easy_small = [1,5,10]
        easy_big = [20,25,50]

        if facts == 1:
            percentage = random.choice(easy_small + easy_big)
            n = str(100 / percentage)
            if n[-2] == '.':
                n = n[:-2]
            if random.randint(0,1)==0:
                q = '$100 \div [\;\;] = ' + str(percentage) + '$'
                ans = '$100 \div ' + str(n) + ' = ' + str(percentage) + '$'
            else:
                ans = '$' + str(percentage) + r' \times ' + str(n) + ' = 100 $'
                if random.randint(0,1)==0:
                    q = '$' + str(percentage) + r' \times [\;\;] = 100 $'
                else:
                    q = r'$ [\;\;] \times ' + str(n) + ' = 100 $'
        else:
            if compound == 0:
                percentage = random.choice(easy_small + easy_big)
            else:
                percentage = 25
                while percentage ==25:
                    if random.randint(0,1)==0:
                        percentage = random.choice(easy_big) + random.choice(easy_small)
                    else:
                        percentage = random.choice(easy_small) * random.randint(2,9)
    else:
        if n < 8:
            if random.randint(1,3) != 3:
                percentage = random.randint(1,99)
            else:
                percentage = random.randint(1,9)
        else:
            a = round(random.random(),1)
            while a == 0:
                a = round(random.random(),1)
            percentage = random.randint(1,99) + a


    if facts == 0:
        if str(percentage) == '25':
            amount = random.randint(2,10)*4
        elif str(percentage) == '20':
            amount = random.randint(2, 10) * 5
        elif str(percentage) == '50':
            amount = random.randint(2, 10) * 2 * random.choice([1,10])
        elif str(percentage)[-1] == '0':
            amount = random.randint(2,10) * 10
        elif str(percentage)[-1] == '5':
            amount = random.randint(2,10) * 20
        else:
            amount = random.randint(2,9) * 100
        if calc == 1:
            amount = random.randint(1,200)#int(str(amount/10)[:-2])
        if reverse == 0:
            if increase == 0:
                q = str(percentage) + '% of ' + str(amount)
                percentage = Decimal(percentage)
                amount = Decimal(amount)
                ans = str(percentage / Decimal(100.0) * amount)
                if "." in ans:
                    while ans[-1] == "0":
                        ans = ans[:-1]
                if ans[-1] == ".":
                    ans = ans[:-1]
            elif increase == 1:
                q = "Increase " + str(amount) + " by " + str(percentage) +"%"
                ans = tools.strip_0(round(amount * (1 + (percentage / (100.0))),5))
            elif increase == 2:
                    q = "Decrease " + str(amount) + " by " + str(percentage) +"%"
                    ans = tools.strip_0(round(amount * (1 - (percentage / (100.0))),5))
        else:

            percentage = Decimal(percentage)
            amount = Decimal(amount)
            ans = tools.strip_0(str(percentage / Decimal(100.0) * amount))


            a = random.randint(1,7)
            if a == 1:
                qualities = [" have brown hair", " wear glasses", " are left handed"]
                quality = random.choice(qualities)

                q = str(str(percentage) + "% of the students in a maths class " + quality + ".\n " +
                        "There are " + str(ans) + " students who " + quality + ".\n " +
                        "How many students are there in the class?")
            elif a == 2:
                qualities = [" is sugar", " is fat", " is caramel"]
                quality = random.choice(qualities)

                q = str(str(percentage) + "% of a chocolate bar " + quality + ".\n " +
                "There are " + str(ans) + " grams of " + quality[4:] + " in the chocolate bar. \n" +
                "What is the total mass of the chocolate bar?")
            elif a == 3:
                qualities = [" is car chases", " is fight scenes"]
                quality = random.choice(qualities)
                q = str(str(percentage) + "% of a movie " + quality + ".\n " +
                "The " + quality[4:] + " last for " + str(ans) + " minutes.\n " +
                #"There are " + str(ans) + " minutes of " + quality[4:] + " in the movie. \n" +
                "How long is the movie?")
            elif a == 4:
                qualities = [ " is uphill", " is downhill", " is along flat roads", " is through the mountains"]
                quality = random.choice(qualities)
                q = str(str(percentage) + "% of a cycling race " + quality + ".\n " +
                "Cyclists ride " + quality[4:] + " for " + str(ans) + " miles. \n" +
                "How long is the race?")
            elif a == 5:
                qualities = [" are broken", " are chocolate", " are wafers"]
                quality = random.choice(qualities)
                q = str(str(percentage) + "% of the biscuits in a tin " + quality + ".\n " +
                "Out of all the biscuits, " + str(ans) + quality + ".\n " +
                "How many biscuits are in the tin?")
            elif a == 6:
                q = str(str(percentage) + "% of a tank is filled with petrol.\n " +
                "There are " + str(ans) + " litres of petrol in the tank.\n " +
                "How many litres are in the tank when it is full?")
            elif a == 7:
                qualities = [" have a bathroom", " include breakfast", " have a TV"]
                quality = random.choice(qualities)
                q = str(str(percentage) + "% of the rooms in a hotel " + quality + ".\n " +
                "At the hotel, " + str(ans) + " rooms " + quality + ".\n " +
                "How many rooms are at the hotel?")
            ans = amount

    return q,ans

def gen_percentages_non_calc(n, compound, calc,facts,increase,reverse):
    qs = []
    ans = []
    if increase == 3:
        increases = [1,1,1,1,1,2,2,2,2,2]
        random.shuffle(increases)
    for i in range(n):
        if increase != 3:
            q, a = percentages_non_calc(i,compound,calc,facts,increase, reverse)
        else:
            q, a = percentages_non_calc(i,compound,calc,facts,increases[i], reverse)

        qs.append(q)
        ans.append(a)

    return {'count': [i for i in range(0, n)], 'questions': qs, 'answers': ans}


