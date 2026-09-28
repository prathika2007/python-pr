
num_str = input("Enter a multi-digit number: ")

frequency = {}
for digit in num_str:
 if digit.isdigit():
  frequency[digit] = frequency.get(digit, 0) + 1
 print("\n--- Digit Frequency ---")
for digit, count in sorted(frequency.items()):
 print(f"Digit {digit} occurs {count} time(s)")