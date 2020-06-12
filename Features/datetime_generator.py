import datetime as dt
import calendar as cal
import collections as clc
import random

C = cal.Calendar()
choices = C.yeardatescalendar(2020, width =1)
print(choices[0])

def returnchoice(a,b,c):
    return random.choice(choices[a][b][c])

def displayer(days):
    mnths = days/30.0
    sment = "{} days since Today''s date.\nWhich is {} months ago.\n\n".format(days,mnths)
    print(sment)


ents = clc.OrderedDict()
strt = [0,1,2]
strt2 = range(1)
strt3 = range(1)

for i in range(100):
    v1 = random.choice(strt)
    v2 =  random.choice(strt2)
    v3  = random.choice(strt3)
    ents[i] = returnchoice(v1, v2, v3)
    k  = dt.date.today()
    d = (k - ents[i]).days
    displayer(d)
