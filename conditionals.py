day_of_week = input("Enter the day of the week").lower()
print (day_of_week )

if day_of_week == "saturday" or day_of_week == "sunday":
  print ("i will practice pythonol")
else:
  print ("i will learn DevOps")

 # calculator.py
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

choice = input("Enter the operation:(Opetions: +,-,*,/,%")

if choice == "+":
    result = num1 + num2
    print("The sum of two number is",result)
elif choice =="-":
    result = num1 - num2
    print("The difference of two number is",result)
elif choice == "*":
    result = num1 * num2
    print("The multiplication of two number is",result)
elif choice == "/":
    result = num1 / num2
    print("The division of two number is",result)
elif choice == "%":
    result = num1 % num2
    print("The modulus of two number is",result)
else:
    print("Invalid operation!")


