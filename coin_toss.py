# FILE NAME - coin_toss.py

# NAME: Regina Swartout
# DATE: 2/18/26
# BRIEF DESCRIPTION:  A program that will randomly return Heads or Tails. To calculate, 
# a random number between 1 and 100 (inclusive) is generated and if the number is 51 or 
# greater then Tails is reported. Otherwise Heads is reported.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!

import random

num = random.randint(1,100)

if num >= 51:
    coin = "Tails"
else:
    coin = "Heads"

print("===== Coin Flipper =====")
print(coin)



########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
Remembering to import random, but luckily there was a comment reminding us to do it.  Thanks!







'''
