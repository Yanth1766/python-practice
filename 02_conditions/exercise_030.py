age = int(input("Enter your age: "))
marks = int(input("Enter your scores: "))

if age >= 18 and marks >= 40:
    print("Pass")
elif age >= 18 and marks < 40:
    print("Fail")
else:
    print("Minor")
