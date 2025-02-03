# Function to compute mortgage payments across different schedules
def mortgage_payments(principal, rate, amortization):
    rate = rate / 100
    monthly_interest = ((1 + rate / 2) ** (2 / 12) - 1)
    semi_monthly_interest = ((1 + rate / 2) ** (2 / 24) - 1)
    bi_weekly_interest = ((1 + rate / 2) ** (2 / 26) - 1)
    weekly_interest = ((1 + rate / 2) ** (2 / 52) - 1)
    monthly_pmt = (((monthly_interest) * ((1 + monthly_interest) * (amortization * 12))) / (((1 + monthly_interest) * (amortization * 12)) - 1)) * principal 
    semi_monthly_pmt = (((semi_monthly_interest) * ((1 + semi_monthly_interest) * (amortization * 24))) / (((1 + semi_monthly_interest) * (amortization * 24)) - 1)) * principal 
    bi_weekly_pmt = (((bi_weekly_interest) * ((1 + bi_weekly_interest) * (amortization * 26))) / (((1 + bi_weekly_interest) * (amortization * 26)) - 1)) * principal 
    weekly_pmt = (((weekly_interest) * ((1 + weekly_interest) * (amortization * 52))) / (((1 + weekly_interest) * (amortization * 52)) - 1)) * principal 
    accelerated_bi_weekly_pmt = monthly_pmt / 2
    accelerated_weekly_pmt = monthly_pmt / 4
    
    return (
        round(monthly_pmt, 2), 
        round(semi_monthly_pmt, 2), 
        round(bi_weekly_pmt, 2), 
        round(weekly_pmt, 2), 
        round(accelerated_bi_weekly_pmt, 2), 
        round(accelerated_weekly_pmt, 2))

# Take user inputs and compute mortgage payments
principal_amount = float(input("Enter the loan amount: "))
interest_rate_input = float(input("Enter the annual interest rate: "))
loan_term = float(input("Enter the loan duration in years: "))

# Compute payments
monthly, semi_monthly, bi_weekly, weekly, accelerated_bi_weekly, accelerated_weekly = mortgage_payments(principal_amount, interest_rate_input, loan_term)

# Display the calculated payment amounts
print(f"Monthly Payment: {monthly}")
print(f"Semi-Monthly Payment: {semi_monthly}")
print(f"Bi-Weekly Payment: {bi_weekly}")
print(f"Weekly Payment: {weekly}")
print(f"Rapid Bi-Weekly Payment: {accelerated_bi_weekly}")
print(f"Rapid Weekly Payment: {accelerated_weekly}")