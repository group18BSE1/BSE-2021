c = int(input("Initial amount of an investment: "))
r = float(input("Yearly rate of interest: "))
t = int(input("Number of years until maturation: "))
n = int(input("Number of times the interest is compounded per year: "))
# calculating the final value of investment to the nearest penny
p = c*(1 + r/n)**(n*t)
print(round(p, 2))
