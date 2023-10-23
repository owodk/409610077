def sayhihi(num): #括號個數需相同
    print('helllo!')
    print('hello!')
    
sayhihi(1.5>3) #括號個數需相同
print('hihi')
#sayhihi(1.5>3)
#print('hihi 2')

#%%
def CtoF1(degreeC):
    degreeF = degreeC *1.8 + 32
    print('攝氏', degreeC, '度可以轉換成華氏', degreeF,'度')
temperatureC = eval(input('請輸入攝氏溫度'))
CtoF1(temperatureC)

#%%
def teatime(dessert,drink = '紅茶'):
    print('我的甜點:',dessert,'；飲料:',drink, sep="")
teatime('馬卡龍', '拿鐵')
teatime('蛋糕')
teatime(drink = '奶茶', dessert = '鬆餅')
teatime('泡芙',drink = '水果茶')
#%%
def cal(x,y):
    div = x // y
    mod = x % y
    return div, mod
a, b = cal(120, 7)
print('120除以7的商數為', a, ',餘數為' ,b)
c, d = cal(250, 15)
print('250除以15的商數為', c, ',餘數為',d)
#%%
x = 30
y = 20

if x > y:
   z = x + y
   print('x大於y ',z)
#%%
score = eval(input('請輸入數學分數(0~100):'))
if score>=60:
    print('及格')
else:
    print('不及格')
#%%
score =eval(input('請輸入數學成績(0~100):'))
if score>=90:
    print("甲等")
elif score>=80:
    print("乙等")        
elif score>=70: 
    print("丙等")
elif score>=60:   
    print("丁等")
else:
    print("不及格")