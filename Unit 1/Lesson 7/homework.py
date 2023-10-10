import math
number = math.pi
print(f"{number: .3f}")

price = 2.99
print(f"${price:.2f}")

percentage = 0.075
print(f"{percentage: .2%}")

discount = 0.25
print(f"{discount: .1%}")

city = "New York"
print(f"{city:<15}")

La = "Los Angeles"
chi = "chicago"

temp = 72.5
print(f"{temp:^10}")

population = 600
area = 2.55
print(f"{'City':<11}{'population':<10} {'Area (sq km)':<10}")
print(f"{city:<12}{population:<12}{area:<10}")
print(f"{La:<12}{population:<9}{area:<10}")
print(f"{chi:<12}{population:<10}{area:<12}")
