#khateeja khatoon
# oct 29 2024

# description: this program prints random integers betwee 25 and 35 using the randrange funtion from thre random module
#the numbers are store in 'rand_num'

import random 
rand_num = [] #initialize an empty list to store random number
for _ in range (10):
    random_number = random.randrange(25,36)
    rand_num.append(random_number)
    print("random integers between 25 and 36:", rand_num) #print the list of random number.