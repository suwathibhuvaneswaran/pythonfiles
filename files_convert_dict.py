f = open("dictionary.txt","r")
temp={}
for line in f.readlines() :
    a,b = line.split()
    temp[a]=int(b)
print(temp)
