total = 0
f = open("test.csv", "w")
print("Type 'end' to end the script.")
while True:
    name = input("Enter a name: ")
    if name.lower() == "end":
        f.close()
        break
    f.write(name+",")
