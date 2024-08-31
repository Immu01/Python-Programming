principal=float(input("\nEnter the principal = "))
years=int(input("\nEnter the number of years = "))
interest=float(input("\nEnter the annual interest rate (in %) = "))
monthly_i=interest/1200
months=years*12
monthly_payment=principal*monthly_i*(1+monthly_i)**months/((1+monthly_i)**months-1)
print("\nMonth\tPayment\tInterest Paid\tRemaining Principal")
remaining=principal
for month in range(1,months+1):
    interest_paid=remaining*monthly_i
    remaining-=monthly_payment-interest_paid
    print(f"\n{month}\t{monthly_payment:.2f}\t{interest_paid:.2f}\t{remaining:.2f}")

# Output
# Enter the principal = 4000
# Enter the number of years = 2
# Enter the annual interest rate (in %) = 12
# Month   Payment Interest Paid   Remaining Principal
# 1       188.29  40.00   3851.71
# 2       188.29  38.52   3701.93
# 3       188.29  37.02   3550.65
# 4       188.29  35.51   3397.87
# 5       188.29  33.98   3243.55
# 6       188.29  32.44   3087.69
# 7       188.29  30.88   2930.28
# 8       188.29  29.30   2771.29
# 9       188.29  27.71   2610.70
# 10      188.29  26.11   2448.52
# 11      188.29  24.49   2284.71
# 12      188.29  22.85   2119.26
# 13      188.29  21.19   1952.16
# 14      188.29  19.52   1783.39
# 15      188.29  17.83   1612.93
# 16      188.29  16.13   1440.76
# 17      188.29  14.41   1266.88
# 18      188.29  12.67   1091.25
# 19      188.29  10.91   913.87
# 20      188.29  9.14    734.72
# 21      188.29  7.35    553.77
# 22      188.29  5.54    371.01
# 23      188.29  3.71    186.43
# 24      188.29  1.86    0.00