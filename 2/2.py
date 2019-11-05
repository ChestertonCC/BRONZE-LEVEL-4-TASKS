name = input("Enter your name: ")
f = open("test.txt", "x")
f.write(name)
f.close()
