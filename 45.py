def word():
    print('需要缴纳的个人所得税是%d元，扣除税后的实际个人收入为%d元'%(a,b))
money = int(input('请输入你的收入金额:'))
if money <= 3500:
    a = 0
    b = 3500
    word()
elif money > 3500 and money <= 5000:
    a = (money - 3500)*3/100
    b = money -a 
    word()
elif money > 5000 and money <= 8000:
    a = 45 + (money - 5000)*10/100
    b = money - a 
    word()
elif money > 8000 and money <= 12500:
    a = 45 + 300 + (money - 8000)*20/100
    b = money - a 
    word()
elif money > 12500 and money <= 38500:
    a = 45 + 300 + 900 + (money - 12500)*25/100
    b = money - a
    word()
elif money > 38500 and money <= 58500:
    a = 45 + 300 + 900 + 6500 +(money-38500)*30/100
    b = money - a
    word()
elif money > 58500 and money <= 83500:
    a = 45 + 300 + 900 + 6500 + 6000 +(money - 58500)*35/100
    b = money - a 
    word()
elif money > 83500:
    a = 45+300+900+6500+6000+8750+(money-83500)*40/100
    b = money - a
    word()
