d = {'a':1,'b':2,'c':3}
for i in d.keys():
    print(i)
for n in d.values():
    print(n)
d2 = {'d':4}
d.update(d2)
print(d)
