#named indexes:

txt1 = "Welcome to {fname} {lname}".format(fname="RozSoft.tech", lname="for python learning")
print(txt1)


#numbered indexes:
txt2 = "Welcome to {0} {1}".format("python", "learning")
print(txt2)

# empty placeholders:
txt3 = "Welcome to {} {}".format("learn", "with Rozana")
print(txt3)

w = "Welcome {} to {} Rozsoft.tech".format("hello", 20)
print(w)

w = "Welcome {} to {} Rozsoft.tech".format(20, 30)
print(w)

k = "Welcome {b:10} to {a} Rozsoft.tech".format(a = 40, b = 30)
print(k)

k = "Welcome {b:^10} to {a} Rozsoft.tech".format(a = 40, b = 30)
print(k)

k = "Welcome {b:<10} to {a} Rozsoft.tech".format(a = 40, b = 30)
print(k)

k = "Welcome {b:>10} to {a} Rozsoft.tech".format(a = 40, b = 30)
print(k)

'''
sting will be changed depend on the following sign based in string formating based on format methot
---------10 <
----10-----^
10--------->
'''