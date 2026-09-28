N = int(input("Enter the length of Fibonacci sequence: "))
fibonacci = []
a, b = 0, 1
for _ in range(N):
 fibonacci.append(a)
 a, b = b, a + b
print(f"Fibonacci sequence of length {N}:")
print(fibonacci)