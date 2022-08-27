w = "Welcome to RozSoft.tech"
print(w)
print(w[6])


print(w[-1])

#slising

print(w[0:7])
print(w[0::2]) # increment qfter each 2 charachter
print(w[2])
print(w[-1:-10:-1 ])
print(w[-1::-1 ]) # reverse by slising format

# string editing based on lenth

t=len(w)
print(t)

for a in range(t):
    # print(a) #this will print only the array of the text
    print(w[a]) # to see the text in the array
print(w[0])


   # " string iteration "

s = "this is sting iteration"
p = s[-1::-1]
print(p)

l = len(s)
print(l)
print(s)

# using for loop

for a in range(l-1, -1, -1):
    print(s[a])

#second method

b = "welcome to sting editing"
for a in b:
    print(a) # you cannot reverse it , to revese it you have to apply following step and revese the text first

r = (b[-1::-1])
print(r)

for a in r:
    print(a)

#some more String function

#lower()
#upper()
#title()
#capitalize()

z = "what do you want?"
n = z.lower()
print(n)

u = z.upper()
print(u)

c = z.capitalize()
print(c)

f = z.title()
print(f)

#some other function
# find()
#index()
#isalpha()
#isalnum()

d = "Welcome"
print(d.find('e')) # will show you the index number

print(d.find('z', -2))

#isalpha()
w = 'abc'
print(w.isalpha())
print(w.isdigit())

w = '123'
print(w.isdigit())
print(w.isalnum())

y = chr(65)
print(type(y), y)

g = ord('b')
print(type(g), g)






