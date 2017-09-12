#上部分为正确部分
from random import randint
passwd = randint(0, 20)
numCount = 0
print("Now let's guess,hope you feed me a number between 0~20")
while numCount < 10:
    value = input("> ")
    numCount += 1
    if not value.isdigit():
        print("Oh no!feed me interger numbers.You have {0} times to go!" .format(10-numCount))

    else:

        if  int(value) > passwd:
            print("bigger than,I want smaller one!You have {0} times to go!" .format(10-numCount))
        elif int(value) < passwd:
            print("Too small,now I like bigger one!You have {0} times to go!" .format(10-numCount))
        else:
            print("Wooo!you are so-o-o-o smart!Good job!")
            break

else:
    print("Let's have a rest!The right number is {0}" .format(passwd))

#----------------------------------------------------------------------------------------------
from random import randint 
passwd = randint(0, 20)
numCount = 0
print("Now let's guess,hope you feed me a number between 0~20")
while numCount < 10:
    value = input("> ")
    numCount += 1

    if not value.isdigit():
        print("Oh no!feed me interger numbers.You have %d times to go!" )

    else:

        if  int(value) > passwd:
            print("bigger than,I want smaller one!You have %d times to go!" .format(9 - numCount))
        elif int(value) < passwd:
            print("Too small,now I like bigger one!You have %d times to go!" .format(0 - numCount))
        else:
            print("Wooo!you are so-o-o-o smart!Good job!")
            break

else:
    print("Let's have a rest!')
#调试中，计数的部分，不清楚为什么不调用数字了，是否格式化的内容，只能直接调取字符，不能调用运算的部分。
#打印部分，又莫名其妙卡了
