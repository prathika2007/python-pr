def DivExp(a, b):
 assert a > 0, "Assertion failed: a must be greater than 0"
 if b == 0:
  raise ZeroDivisionError("Division by zero is not allowed")
 return a / b
try:
 a = float(input("Enter value of a: "))
 b = float(input("Enter value of b: "))
 result = DivExp(a, b)
 print(f"Result: {a} / {b} = {result}")
except AssertionError as e:
 print(f"Assertion Error: {e}")
except ZeroDivisionError as e:
 print(f"Exception: {e}")