loanAmount = input('Enter loan amount: \n')
loanAmount = float(loanAmount)

years = input('How many years will you have the loan? \n')
years = float(years) * 12

interestRate = input('Enter Interest Rate: \n')
interestRate = float(interestRate) / 100 / 12

mortgagePayment = loanAmount * (interestRate * (1 + interestRate) ** years) / ((1 + interestRate) ** years -1)

print("The monthy mortgage payment is\n (%.2f) " % mortgagePayment)
