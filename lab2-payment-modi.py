# lab2
# algebraic equation
# payment = (((1+rate)^years)*principal*rate/(1+rate)^years-1)
# use variables and two decimal places
# find out annual and monthly payment

principal_in = ((raw_input('Please enter the amount you borrowed:')))
# enter with dollar sign
principal = float(principal_in.replace('$',''))
#print principal
rate_in = ((raw_input('Please enter the interest rate:')))
# enter with %
if rate_in.find('%') == -1:
    rate = float(rate_in)
    #print rate
else:
    rate_hundred = float(rate_in.replace('%',''))
    rate = float(rate_hundred/100)
#print rate
years = (input('Please enter the year you required to repay the loan:'))
#print years
#print("Annual payment is:")
print("Annual payment is:"+"{:.2f}".format((principal*((1+rate)**(years))*rate)/((1+rate)**years-1)))

# output
payment = (principal*((1+rate)**(years))*rate)/((1+rate)**years-1)
mon_payment = payment/12
print ("Monthly payment is:""{:.2f}".format(mon_payment))
print ("Total payment for life is:"+"{:.2f}".format(years*payment))

# input income
income = float((input('Please enter the annual income:')))
mon_income = float(income/12)
if mon_payment > mon_income:
    if rate >= .05:
        print("you should refinance")
    else:
        print("you should seek financial counseling")
else:
    print("make sure to make all payment on time")
