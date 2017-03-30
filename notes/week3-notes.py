n = 5
while n<= 5
    print("counting down:{}".format(n))
#  n--
    n -= 1
else:
    print("we got to zero")

import random
number = random.randint(0,101)
print(number)
print("let the game begin")

guess = int(input('\nPlease input a number'))
while True:
    if number == guess:
        break
    elif number < guess:
        print('bigger')
    else:
        print('smaller')
    guess = int(input("please guess again"))
print("correct")


import random
n = random.randint(1,4)
counter = 0
counter2 = 0
while counter < 10:
    count += 10
    if counter % 2 ==0:
        continue
    while True:
        counter2 += 1
        if counter2 % 2 ==0:
            print('loop2:{0}'.format(counter2))
        else:
            break
    print('loop1:{0}'.format(counter1))
