credits=int(input("\nEnter the number of credits earned = "))
if credits>=90:
    print("\nSenior status")
elif credits>=60 and credits<90:
    print("\nJunior status")
elif credits>=30 and credits<60:
    print("\nSophomore status")
else:
    print("\nFreshman status")

# Output
# Enter the number of credits earned = 55
# Sophomore status