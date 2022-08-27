'''
print(
+add
-subtract
*multiplication
/divide)
'''

print( '''+ add
-subtract
*multiplication
/divide''')
a = int(input("enter first value:"))
b = int(input("enter second value:"))
opr = input("enter the opr: ")

if opr == '+' :
    print("addition", a+b)

elif opr == '-':
    print("substruction", a - b)

elif opr == '*':
    print("multiplication", a * b)

elif opr == '/':
    print("Division", a / b)

else:
    print("invalid operator")

if opr != "*" and opr != "+" and opr != "/" :
    print("invalid operator")







