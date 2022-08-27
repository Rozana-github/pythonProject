import math
import random


x = 10.5
print(math.ceil(x))

p = -10
print(math.fabs(p))

q = 5
print(math.factorial(q))

l = [10, 20, 30, 40, 50]
print(math.fsum(l))

print(math.sqrt(16))

print(random.randrange(1,9))
print(random.randint(1,9))
print(random.choice(l))

r = random.random() # betweet 1,0
print(r)

t = [10, 20, 30, 40, 50]
random.shuffle(t)
print(t)

u = random.uniform(3, 9)
print(u)

