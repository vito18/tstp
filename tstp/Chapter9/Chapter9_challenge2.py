enter = input("Enter something: ")

with open("challenge2.txt", "w") as f:
    f.write(enter)

with open("challenge2.txt", "r") as r:
    print(r.read())
    
