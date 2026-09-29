age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ")

if age >= 18 and not has_id.lower() == "no":
    print("Allowed")
else:
    print("Not allowed")
