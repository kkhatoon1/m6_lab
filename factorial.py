#khateeja khatoon
# oct 29 2024 
#problem4 
# description: this program calculates the factorial of a user-input value using two methods:
#1. using the factorial function from the math module.
#2. using a for loop to calculater the factorial manually.
# finally, it compares the two results and prints whether they are equal.

import math 
#get user input for the value to calculate the factorial
user_input = int(input("enter a number to calculate its factorial:"))

#calculate factorial using the math
factorial_math = math.factorial(user_input)

#calculate factorial using a loop 
factorial_manual=1 
for i in range(1, user_input + 1):
    factorial_manual*= i 

    #print the results 
    print(f"factorial calculated using math.factorial:{factorial_math}")
    print(f"factorial calculated manually: {factorial_manual}")

    # compare the results 
    if factorial_math == factorial_manual:
        print("both methods produce the same result.")
    else: 
        print("the results are different.")