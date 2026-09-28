import csv
filename = input("Enter CSV filename: ")
data = []
with open(filename, newline='') as csvfile:
 reader = csv.DictReader(csvfile)
 for row in reader:
  data.append(row)
column = input("Enter column name to summarize (numeric): ")
values = [float(row[column]) for row in data if row[column].strip()]
print(f"\nMax {column}: {max(values)}")
print(f"Min {column}: {min(values)}")
print(f"Average {column}: {sum(values)/len(values):.2f}")