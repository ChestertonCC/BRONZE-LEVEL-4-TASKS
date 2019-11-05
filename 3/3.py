f = open("test.txt", "w")
f.write("lluc bad")
f.close()
print("File 'test.txt' contains: ")
f = open("test.txt", "r")
print(f.read())
yn = input("Do you want to delete everything in it? (y/n) ")
f.close()
if yn == "y":
    f = open("test.txt", "r+")
    f.truncate(0)
else:
    f.close()
