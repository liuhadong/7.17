w1 = 'I,love,python'
print(w1[2:])
w2 = 'aabbccddee' 
a = w2.replace('dd','ff')
print(a)
w3 = 'ab2b3n5nn2n67mm4n2'
b = w3.count('n')
print('字母n出现的次数为%d'%b)
zidian = {} 
for i in w3:
    if i in zidian.keys():
        zidian[i] += 1
    else:
        zidian[i] = 1
print(zidian)
