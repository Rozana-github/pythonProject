'''
-ordered sequence type data,
-immutable,
-(, , ,)
- also worked based on index
- only one data will not tel as a tuple , in that case it will be consider as string
   t = ("python") - this is not a tuple it is a string
'''

# create tuple
t = (20, 25, 30, 50, 55)
a = t[2]
print(a)

#Get value of tuple

p = len(t)
print(p)

for a in range(p):
    print(a) # only index
    print(t[a]) #index with data


#another way to access tuplel from direct tuple variable

for a in t:
    print("from direct tuple",a)

    # tuple function
    # min()
    # max()
    #count()
    #index()
    #sum()

m = min(t)
print(m)


n = max(t)
print(n)

c = t.count(20)
print(c)

s = sum(t, 10)
print(s)

