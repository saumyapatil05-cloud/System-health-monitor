# slice operator
fruits=["apple","pears","strawberries"]
text="Hello I like python"

#print(text[start:stop:step])
print(text[1:])  #default start and stop just put [::]

print(fruits[1::2])

fruits[1:1]=['mango']
print(fruits)
