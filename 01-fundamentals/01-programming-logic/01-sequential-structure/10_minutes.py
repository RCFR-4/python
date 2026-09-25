# Ask the user how many days, hours, and minutes they have, and convert the total time to minutes.

days = int(input("How many days do you have? "))
hours = int(input("How many hours do you have? "))
minutes = int(input("How many minutes do you have? "))

total_minutes = minutes + ((60 * (days * 24)) + (hours * 60))

print(f"The total time in minutes is: {total_minutes}")
