
#apr
apr = 0.009
loan = 7800
number_of_months = 60

total_interest = 0
monthly_payment_with_interest = 0
principal = loan
for i in range(0,60):
    interest = principal * (apr / 12)
    print "p:", str(principal), "      i: ", str(interest)
    principal = principal - (loan/number_of_months)
    total_interest += interest
    
print "Total INTEREST: ", total_interest

monthly_payment_with_interest = (loan + total_interest) / number_of_months
    
print "MONTHLY PAYMENT WITH INTEREST: ", monthly_payment_with_interest

