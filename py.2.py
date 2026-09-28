name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
from datetime import datetime
current_year = datetime.now().year
age = current_year - year_of_birth
# Check senior citizen status
print(f"\n Hello {name}, you are {age} years old.")
if age >= 60:
 print("Status: Senior Citizen ")
else:
 print("Status: Not a Senior Citizen ")