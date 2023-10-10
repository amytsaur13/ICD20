total = float(input("Please enter a dollar amount: $ "))

t = total//2.0
total = total%2
l = total//1.0
total = total%1
q = total//0.25
total = total%0.25
d = total//0.10
total = total%0.10
n = total//0.05

print(f"There is {t} toonies, {l} loonies, {q} quarters, {d} dimes and {n} nickles")