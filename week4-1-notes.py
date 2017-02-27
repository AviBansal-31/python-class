# range(5) creates a sequence 0-4, one number at a time
"""
for item in range(5):
    print(item)

for item in range(10,20):
    print(item)

for item in range(10,20, 2):
    print(item)

min_number = int(input("give a min value"))
max_number = int(input("give a max"))
if min_number % 2 ==0:
    min_number += 1
total = 0

for number in range(min_number, max_number + 1, 2):
    total += number
print(total)
for number in range(0,100):
    total += number
    if total > 100:
        print("we're over 100")
        print("the last number was {}".format(number))
        break

my_list = [5, 3, 2, 10, 9]
for item in my_list:
    print(item)

name = 'jimmy'
for cat in name:
    print(cat)
"""
def hello(name):
    print("hello,{}".format(name))
hello("cat")
hello("dog")
# print_separator()
def find_max(a, b):
    if a > b:
        print("max is".format(a))
    elif b > a:
        print("max is".format(b))
    else:
        print("{0} and {1} are equal".format(a,b))
find_max(5,10)
find_max(9,5)
find_max(8,8)

x =3
y =4
find_max(x,y)
name = 'sophia'
number = 10
def scope_test(number):
    # number only local in it
    print(name)
    print("the value of number is {}".format(number))
    number=7
    print("the value of number is {}".format(number))
# global one
scope_test(number)
print("number still {}".format(number))
# print_separator()
def print_favorite(name, thing='fishing'):
    print("hi, {0}, your favorite thing is {1}".format(name,thing))
print_favorite('jo')
print_favorite('jo', 'playing')
print_favorite('jim', thing = 'eating')

def print_more(name, animal='none',luck=0,color='none'):
    print("hi, {0}\n\tI see your color is {3},\n"
        "animal is {1}, \n\tand lucky number is {2}\n".format(name,animal,luck,color))
print_more('jo')
print_more('jim',luck=7)
print_more('kim',color='red',luck=9)
# if arguments include '=', include it when call
