p = float(input("Enter the principle: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period in years: "))
amount = p * (pow((1 + r / 100), t))
ci = amount - p
print("The compound interest is: ", ci)