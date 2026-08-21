age = float(input("Enter your age in years: "))

total_days = age*365.25
total_hours = total_days*24
total_minutes = total_hours*60

print("You are approximately:\n")
print(f"- {round(total_days)} days old")
print(f"- {round(total_hours)} hours old")
print(f"- {round(total_minutes)} minutes old")