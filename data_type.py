"""
a) numeric type :- 1. int 2. float 3. complex (immutable object)
b) sequence type :- 1. string = 'single coutasion' , " double coutusion" , #'''''' (mutable object)
                    2. List[] (mutable object slower than tuple; ordered sequence)
                    3.Tuple{} (imutable object but faster than list)
c) Dictionary { key : value} (mutable object ;  unordered collection of keys and values)
d) set s={ no duplicate value, unordered collection no duplicates} (mutable object)
"""

# numerical type

a = 5
print(a, "type of a ", type(a))
b=2.5
print(b, "type of b ", type(b))
c = 5 + 3j
print(c, "type of c ", type(c))


# String
string1 = 'hi'
string2 = "this is RozSoft.tech"
string3 = ''' for long text 
                      of
                  many lines'''

print(string1, type(string1))
print(string2, type(string2))
print(string3, type(string3))


# list
a = [10, 20, 30, 40] # mutable , we can change it
print(a, type(a))
a[1]= 15
print(a)

#tuple
t = {10, 'program', 30 + 4j, 40} # touple is not mutable
print(t, type(t))

#dictionary

d = {1: 'dhaka', 2 :'bangladesh' }
print(d, type(d))

#get vqlue of dictionary

print(d[1]) # get the value of fist city

# set

s = {10, 10, 20, 30}
print(s,type(s))
# set will remove duplicate value










