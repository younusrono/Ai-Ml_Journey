# _____________________Q1____________________

# 1. Open "names.txt" in write mode and get 5 names from the user
with open("names.txt", "w") as file:
    print("Enter 5 names:")
    for i in range(5):
        name = input(f"Name {i+1}: ")
        file.write(name + "\n")

# 2. Open the file in read mode and print all names
print("\nReading names from file:")
with open("names.txt", "r") as file:
    content = file.read()
    print(content, end="")

# _____________________Q2____________________

# 1. Open "log.txt" in append mode and add a new entry
with open("log.txt", "a") as file:
    file.write("Program run successfully\n")

# 2. Open the file in read mode and print all logs
print("Current logs:")
with open("log.txt", "r") as file:
    print(file.read(), end="")

# _____________________Q3____________________

# 1. Defined list of numbers
numbers = [5, 10, 15, 20, 25]

# 2. List comprehension filtering numbers greater than 15
filtered_numbers = [num for num in numbers if num > 15]

# 3. Print the new list
print("Numbers greater than 15:", filtered_numbers)


# _____________________Q4____________________

import json

# 1. Create a dictionary of 3 cities and populations, then save to "cities.json"
cities_data = {
    "New York": 8336000,
    "London": 8982000,
    "Tokyo": 13960000
}

with open("cities.json", "w") as file:
    json.dump(cities_data, file, indent=4)

# 2. Load the JSON and print each city and population
with open("cities.json", "r") as file:
    loaded_data = json.load(file)

print("Current Cities and Populations:")
for city, population in loaded_data.items():
    print(f"- {city}: {population:,}")

# 3. Ask user for a new entry and update the JSON file
new_city = input("\nEnter a new city name: ")
new_pop = int(input(f"Enter the population for {new_city}: "))

loaded_data[new_city] = new_pop

with open("cities.json", "w") as file:
    json.dump(loaded_data, file, indent=4)
    
print(f"Successfully updated 'cities.json' with {new_city}!")


# _____________________Q5____________________

# Try to open "data.txt" in read mode and handle FileNotFoundError
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
