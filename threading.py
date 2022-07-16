from datetime import datetime

import time
x=0
t=time.time

while(True):
    if(time<20):
        if(time==x):
            x=t+5
            print ('thread 1')
            print ('thread 2')

    if (time>20 and t<38):
        if (t==x):
            print("threading 2")
            print("threading 3")

    if(t>38 and t<60):
        print('thrad 2')
        #here  we will apply thread method
        print('thrad 1')
    else:
         False
