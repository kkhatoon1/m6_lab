# khateeja khatoon
# oct 29 2024
#problem 3 
# description: this program stimulates a coin flip where "heads" occurs x% of the time and "tails" occurs (100-x)% of the time.
# the program flips the coin 1000 times and calculates the percentage of heads in the results.

import random 
x = 78
# initialize 
coin_flips =[]  
for _ in range(1000):
    #generate random numbers between 1 and 100 
    flip = random.randint(1, 100)
    if flip <=x:
       coin_flips.append("heads")
    else:
        coin_flips.append("tails")
        #calculate occurance of heads in the list 
        heads_count = coin_flips.count("heads")
        # calculate percentage of heads 
        heads_percentage = (heads_count/ 1000)*100
        #print the results 
        print(f"heads count: {heads_count} times out of 1000 flips")
        print(f"heads percentage: {heads_percentage}%")
