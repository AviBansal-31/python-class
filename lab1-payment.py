# one-line required
# payment = (((1+rate)^years)*principal*rate/(1+rate)^years-1)

"{:.2f}".format((Decimal(input('Please enter the amount of money you borrowed:'))*(1+Decimal(input('Please enter the interest rate:')))*(Decimal(input('Please enter the interest rate:'))))/Decimal((1+input('Please enter the interest rate:'))**input('Please enter the year to repay the loan in full:')-1))
