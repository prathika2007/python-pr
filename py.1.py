num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Display menu
print("\nChoose operation:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
choice = int(input("Enter your choice (1-4): "))
# Performing operation
if choice == 1:
 result = num1 + num2
 print(f"Result: {num1} + {num2} = {result}")
elif choice == 2:
 result = num1 - num2
 print(f"Result: {num1} - {num2} = {result}")
elif choice == 3:
 result = num1 * num2
 print(f"Result: {num1} * {num2} = {result}")
elif choice == 4:
 if num2 != 0:
  result = num1 / num2
 print(f"Result: {num1} / {num2} = {result}")
else:
  print("Error: Division by zero is not allowed.")
