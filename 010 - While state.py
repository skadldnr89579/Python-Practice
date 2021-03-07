#while state

x=0
while x<10:
    x=x+1
    if x<3:
        continue
    print(x)
    if x>7:
        break

"""
while condition:
    code implement
    continue # back to while - code implement - continue
    ....
    break # while state end
"""

z=1
total=0
while 1:
    total=total+z
    if total > 100000:
        print(z)
        print(total)
        break
    z=z+1
    
