#zip function

l = [10, 20, 40, 30]
l1 = [5, 6, 7, 8, 10]

for a, b in zip(l,l1):
    print(a, b)

    # another way

l = [10, 20, 40, 30]
l1 = [5, 6, 7, 8, 10]

t = len(l)
for h in range(t):
    print(l[h], l1[h])