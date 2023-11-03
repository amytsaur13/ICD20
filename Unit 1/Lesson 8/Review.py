import math
number = math.pi
print(f"{number:.3f}")

price = float(29.99)
print(f"${price:.2f}")

tax_rate = 0.075
print(f"{tax_rate:.2%}")

discount = 0.25
print(f"{discount:.1%}")

city = "New York"
print(f"{city:<15}")

temperature = float(72.5)
print(f"{temperature:10}")

item = "Product"
price = 25.99
quanity = 3
total = price * quanity

Item = "Item"
Price = "Price"
Quanity = "Quanity"
Total = "Total"


print(f"{Item:<9}{Price:>7}{Quanity:>10}{Total:>8}")
print(f"{item:.<9}{price:>7}{quanity:>10}{total:>8}")

city = "City"
population = "Population"
area = "Area (sq km)"
ny = "New York"
chi = "Chicago"
la = "Los Angeles"
pop1 = "8,398,748"
area1 = "468.19"
pop2 = "2,693,976"
area2 = "227.63"
pop3 = "3,990,456"
area3 = "227.63"



print(f"{city:<14}{population:>12}{area:>16}")
print(f"{ny:<14}{pop1:>11}{area1:>11}")
print(f"{chi:<14}{pop2:>11}{area2:>11}")
print(f"{la:<14}{pop3:>11}{area3:>11}")
