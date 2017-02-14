# lab2
# algebraic equation
# payment = (((1+rate)^years)*principal*rate/(1+rate)^years-1)
# use variables and two decimal places
# find out annual and monthly payment

principal = float((input('Please enter the amount you borrowed:')))
print principal
rate = float((input('Please enter the interest rate:')))
print rate
years = (input('Please enter the year you required to repay the loan:'))
print years
print("{:.2f}".format((principal*((1+rate)**(years))*rate)/(1+rate)**years-1))


# '$'
payment = (principal*((1+rate)**(years))*rate)/(1+rate)**years-1
mon_payment = payment/12
print (payment/12)

income = float((input('Please enter the annual income:')))
mon_income = income/12
if mon_payment > mon_income:

    if rate >= .05:
        print("you should refinance")
    else:
        print("you should seek financial counseling")
