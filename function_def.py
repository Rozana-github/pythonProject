
# define a function
def showdata():
    print("I am the best")
# call a function
showdata()
showdata()
showdata()

# function argument where information can be passed as parameter
def sum(a,b):
    print(a+b)
sum(10, 30)
sum(2, 30)

# default parameter argument
def sum1(a, b= 1):
    print(a+b)
sum1(20)
sum1(10, 30) # b=1 value will be overwide by 30


# return value

def square(x):
    return x*x, x*2

s = square(5)
print(s)


