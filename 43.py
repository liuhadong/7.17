for num1 in range(2,100):
    for num2 in range(2,num1):
        if num1 % num2 == 0:
            break
        num2 += 1
    else:
        print(num1,end=',')
    num1 += 1
print('')
