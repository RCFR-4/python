# Ask the user how many days, hours, and minutes they have, and convert the total time to minutes.

days = int(input("how many days you have? "))
hours = int(input("how many hours you have? "))
minutes = int(input("how many minutes you have? "))

total_minutes = minutes + ((60 * (days * 24)) + (hours * 60))

print(f"the total time in minutes is: {total_minutes}")
