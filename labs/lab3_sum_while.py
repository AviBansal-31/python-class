# lab3
#  sum all numbers between the given number plus 100

number = input("please enter the number:")
sum = 0
sum_odd = 0
sum_even = 0
i = number
i_odd = number
i_even = number + 1

while i <= number + 100:
  sum += i
  i += 1
print("the sum is:")
print(sum)

# sums all of the odd numbers between that number plus
if number % 2 == 0:
    while i_even <= number + 101:
        sum_even += i_even
        i_even += 2
    print("the odd sum is:")
    print(sum_even)
else:
    while i_odd <= number + 100:
        sum_odd += i_odd
        i_odd += 2
    print("the odd sum is:")
    print(sum_odd)
