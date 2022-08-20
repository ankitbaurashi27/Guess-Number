import random
import math

#for taking input from user
min = int(input("Enter minmum value:- "))

max = int(input("Enter maximum value:- "))

# random number between
# the min and max
x = random.randint(min, max)
print("\n\tYou've only ", round(math.log(max - min + 1, 2)),
	" chances to guess the integer!\n")

# Initializing the number of count / guess to zero.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(max - min + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Hurray you did it in ", count, " try")
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")


if count >= math.log(max - min + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
