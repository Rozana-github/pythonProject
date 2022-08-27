'''

a set is a collection
which is unordered and un indexed , that is iterable , mutable and has no duplicate elements.
{} to wtire code with python
set fuction:
-set()
- add()
-pop()
-remove()
-clear()
-discard()
-update()
'''

#how to convert a list in a set?

l = [10, 30, 40, 40, 50]
s = set(l)
print(s, type(s))

# how to add into a set

s.add(45)
s.add(40)
print(s)

# pop()
s.pop() # it will delete randomly
print(s)

# remove()
s.remove(10)
print(s)

# discard()
s.discard(30)
print(s)

#clear()

s.clear()
print(s)

#update s set aded list l

s.update(l)
print(s)

