#%%
X=list()
print(X)
Y=list([1,2,3])
x2=[]
print(x2)
y3=[1,2,3]
print(y3)
#%%
L=[2,5,8,7,94,41,6,668]
del L[4]
del L[8]
print(L)
#%%
#任意物件的串列
a=[3,4,5]
b=[5,4,'哈囉!']
c=[]
d=[45,[a,b]]
e=a+b
#串列的操作
b[0]=42
x=a[1]
y=b[1:3]
z=d[1][0][1]
#%%
[1,2,3,4,'喵!']==[555,5,55,5]
[1,2,3]==[3,2,1,6]
#%%
print(3 in [2,3,63,5,4])
print('owo'in [5,'bob'])
#%%
    #0,1,2,3,4,5,6,7,8
L = [1,2.3,54,5,47,55,5,2]
L[2:5]
                #-3,-2,-1
L[0:-2]
#%%
listc=[i for i in range(10)]
print(listc)
#%%
listc2=[j+3 for j in range(10)]
print(listc2)
#%%
num1=[1,3,5,7,9]
num2=[2,5,8,11,14]
num1.append(11)
print(num1)
num1.extend(num2)
print(num1)
num1.count(11)
num1.index(9)
num1.insert(3,666)
print(num1)
num1.pop()
print(num1)
#%%
tup=tuple()
print(tup)
tup2=tuple((1,2,3))
print(tup2)
#%%
a=(3,4,5,6,7)
b=()
c=(2,[3,5],(10,11,12))
d=a[1]
e=a[1:3]
f=c[1][1]
#%%
#可減號不可加法
s1={1,2,3,4,5}
s2={3,4,5,6,7,8}
s3=s1-s2
print(s3)
print(s1[1:3])
#%%
A={1,2,3,4,5,6,7,8,9}
print(len(A))
print(max(A))
print(min(A))
print(sum(A))

#%%
x={'A':100,'B':200}
y={'B':200,'A':100}
print(x==y)
print(x)
print(y)

A={'one':122,'two':211,'three':214}
x=A['one']
print(x)

A['two']=123
print(A['two'])
#del刪除
A={'one':122,'two':211,'three':214}
del A['one']
print(A)
#%%
#dict相關函數 key()、values()、items()
dic={'x':14,'y':56,'z':59}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
