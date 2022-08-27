# program to convert a sting into list

s = input("enter the value:-")
print(s)

# now covert the entered sting into list

l = s.split()
print(l)

# if there is multiple sting entered then how to convert


p = []
for a in range(1, 4):
   n = input("enter the value" + str(a) +":- ")
   print(n)
   p.append(n)
print(p)
