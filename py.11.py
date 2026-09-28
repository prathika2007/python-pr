class Complex:
 def __init__(self, real, imag):
    self.real = real
    self.imag = imag
 def __add__(self, other):
    return Complex(self.real + other.real, self.imag + other.imag)
 def __str__(self):
   return f"{self.real} + {self.imag}i"
def add_complex_numbers(numbers):
 result = Complex(0, 0)
 for num in numbers:
   result = result + num
 return result
N = int(input("Enter number of complex numbers (N >= 2): "))
numbers = []
for i in range(N):
 r = float(input(f"Enter real part of number {i+1}: "))
 im = float(input(f"Enter imaginary part of number {i+1}: "))
 numbers.append(Complex(r, im))
sum_result = add_complex_numbers(numbers)
print("\nSum of complex numbers =", sum_result)