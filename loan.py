
## input and calculations ##
loanAmount = float(input('Enter loan amount: \n'))
years = float(input('How many years will you have the loan? \n')) * 12   # *12 calculates number of payments
interestRate = (float(input('Enter Interest Rate: \n')) / 100 / 12)
monthlyPayment = loanAmount * (interestRate * (1 + interestRate) ** years) / ((1 + interestRate) ** years -1)
monthlyPayment = round(monthlyPayment, 2)
#monthlyInterest = round((loanAmount * interestRate/100/12),2)
#monthlyBalance = float(loanAmount - (monthlyPayment - monthlyInterest))
monthlyBalance = 1.0000
# print("The monthy payment is\n (%.2f) " % monthlyPayment)





print ("Month", "\t\t", "Payment", "\t\t", "Interest", "\t\t", "Balance")
print ("-----", "\t\t", "-------", "\t\t", "--------", "\t\t", "-------")

month = 0
while month < years:
    month += 1
    monthlyInterest = round((loanAmount * interestRate), 2)
    monthlyBalance = round(float(loanAmount - (monthlyPayment - monthlyInterest)), 2)

    print (month, "\t\t", monthlyPayment, "\t\t", monthlyInterest, "\t\t\t", monthlyBalance )
