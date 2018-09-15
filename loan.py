
## input and calculations ##
loanAmount = float(input('Enter loan amount: \n'))
years = float(input('How many years will you have the loan? \n')) * 12   # *12 calculates number of payments
interestRate = float(input('Enter Interest Rate: \n')) / 100 / 120
monthlyPayment = loanAmount * (interestRate * (1 + interestRate) ** years) / ((1 + interestRate) ** years -1)
monthlyInterest = round((loanAmount * interestRate/100/12),2)
monthlyBalance = float(loanAmount - (monthlyPayment - monthlyInterest))

# print("The monthy payment is\n (%.2f) " % monthlyPayment)


month = 0
while monthlyBalance > 0:
    month += 1


print ("Month", "\t\t", "Payment", "\t\t", "Interest", "\t\t\t", "Balance")
print ("-----", "\t\t", "-------", "\t\t", "--------", "\t\t\t", "-------")
