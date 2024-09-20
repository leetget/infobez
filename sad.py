with open('data.txt','r',encoding="utf8") as file:
    data = file.read().replace('\n','')
    #print(data)
def Autoreplace(x,a,b):
    x_temp = x.replace(a,'*')
    x_temp = x_temp.replace(b,a)
    x = x_temp.replace('*',b)
    return x
data = Autoreplace(data,'У',' ')
#data = Autoreplace(data,'Х','И')
data = Autoreplace(data,'Ф','Э')
data = Autoreplace(data,'Я','Т')
data = Autoreplace(data,'П','О')

print(data)##