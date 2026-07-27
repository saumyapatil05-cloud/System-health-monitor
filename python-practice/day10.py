#file=open("file.txt","w")
#
#file.write("python\n")
#file.write("I am learning to write in a file")
#file.close()

with open("file.txt","a") as f:
	f.write("\nI love cloud programming")

