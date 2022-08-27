'''
key point
 input() : to take input from key board
 int() : int type input
 float() : define float type input
 eval() : it can work both for int() and float()
'''

a = input("enter the value: ")
print(a)

c = input("enter the value c : ")
d = input("enter the value d : ")

print("sum of the c and d :", (c+d))  # this will show as string if we dont identifiy the data type

#type casting

a = int(input("enter value a:"))
b = float(input("enter value b:"))
print(a+b)

#eval() can be used for the place of int() and float()

e = eval(input( "enter value e :"))
d = eval(input( "enter value d:"))

print("output: ", (e+d))
