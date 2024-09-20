with open('data.txt','r',encoding="utf8") as file:
    data = file.read().replace('\n','')
    print(data)

data = sorted(data, key=lambda x: x.lower(),reverse=True)

print(len(data))

i = 0

while(i< len(data) -1 ):
    if(data[i] != data[i+1]):
        print((str(data.count(data[i])) + " - " + data[i]))
    i+=1