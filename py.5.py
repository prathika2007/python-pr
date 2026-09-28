import math
N = int(input("Enter how many numbers: "))
numbers = []
for i in range(N):
 num = float(input(f"Enter number {i+1}: "))
 numbers.append(num)
mean = sum(numbers) / N
variance = sum((x - mean) ** 2 for x in numbers) / N
std_dev = math.sqrt(variance)
print("\n--- Results ---")
print(f"Numbers: {numbers}")
print(f"Mean = {mean:.2f}")
print(f"Variance = {variance:.2f}")
print(f"Standard Deviation = {std_dev:.2f}")