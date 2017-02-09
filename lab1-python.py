print("I am\n") # EOL
print("hi\ttab") # 4 spaces
print("this's") # work with '
# error print ("this "quote"")
1//3 => 0
5 ** 5 => 3125
5/2+3 => 5.5
1//4 *100 =>0
import math
math.log(5)
math.sin(5)


# day 2
.1+.1 => 0.2
.1+.2 => 0.300000000000000004

# floating point
from decimal import *
Decimal('.1')/Decimal('.2') => Decimal('0.5')
str(Decimal('.1')+Decimal('.2')) =>'0.3'

# change precision
getcontext().prec = 4
str(Decimal('.2')+Decimal('.3')) =>'0.6667'

# format strings
"{}".format(Decimal('2')/Decimal('3')) => '0.666667'
"{:.2f}".format(.1) => '0.10'
"{:0.2%}".format(.1) => '10.00%'
"{3:0.2f}, {2:0.2f}".format(1, 2, 3, 4) => '4.00, 3.00'

# getting input
input('please input:')
print('hello,{0}'.format(input('please enter:')))
input('number1')+input('number2')
float(input('num1:'))+float(input('num2:'))
#can input int
int(input('')) # cannot input float
# decimal will output Decimal('')
