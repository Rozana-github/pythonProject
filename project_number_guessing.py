import random
cnumber = random.randrange(1, 11)

userinput = int(input("enter your number"))

if userinput > cnumber:
    print("the computer number", cnumber)
    print("your number is greater than computer number")

elif userinput < cnumber:
    print("the computer number", cnumber)
    print("your number is smaller than computer number")
else:
    print("the computer number", cnumber)
    print("you are perfect ! wao !")

