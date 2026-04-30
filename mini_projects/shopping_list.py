# Shopping List Manager

shopping = []

while True:
    item = input("Enter item (or 'exit'): ")
    if item.lower() == "exit":
        break
    shopping.append(item)

print("Your Shopping List:", shopping)