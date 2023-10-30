with open('data.txt','w') as file:
    file.write('寫入資料到檔案\n')
    file.write('cjufiygh.jfiu\n')
    file.write('5646666')


with open('data.txt','r') as file:
    data=file.read()
    print(data)
