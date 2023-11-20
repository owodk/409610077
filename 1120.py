#%%
with open('owo.txt','w') as file:
    file.write('456123\n')
    file.write('456\n')
    file.write('789\n')


with open("owo2.txt") as file:
    data=file.read()
    print(data)


#%%
import calendar
print(calendar.month(2019,1))

import calendar as cal
print(cal.month(2019,2))

from calendar import month
print(month(2019,3))

#%%
try:
   a=0
   b.split()
   b=0
except:
   c=0

X=eval(input("請輸入被除數X:"))
Y=eval(input("請輸入除數Y:"))
Z=X/Y
print("X除以Y的結果等於",Z)
#%%
try:
    X=eval(input("請輸入被除數X:"))
    Y=eval(input("請輸入除數Y:"))
    Z=X/Y
except ZeroDivisionError:
    print("除數不得為0")
except Exception as e1:
    print(e1.args)
else:
    print("沒有捕捉到例外!X除以Y的結果等於",Z)
finally:
    print("離開try...except區塊")