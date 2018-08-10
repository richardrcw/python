import random

highest = 10

num = random.randint(1, highest)

guess = -1

while guess != num:
	guess = int(input("Guess number between 1 and {}: ".format(highest)))
	if guess > num:
		print("Lower...")
	elif guess < num:
		print("Higher....")
	else:
		print("Got it!")
