#list iteration
l = [10, 20, 30, 40, 60, 80, 90]
t = len(l)
print(t)

for a in range(t): # 0 to 6
    print(l[a])


for a in l:
    print(a)


# for  reverse the index
for a in range(t-1, -1, -1):
    print(l[a])

