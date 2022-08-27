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
    1. Enqueue (Push) operation
    2. Dequeue (Pop) the fist element
    3. rear element 
    4. Front element 
    5. Display Queue
    6. Exit 
    '''))

    if c == 1:
        n = input("enter the value :-")
        l.append(n)
        print(l)

    elif c == 2:
        if len(l) == 0:
            print("empty queue")
        else:
            del l[0]
            print(l)

    elif c == 3:
        if len(l) == 0:
            print("empty queue")
        else:
            print("last element of the queue", l[-1])


    elif c == 4:
        if len(l) == 0:
            print("empty queue")
        else:
            print("first element of the queue", l[0])

    elif c == 5:
        print("Display Queue", l)

    elif c == 6:
        break

    else:
        print("entered invalid value!!!")


