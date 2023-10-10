name = input("What is your name?")
print(f"your name is: {name} ")

print(" ")

print("Game #1:")
name2 = input("What is your opponents name? ")
print(f"Opponents name: {name2}")
points1 = int(input("How many points did you get? "))
points2 = int(input("How many points did your opponent get? "))
print(f"Your Points: {points1}")
print(f"Opponents Points: {points2}")

print(" ")

print("Game #2:")
name3 = input("What is your opponents name? ")
print(f"Opponents name: {name3}")
points3 = int(input("How many points did you get? "))
points4 = int(input("How many points did your opponent get? "))
print(f"Your Points: {points3}")
print(f"Opponents Points: {points4}")

print(" ")

print("Game #3:")
name4 = input("What is your opponents name? ")
print(f"Opponents name: {name4}")
points5 = int(input("How many points did you get? "))
points6 = int(input("How many points did your opponent get? " ))
print(f"Your Points: {points5}")
print(f"Opponents Points: {points6}")

print(" ")

print("Game #4:")
name5 = input("What is your opponents name? ")
print(f"Opponents name: {name5}")
points7 = int(input("How many points did you get? "))
points8 = int(input("How many points did your opponent get? "))
print(f"Your Points: {points7}")
print(f"Opponents Points: {points8}")

print(" ")

print("Game #5:")
name6 = input("What is your opponents name? ")
print(f"Opponents name: {name6}")
points9 = int(input("How many points did you get? "))
points10 = int(input("How many points did your opponent get? "))
print(f"Your Points: {points9}")
print(f"Opponents Points: {points10}")

print(" ")

box1 = (f"{points1/81:.2%}")
box2 = (f"{points3/81:.2%}")
box3 = (f"{points5/81:.2%}")
box4 = (f"{points7/81:.2%}")
box5 = (f"{points9/81:.2%}")

print("Dots and Bots Tracker")
print(f"Players Name: {name}")

print(f"{'Opponent':<20}{'Your Points':>15}{'Opponent Points':>25}{'Box %':>15}")
print("==============================================================================")
print(f"{name2:<20}{points1:>15}{points2:>25}{box1:>15}")
print(f"{name3:<20}{points3:>15}{points4:>25}{box2:>15}")
print(f"{name4:<20}{points5:>15}{points6:>25}{box3:>15}")
print(f"{name5:<20}{points7:>15}{points8:>25}{box4:>15}")
print(f"{name6:<20}{points9:>15}{points10:>25}{box5:>15}")
print("==============================================================================")

total1 = points1+points3+points5+points7+points9

print("Summary:")
print(f"{'Total Points: '}{total1}")
print(f"{'Total Points of Opponent: '}{points2+points4+points6+points8+points10}")
print(f"{'Percentage Points Received: '}{total1/405:.2%}")

