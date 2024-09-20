with open('data.txt','r',encoding="utf8") as file:
    data = file.read().replace('\n','')
    #print(data)
def Autoreplace(x,a,b):
    x_temp = x.replace(a,'*')
    x_temp = x_temp.replace(b,a)
    x = x_temp.replace('*',b)
    return x

data = Autoreplace(data,"У"," ")

#data = Autoreplace(data,"З","О")
#data = Autoreplace(data,"В","Е")
#data = Autoreplace(data,"П","А")

#data = Autoreplace(data,"Р","И")
#data = Autoreplace(data,"Я","Н")
#data = Autoreplace(data,"Ч","С")
#data = Autoreplace(data,"С","Т")
#data = Autoreplace(data,"Б","Л")
#data = Autoreplace(data,"Й","В")
#data = Autoreplace(data,"Л","Р")
#data = Autoreplace(data,"Ф","М")
#data = Autoreplace(data,"Ш","К")
#data = Autoreplace(data,"Х","У")
#data = Autoreplace(data,"Ь","П")
#data = Autoreplace(data,"Г","К")
#data = Autoreplace(data,"Т","Н")











print(data)##