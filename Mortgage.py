def mortgage_payments(principal, rate, amortization):

    r = rate / 100.0

    def calc_payment(frequency):
        i = (1 + r / 2) ** (2 / frequency) - 1
        n = amortization * frequency
        payment = principal * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        return payment

    monthly = calc_payment(12)
    semi_monthly = calc_payment(24)
    bi_weekly = calc_payment(26)
    weekly = calc_payment(52)
    rapid_bi_weekly = monthly / 2
    rapid_weekly = monthly / 4

    return (monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly)

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the quoted interest rate (as a percent): "))
amortization = float(input("Enter the amortization period in years: "))

(monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly) = mortgage_payments(principal, rate, amortization)

print(f"Monthly Payment: ${monthly:.2f}")
print(f"Semi-monthly Payment: ${semi_monthly:.2f}")
print(f"Bi-weekly Payment: ${bi_weekly:.2f}")
print(f"Weekly Payment: ${weekly:.2f}")
print(f"Rapid Bi-weekly Payment: ${rapid_bi_weekly:.2f}")
print(f"Rapid Weekly Payment: ${rapid_weekly:.2f}")
