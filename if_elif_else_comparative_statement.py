'''
if[condition1]:
   [statement1]

   elif[condition2]:
   [statement2]

   elif[condition3]:
   [statement3]

   else[condition4]:
   [statement4]

'''

student_number = int(input("enter students number"))
print("students number is", student_number)

if (student_number > 60 and student_number < 100):
    print("first division")
elif(student_number >45 and student_number< 59):
    print("second divition")
elif(student_number >33 and student_number< 44):
    print("third divition")
else:
    print("fail")
