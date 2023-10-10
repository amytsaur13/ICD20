print("Welcome to the School Resource Assesment")
print("Location: BVG")
print("*Data Collection*")

print("1. Restrooms: ")
restrooms_input = int(input("How many restrooms are there? : "))
location_restrooms = input("Where are these restrooms? (sepreate by commas) : ")
describe_restrooms = input("How are the conditions of the restrooms? : ")

print("2. Water Fountains: ")
waterfountains_input = int(input("How many water fountains are there? : "))
location_waterfountains = input("Where are the Water Fountains? :")
describe_waterfountains = input("How are the conditions of the Water Fountains? : ")

print("3. Gyms : ")
gym_input = int(input("How many gyms are there? : "))
location_gym = input("Where are these gyms? : ")
describe_gym = input("How are the conditions of the gym? : ")

print("4. Change Rooms : ")
Change_rooms_input = int(input("How many change rooms are there? : "))
location_changerooms = input("Where are these Change Rooms? : ")
describe_changerooms = input("How are the conditions of the Water Fountains? : ")

print("5. Common Area : ")
common_area_input = int(input("How many common areas are there? : "))
locaition_common_area = input("Where are these common areas? : ")
describe_common_areas = input("How are the conditions of the common areas? : ")

print("6. Classroom : ")
classroom_input = int(input("How many classrooms are there?"))

print("** Data Colllection **")

print("1. Restrooms: ")
print(f"There are {restrooms_input} of Restooms in the school")
print(f" Locations: {location_restrooms}")
print(f"Conditions: {describe_restrooms}")

print("2. Water Fountains: ")
print(f" There are {waterfountains_input} of Water Fountains in the school")
print(f" Locations: {location_waterfountains}")
print(f" Conditions: {describe_waterfountains}")

print("3. Gyms : ")
print(f" There are {gym_input} of gyms in the school. ")
print(f" Locations: {location_gym}")
print(f" Conditions: {describe_gym}")

print("4. Change Rooms : ")
print(f" There are {Change_rooms_input} in the school")
print(f" Locations: {location_changerooms}")
print(f" Conditions: {describe_changerooms}")

print("5. Common Area : ")
print(f"There are {common_area_input} in the school")
print(f" Location: {locaition_common_area}")
print(f" Conditions: {describe_common_areas}")

print("6. Classroom : ")
print(f" Total number of classrooms: {classroom_input}")
print(f" Number of Water Fountains per classroom: {waterfountains_input/classroom_input}")
print(f" Number of Restrooms per classroom: {restrooms_input/classroom_input}")
print(f"Number of Gyms per classroom: {gym_input/classroom_input} ")
print(f"Number of change rooms per class room: {Change_rooms_input/classroom_input}")
print(f"Number of common areas per class room: {classroom_input/classroom_input}")