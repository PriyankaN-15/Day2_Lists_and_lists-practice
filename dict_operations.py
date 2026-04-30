# Dictionary Operations - Day 2

student = {
    "name": "Priyanka",
    "age": 21
}

# Access
print("Name:", student["name"])

# Update
student["age"] = 22

# Add new key
student["branch"] = "ECE"

# Loop
for key, value in student.items():
    print(key, ":", value)