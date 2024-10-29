#khateeja khatoon
#oct 29 2024 
#program 2
# description: this program selects a ramdom day of the week from the list and prints a message indicationg that it was a rainy day with lightning.

import random
#list of days of the week 
days_of_week =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
#use random choice to select random day from the list 
random_day = random.choice(days_of_week)

#print the message with selected day 
print(f"it was a rainy {random_day} and the lightning flashed across the sky.")