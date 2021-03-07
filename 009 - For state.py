#for statement
list=[1,2,3,4,5]
for x in list: # for variable(x) in list(range)
    print(x)

#other example

#string
str='abcdef'
for c in str:
    print(c)

#dictionary

asd={'v':98,'b':99,'n':100}
for v in asd:
    print(v)

#range()

for g in range(10):
    print(g)

"""
for variable in range:
    repeated execution

range :
string/list/tuple/dictionary/range()/objects that are able to be repeated
"""

list1=[1,2,3,4,5]
for f in list1:
    print(f)
    if f<3:
        continue
    else:
        break
"""
for variable in range:
...
continue # next repeat statement
...
break # end for statement
"""

list2=[1,2,3]
for q in list2:
    print(q)
    #break
else:
    print('Perfect')

"""
for variable in range:
repeat implement code
else:
execute after for statement
"""
