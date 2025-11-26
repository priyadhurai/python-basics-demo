"""
Python Basics Demonstration Script
Author: Banupriya
Description:
    This script demonstrates Python fundamentals including:
    - Variables and data types
    - Lists, tuples, sets, dictionaries
    - Conditions and loops
    - Functions
    - File handling
    - Exception handling
    - Simple data processing
"""

# --------------------------------------------------------
# 1. VARIABLES & DATA TYPES
# --------------------------------------------------------
name = "Banu"
age = 30
salary = 45000.50
is_active = True

print("----- Variables & Data Types -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Salary: {salary}")
print(f"Active Employee: {is_active}")
print(type(name), type(age), type(salary), type(is_active))


# --------------------------------------------------------
# 2. LIST, TUPLE, SET, DICTIONARY
# --------------------------------------------------------
fruits = ["apple", "banana", "mango"]  # List
coordinates = (12.5, 45.8)             # Tuple
unique_ids = {101, 102, 103, 103}      # Set (removes duplicates)
employee = {                           # Dictionary
    "id": 1,
    "name": "Banu",
    "department": "IT",
    "rating": 4.7
}

print("\n----- Data Structures -----")
print("List:", fruits)
print("Tuple:", coordinates)
print("Set (unique):", unique_ids)
print("Dictionary:", employee)


# --------------------------------------------------------
# 3. CONDITIONS
# --------------------------------------------------------
print("\n----- Conditions -----")
if age > 18:
    print("Employee is an adult.")
else:
    print("Employee is a minor.")


# --------------------------------------------------------
# 4. LOOPS
# --------------------------------------------------------
print("\n----- Loops -----")
print("For Loop Example:")
for fruit in fruits:
    print("Fruit:", fruit)

print("\nWhile Loop Example:")
count = 0
while count < 3:
    print("Count:", count)
    count += 1


# --------------------------------------------------------
# 5. FUNCTIONS
# --------------------------------------------------------
print("\n----- Functions -----")

def calculate_bonus(salary, rating):
    if rating > 4.5:
        return salary * 0.20
    elif rating > 4.0:
        return salary * 0.10
    else:
        return salary * 0.05

bonus = calculate_bonus(salary, employee["rating"])
print(f"Calculated Bonus: {bonus}")


# --------------------------------------------------------
# 6. FILE HANDLING
# --------------------------------------------------------
print("\n----- File Handling -----")

sample_text = "This is a sample file content for Python basics demo."

# Write to file
with open("sample_output.txt", "w") as f:
    f.write(sample_text)

# Read from file
with open("sample_output.txt", "r") as f:
    content = f.read()

print("File Content:", content)


# --------------------------------------------------------
# 7. EXCEPTION HANDLING
# --------------------------------------------------------
print("\n----- Exception Handling -----")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# --------------------------------------------------------
# 8. SIMPLE DATA PROCESSING EXAMPLE
# --------------------------------------------------------
print("\n----- Simple Data Processing -----")

numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
avg = total / len(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", avg)

print("\nProgram completed successfully.")
