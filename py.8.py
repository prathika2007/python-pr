def bubble_sort_desc(arr):
 n = len(arr)
 for i in range(n):
  for j in range(0, n - i - 1):
   if arr[j] < arr[j + 1]: #l
    arr[j], arr[j + 1] = arr[j + 1], arr[j]
 return arr

marks = []
print("Enter marks for 6 subjects:")
for i in range(6):
 mark = int(input(f"Enter mark for subject {i+1}: "))
 marks.append(mark)

sorted_marks = bubble_sort_desc(marks)

print("\n=== Student Marks Report ===")
print("Marks from highest to lowest:")
for m in sorted_marks:
 print(m)