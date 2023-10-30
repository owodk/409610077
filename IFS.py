i = 0
while i<3:
    print(i)
    i=i+1
#%%

answer = input("請輸入「快樂」的英文:")
while answer.upper()!= "HAPPY":
    answer = input("答錯了，請重新輸入「快樂」的英文:")
else:
    print("答對了!")
#%%
for i in range(5):
    print(i)


name='Bob'
for i in range(len(name)):
    print(i,name[i])
    
name='Bob' 
for i in name:
    print(i)
#%%
answer = input("請輸入「好」的英文:")

while answer.upper()!="GOOD":
 if answer.upper()=="QUIT":
    print("我不玩了!")
    break
    print("Bye!")
 answer = input("答錯了，請重新輸入「好」的英文:")
else:
   print("答對了!")  
#%%
i=0
while i<10:
   i=i+1
   if i%3!=0:
    continue
   i = i+2
   print(i)

