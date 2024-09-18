try:
    age=int(input("Please enter ur age: "))
except ValueError:
    print("This is not a valid reponse")
    break 
print(f"Your age is {age}")
print(f"In one year, you will be {age+1})
