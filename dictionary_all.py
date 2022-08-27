'''
1. unordered data
2. key: value pair where key will be unique but value can be similar
3. {} inside
4. Mutable

'''


#create dictionary

d = { 'name': 'python', 'fees': 8000, 'duration': '2 months' }
print(type(d))
print(d)

# acccess element form dictionary

n = d['name']
print(n)

# iterate through a dictionary

for a in d:
    print(a) # to see only keys
    print(d[a]) # to see the value of keys
    print(a, d[a]) # to see both keys and values together


'''
function for dictionary
1. get()
2. keys()
3. values()
4. items()
5. del()
6. pop()
7.dict()
8. clear()
'''

#1.get()
c = {'course': 'python', 'fees': 8000, 'duration': '2 months' }
n = c.get('course')
print(n)

#2. keys()

for a in c.keys():
    print(a)
#3. values()

for a in c.values():
    print(a)

#items

for a, b in c.items():
    print(a, b)

#5. del()

del c['course']
print(c)

#6. pop()

p = c.pop('fees')
print(p)

#7.dict()
b = dict( name ='python', price= 60)
print(b)

#update()

b.update({'duration':'2 months'})
print(b)

#8. clear()
# it will clear all data from dictionary

b.clear()
print(b)
print(type(b))

" How to insert value inside the dictionary"
b['cource_start'] = "7th september"
print(b)
b['place'] = "dhaka"
print(b)

# Create a nested dictionary
course = {
    'php':{'fees': 5000, 'duration': '2 months'},
    'python':{'fees': 5000, 'duration': '1 month'},
    'java':{'fees': 1000, 'duration':'2 months'}
}
print(course)

print(course['php']['fees'])

for k,v in course.items():
   # print(k,v)
    print(k,v['duration'],v['fees'])

# update()
course['java']['fees'] = 1000

" delete"
del course['duration']
print(course)

