'''

1. Push -  use insert into the list
2. POP - Delete from the list
3. Peek _ to see the last element from the list
4. Display - to see the full list
 The stack is a linear data structure and stored data sequencially; store item LIFO , last in Fisrt out .

'''


l = []

while True:
    c = int(input('''
    1. Push operation
    2. Pop operation
    3. Peek operation 
    4. Display operation
    5. Exit 
    '''))

    if c == 1:
        n = input("enter the value :-")
        l.append(n)
        print(l)

    elif c == 2:
        if len(l) == 0:
            print("empty stack1")
        else:
            p = l.pop()
            print(p)
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("empty stack1")
        else:
            print("last element of the stack", l[-1])
    elif c == 4:
        print("Display list", l)

    elif c == 5:
        break

    else:
        print("entered invalid value!!!")


