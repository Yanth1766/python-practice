age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no/student): ")

if age >= 18 and (has_id.lower() == "yes" or has_id.lower() == "student"):
    print("Allowed")
else:
    print("Not allowed")
