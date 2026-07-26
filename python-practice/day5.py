fruits=["apples","pears","orange"]

for fruit in fruits:
	if fruit=="pears":
		print(fruit)
	else:
		print("not pears")

for x in range(len(fruits)):     #len() gives length
	if fruits[x]=="pears":
		print(fruits[x])
	else:
		print("Not a pear")
