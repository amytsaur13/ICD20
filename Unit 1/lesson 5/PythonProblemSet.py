# main = float(input("What is the price of your main course?"))
# apppetizer = float(input("What is the price of your appetizer?"))
# drink = float(input("What is the price of your drink?"))
# desert = float(input("What is the price of your desert"))
# tip_rate = float(input("Enter your tip rate (as a percentage)"))
# Taylor_Swift = (f"{main+apppetizer+drink+desert+tip_rate}")

# print("Bill Summary")
# print(f"Subtotal: ${Taylor_Swift}")
# print(f"Tip: {tip_rate}: ${Taylor_Swift * tip_rate / 100} ")
# print(f"Total Cost: $ {Taylor_Swift + tip_rate}")

# length_wall = input("What is the length of the wall?")
# width_wall = input("What is the width of wall?")
# height_house = input("What is the height of the wall?")
# cost_brick = input("What is the cost of the brick?")

# length_brick = input("What is the lengith of the brick")
# width_brick = input("What is the width of the brick?")
# height_brick = input("What is the height of the brick?")

# sa = length_brick * width_wall * 4 
# bricks_volume = length_brick*width_brick*height_brick
# bricks = sa/bricks_volume

# print("House Details: ")
# print(f"Wall surface area: {sa}" )
# print(f"Brick Required: {bricks}")

distance = float(input("What is the distance of the trip?"))
efficancy = float(input("What is the fuel efficancy of your car in km/l"))
price = float(input("What is the price for gas?"))
passengers = int(input("How many people in the car?"))

print(f"You will need a total of {distance/efficancy} liters of gas")
print(f"It will cost: {distance/efficancy*price}")
print(f"It will only cost: {distance/efficancy*price/passengers} per passenger")
