import datetime as dt
import calendar as cal
import collections as clc
import random
import time

#---------------------------------------
def returnchoice(a,b,c):
    """
    """
    return random.choice(choices[a][b][c])

#----------------------------------------
def displayer(days):
    """
    """
    mnths = days/30.0
    if abs(int(days)) <= 7:
        sment = "WOW  SO CLOSE! ONLY {} days since Today''s date.\nWhich is {} months ago.\n\n".format(days,mnths)
        print(sment)
        #time.sleep(1)
        return 1
    else:
        sment = "{} days since Today''s date.\nWhich is {} months ago.\n\n".format(days,mnths)
        #print(sment)
        return 0




ents = clc.OrderedDict()
C = cal.Calendar()
z = C.yeardatescalendar(2020, width =12)

t  = dt.date.today()
rng = 1000
cnt = 0
k = range(0,7)

for i in range(rng):
    d = random.choice(k)
    chc  = random.choice( [random.choice(x) for x in z[0][:]][d])
    dy = (t - chc).days
    cnt += displayer(dy)

print(cnt)
hitperc = (cnt/rng)*100.0
print('Hit rate was {} %'.format(hitperc))


