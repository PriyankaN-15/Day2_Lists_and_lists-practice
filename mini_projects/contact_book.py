# Contact Book

contacts = {}

while True:
    name = input("Enter name (or 'exit'): ")
    if name.lower() == "exit":
        break

    phone = input("Enter phone number: ")
    contacts[name] = phone

print("\nSaved Contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)