file = open("file.txt","r")
f=file.readlines()

newlist=[]
for line in f:
#	newlist.append(line[:-1])  or we can do
	 newlist.append(line.strip())

print(newlist)
