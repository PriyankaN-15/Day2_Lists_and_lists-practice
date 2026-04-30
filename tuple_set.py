# Tuple & Set Basics - Day 2

# Tuple
genders = ("male", "female", "others")
print("Tuple slice:", genders[1:3])

# Tuple repetition
repeated = (1, 2) * 3
print("Repeated:", repeated)

# Set
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference:", s1 - s2)

# Add & discard
s1.add(6)
s1.discard(10)

print("Updated set:", s1)